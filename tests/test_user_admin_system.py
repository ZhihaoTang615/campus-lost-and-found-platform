"""Tests for the lecturer-requested user and read-only admin systems.

The database doubles in this module deliberately implement only the small
mysql.connector surface used by the Flask routes.  No test in this file needs
or attempts to connect to a live MySQL server.
"""

from datetime import date, datetime
from html import unescape
import re
from urllib.parse import parse_qs, urlsplit

import pytest
from werkzeug.security import check_password_hash, generate_password_hash

import app as app_module


def normalize_sql(query):
    """Collapse SQL whitespace so assertions focus on query behaviour."""

    return " ".join(query.split())


def visible_text(response):
    """Return readable response text without depending on HTML structure."""

    html = response.get_data(as_text=True)
    without_tags = re.sub(r"<[^>]+>", " ", html)
    return " ".join(unescape(without_tags).split())


def navigation_link_labels(response):
    """Return the ordered text labels for links in the primary navigation."""

    html = response.get_data(as_text=True)
    navigation_match = re.search(
        r'<nav\b[^>]*aria-label="Primary navigation"[^>]*>(.*?)</nav>',
        html,
        flags=re.IGNORECASE | re.DOTALL,
    )
    assert navigation_match is not None
    link_contents = re.findall(
        r"<a\b[^>]*>(.*?)</a>",
        navigation_match.group(1),
        flags=re.IGNORECASE | re.DOTALL,
    )
    return [
        " ".join(re.sub(r"<[^>]+>", " ", content).split())
        for content in link_contents
    ]


def assert_login_redirect(response, expected_next):
    """Assert a protected request redirects to login with a local next path."""

    assert response.status_code == 302
    destination = urlsplit(response.headers["Location"])
    assert destination.path == "/login"
    assert destination.scheme == ""
    assert destination.netloc == ""
    assert parse_qs(destination.query).get("next") == [expected_next]


class SequencedCursor:
    """A cursor with queued fetch results for multi-query routes."""

    def __init__(self, fetchone_results=None, fetchall_results=None):
        self.fetchone_results = list(fetchone_results or [])
        self.fetchall_results = list(fetchall_results or [])
        self.executed = []
        self.dictionary = False
        self.closed = False

    def execute(self, query, parameters=None):
        self.executed.append((query, parameters))

    def fetchone(self):
        if not self.fetchone_results:
            return None
        return self.fetchone_results.pop(0)

    def fetchall(self):
        if not self.fetchall_results:
            return []
        return list(self.fetchall_results.pop(0))

    def close(self):
        self.closed = True


class SequencedConnection:
    """A connection double that exposes one reusable cursor."""

    def __init__(self, cursor):
        self.cursor_instance = cursor
        self.committed = False
        self.closed = False

    def cursor(self, dictionary=False):
        self.cursor_instance.dictionary = dictionary
        return self.cursor_instance

    def commit(self):
        self.committed = True

    def is_connected(self):
        return not self.closed

    def close(self):
        self.closed = True


class DuplicateEmailCursor(SequencedCursor):
    """Support either pre-insert duplicate checks or integrity handling."""

    def execute(self, query, parameters=None):
        super().execute(query, parameters)
        if "insert into users" in normalize_sql(query).lower():
            raise app_module.mysql.connector.IntegrityError(
                "Duplicate entry for unique email"
            )


def install_database(
    monkeypatch,
    *,
    fetchone_results=None,
    fetchall_results=None,
    cursor_class=SequencedCursor,
):
    """Install and return a controlled database connection."""

    cursor = cursor_class(
        fetchone_results=fetchone_results,
        fetchall_results=fetchall_results,
    )
    connection = SequencedConnection(cursor)
    monkeypatch.setattr(
        app_module,
        "get_database_connection",
        lambda: connection,
    )
    return connection


def matching_execution(cursor, sql_fragment):
    """Return the first recorded execution matching a SQL fragment."""

    fragment = sql_fragment.lower()
    for query, parameters in cursor.executed:
        if fragment in normalize_sql(query).lower():
            return query, parameters
    raise AssertionError(f"No SQL execution contained {sql_fragment!r}")


def insert_values(cursor, table_name):
    """Map an INSERT's named columns to its parameter values."""

    query, parameters = matching_execution(
        cursor,
        f"insert into {table_name}",
    )
    match = re.search(
        rf"insert\s+into\s+{re.escape(table_name)}\s*\((.*?)\)\s*values",
        query,
        flags=re.IGNORECASE | re.DOTALL,
    )
    assert match is not None, "INSERT should name its target columns"
    columns = [
        column.strip().strip("`").lower()
        for column in match.group(1).split(",")
    ]
    assert parameters is not None
    assert len(columns) == len(parameters)
    return dict(zip(columns, parameters))


def authenticate_session(client, user_id=42, name="Test User", role="user"):
    """Place only trusted authentication values in the test session."""

    with client.session_transaction() as flask_session:
        flask_session.clear()
        flask_session["user_id"] = user_id
        flask_session["user_name"] = name
        flask_session["user_role"] = role


def registration_data(**overrides):
    data = {
        "full_name": "Zhihao Tang",
        "email": "ZHIHAO@EXAMPLE.COM",
        "password": "secure-password",
        "confirm_password": "secure-password",
    }
    data.update(overrides)
    return data


def lost_item_data():
    return {
        "item-name": "Black Backpack",
        "category": "Bag",
        "location": "Computer Lab",
        "date-lost": "2026-07-13",
        "description": "Black backpack with notebooks inside.",
        "contact": "zhihao@example.com",
    }


def sample_found_item():
    return {
        "id": 7,
        "item_name": "Student ID Card",
        "category": "Card",
        "report_type": "found",
        "location": "Cafeteria",
        "report_date": date(2026, 7, 12),
        "description": "Student ID card found near the west entrance.",
        "contact_information": "owner@example.com",
        "status": "Unclaimed",
        "image_path": None,
    }


def claim_data():
    return {
        "name": "Zhihao Tang",
        "contact": "zhihao@example.com",
        "message": "The card contains my student number.",
    }


# Registration


def test_registration_page_loads(client):
    response = client.get("/register")

    assert response.status_code == 200
    assert b"<form" in response.data.lower()


def test_successful_registration_normalizes_email_and_hashes_password(
    client,
    monkeypatch,
):
    connection = install_database(monkeypatch, fetchone_results=[None])

    response = client.post(
        "/register",
        data=registration_data(),
        follow_redirects=False,
    )

    assert response.status_code == 302
    assert urlsplit(response.headers["Location"]).path == "/login"
    assert connection.committed is True

    login_page = client.get(response.headers["Location"])
    assert b"registration successful" in login_page.data.lower()

    values = insert_values(connection.cursor_instance, "users")
    assert values["full_name"] == "Zhihao Tang"
    assert values["email"] == "zhihao@example.com"
    assert values["password_hash"] != "secure-password"
    assert "secure-password" not in values["password_hash"]
    assert check_password_hash(values["password_hash"], "secure-password")
    assert values["role"] == "user"
    assert connection.cursor_instance.closed is True
    assert connection.closed is True


def test_public_registration_ignores_attempted_admin_role(client, monkeypatch):
    connection = install_database(monkeypatch, fetchone_results=[None])
    submitted = registration_data(role="admin")

    response = client.post("/register", data=submitted)

    assert response.status_code in {200, 302}
    values = insert_values(connection.cursor_instance, "users")
    assert values["role"] == "user"
    assert "admin" not in values.values()


def test_duplicate_registration_is_rejected_with_friendly_message(
    client,
    monkeypatch,
):
    connection = install_database(
        monkeypatch,
        fetchone_results=[{"id": 9}],
        cursor_class=DuplicateEmailCursor,
    )

    response = client.post(
        "/register",
        data=registration_data(),
        follow_redirects=True,
    )

    assert response.status_code == 200
    page = response.get_data(as_text=True).lower()
    assert "already" in page or "exists" in page or "registered" in page
    assert connection.committed is False


@pytest.mark.parametrize(
    "overrides",
    [
        {"full_name": ""},
        {"email": ""},
        {"password": ""},
        {"confirm_password": ""},
    ],
)
def test_registration_rejects_missing_fields(client, monkeypatch, overrides):
    connection = install_database(monkeypatch)

    response = client.post(
        "/register",
        data=registration_data(**overrides),
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert not any(
        "insert into users" in normalize_sql(query).lower()
        for query, _ in connection.cursor_instance.executed
    )
    assert connection.committed is False


@pytest.mark.parametrize(
    "overrides",
    [
        {"full_name": "   \t"},
        {"email": "   \t"},
        {"password": "        ", "confirm_password": "        "},
    ],
)
def test_registration_rejects_whitespace_only_values(
    client,
    monkeypatch,
    overrides,
):
    connection = install_database(monkeypatch)

    response = client.post(
        "/register",
        data=registration_data(**overrides),
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert not any(
        "insert into users" in normalize_sql(query).lower()
        for query, _ in connection.cursor_instance.executed
    )
    assert connection.committed is False


def test_registration_rejects_invalid_email(client, monkeypatch):
    connection = install_database(monkeypatch)

    response = client.post(
        "/register",
        data=registration_data(email="not-an-email"),
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert connection.cursor_instance.executed == []
    assert connection.committed is False


def test_registration_rejects_short_password(client, monkeypatch):
    connection = install_database(monkeypatch)

    response = client.post(
        "/register",
        data=registration_data(password="short", confirm_password="short"),
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert connection.cursor_instance.executed == []
    assert connection.committed is False


def test_registration_rejects_mismatched_passwords(client, monkeypatch):
    connection = install_database(monkeypatch)

    response = client.post(
        "/register",
        data=registration_data(confirm_password="different-password"),
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert connection.cursor_instance.executed == []
    assert connection.committed is False


# Login, logout, and authorization


def account_record(role="user"):
    return {
        "id": 42 if role == "user" else 1,
        "full_name": "Zhihao Tang" if role == "user" else "Site Admin",
        "email": "zhihao@example.com" if role == "user" else "admin@example.com",
        "password_hash": generate_password_hash("secure-password"),
        "role": role,
    }


def test_login_page_loads(client):
    response = client.get("/login")

    assert response.status_code == 200
    assert b"<form" in response.data.lower()


def test_valid_normal_user_login_sets_session_and_normalizes_email(
    client,
    monkeypatch,
):
    account = account_record("user")
    connection = install_database(monkeypatch, fetchone_results=[account])
    with client.session_transaction() as flask_session:
        flask_session["user_id"] = 999
        flask_session["user_name"] = "Old User"
        flask_session["user_role"] = "admin"

    response = client.post(
        "/login",
        data={"email": "  ZHIHAO@EXAMPLE.COM  ", "password": "secure-password"},
        follow_redirects=False,
    )

    assert response.status_code == 302
    assert urlsplit(response.headers["Location"]).path == "/my-reports"
    _, parameters = matching_execution(connection.cursor_instance, "from users")
    assert parameters == ("zhihao@example.com",)
    with client.session_transaction() as flask_session:
        assert flask_session["user_id"] == 42
        assert flask_session["user_name"] == "Zhihao Tang"
        assert flask_session["user_role"] == "user"
        assert "password" not in flask_session
        assert "password_hash" not in flask_session
    assert connection.cursor_instance.closed is True
    assert connection.closed is True


def test_valid_admin_login_sets_session_and_redirects_to_admin(
    client,
    monkeypatch,
):
    account = account_record("admin")
    install_database(monkeypatch, fetchone_results=[account])

    response = client.post(
        "/login",
        data={"email": "ADMIN@EXAMPLE.COM", "password": "secure-password"},
        follow_redirects=False,
    )

    assert response.status_code == 302
    assert urlsplit(response.headers["Location"]).path == "/admin"
    with client.session_transaction() as flask_session:
        assert flask_session["user_id"] == 1
        assert flask_session["user_name"] == "Site Admin"
        assert flask_session["user_role"] == "admin"


@pytest.mark.parametrize(
    ("database_account", "password"),
    [
        (None, "secure-password"),
        (account_record("user"), "wrong-password"),
    ],
)
def test_invalid_login_uses_generic_message(
    client,
    monkeypatch,
    database_account,
    password,
):
    install_database(monkeypatch, fetchone_results=[database_account])

    response = client.post(
        "/login",
        data={"email": "unknown@example.com", "password": password},
        follow_redirects=True,
    )

    assert response.status_code == 200
    page = response.get_data(as_text=True).lower()
    assert "invalid email or password" in page
    assert "account does not exist" not in page
    assert "email not found" not in page
    with client.session_transaction() as flask_session:
        assert "user_id" not in flask_session
        assert "user_role" not in flask_session


def test_login_does_not_allow_external_next_redirect(client, monkeypatch):
    assert app_module.is_safe_next_url("//evil.example/steal") is False
    assert app_module.is_safe_next_url("/%2f%2fevil.example/steal") is False
    assert app_module.is_safe_next_url("/%5cevil.example/steal") is False
    install_database(monkeypatch, fetchone_results=[account_record("user")])

    response = client.post(
        "/login?next=https://evil.example/steal",
        data={"email": "zhihao@example.com", "password": "secure-password"},
        follow_redirects=False,
    )

    assert response.status_code == 302
    destination = urlsplit(response.headers["Location"])
    assert destination.netloc == ""
    assert destination.scheme == ""
    assert destination.path == "/my-reports"


def test_login_returns_normal_user_to_safe_requested_page(client, monkeypatch):
    install_database(monkeypatch, fetchone_results=[account_record("user")])

    response = client.post(
        "/login",
        data={
            "email": "zhihao@example.com",
            "password": "secure-password",
            "next": "/items?q=backpack",
        },
        follow_redirects=False,
    )

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/items?q=backpack")


def test_login_returns_admin_to_safe_admin_page(client, monkeypatch):
    install_database(monkeypatch, fetchone_results=[account_record("admin")])

    response = client.post(
        "/login",
        data={
            "email": "admin@example.com",
            "password": "secure-password",
            "next": "/admin",
        },
        follow_redirects=False,
    )

    assert response.status_code == 302
    assert urlsplit(response.headers["Location"]).path == "/admin"


@pytest.mark.parametrize("admin_path", ["/admin", "/db-test"])
def test_normal_user_login_does_not_return_to_admin_only_next(
    client,
    monkeypatch,
    admin_path,
):
    install_database(monkeypatch, fetchone_results=[account_record("user")])

    response = client.post(
        "/login",
        data={
            "email": "zhihao@example.com",
            "password": "secure-password",
            "next": admin_path,
        },
        follow_redirects=False,
    )

    assert response.status_code == 302
    assert urlsplit(response.headers["Location"]).path == "/my-reports"


def test_logout_clears_authentication_session(client):
    authenticate_session(client)

    response = client.post("/logout", follow_redirects=True)

    assert response.status_code == 200
    assert "logged out" in response.get_data(as_text=True).lower()
    with client.session_transaction() as flask_session:
        assert "user_id" not in flask_session
        assert "user_name" not in flask_session
        assert "user_role" not in flask_session


def test_logout_is_post_only(client):
    response = client.get("/logout")

    assert response.status_code == 405


def test_my_reports_requires_login_and_preserves_local_next(client):
    response = client.get("/my-reports", follow_redirects=False)

    assert_login_redirect(response, "/my-reports")


@pytest.mark.parametrize(
    "path",
    [
        "/items",
        "/report-lost-item",
        "/report-found-item",
        "/item-details",
        "/items/7",
        "/claim-request/7",
        "/claim-success/7",
    ],
)
def test_logged_out_protected_get_redirects_without_database(
    client,
    monkeypatch,
    path,
):
    def fail_if_database_is_opened():
        raise AssertionError("A logged-out protected request must not query data")

    monkeypatch.setattr(
        app_module,
        "get_database_connection",
        fail_if_database_is_opened,
    )

    response = client.get(path, follow_redirects=False)

    assert_login_redirect(response, path)


def test_protected_query_string_is_preserved_as_safe_next(client, monkeypatch):
    def fail_if_database_is_opened():
        raise AssertionError("Authentication must run before item searching")

    monkeypatch.setattr(
        app_module,
        "get_database_connection",
        fail_if_database_is_opened,
    )

    response = client.get(
        "/items?q=backpack&category=Bag",
        follow_redirects=False,
    )

    assert_login_redirect(response, "/items?q=backpack&category=Bag")


def test_admin_requires_login(client, monkeypatch):
    def fail_if_database_is_opened():
        raise AssertionError("A logged-out admin request must not query data")

    monkeypatch.setattr(
        app_module,
        "get_database_connection",
        fail_if_database_is_opened,
    )

    response = client.get("/admin", follow_redirects=False)
    diagnostic_response = client.get("/db-test", follow_redirects=False)

    assert_login_redirect(response, "/admin")
    assert_login_redirect(diagnostic_response, "/db-test")


def test_normal_user_cannot_access_admin(client, monkeypatch):
    authenticate_session(client, role="user")

    def fail_if_database_is_opened():
        raise AssertionError("A denied user must not query admin data")

    monkeypatch.setattr(
        app_module,
        "get_database_connection",
        fail_if_database_is_opened,
    )

    response = client.get("/admin", follow_redirects=False)
    diagnostic_response = client.get("/db-test", follow_redirects=False)

    assert response.status_code == 403
    assert diagnostic_response.status_code == 403


@pytest.mark.parametrize("path", ["/admin", "/db-test"])
def test_invalid_user_id_cannot_use_forged_admin_role(
    client,
    monkeypatch,
    path,
):
    authenticate_session(client, user_id=True, role="admin")

    def fail_if_database_is_opened():
        raise AssertionError("An invalid session must not query admin data")

    monkeypatch.setattr(
        app_module,
        "get_database_connection",
        fail_if_database_is_opened,
    )

    response = client.get(path, follow_redirects=False)

    assert_login_redirect(response, path)


@pytest.mark.parametrize(
    ("path", "expected_status"),
    [
        ("/items", 200),
        ("/report-lost-item", 200),
        ("/report-found-item", 200),
        ("/item-details", 302),
        ("/items/7", 200),
        ("/claim-request/7", 200),
        ("/claim-success/7", 200),
        ("/my-reports", 200),
    ],
)
def test_administrator_can_access_normal_user_routes(
    administrator_client,
    fake_db,
    path,
    expected_status,
):
    item = sample_found_item()
    fake_db(rows=[item], row=item)

    response = administrator_client.get(path, follow_redirects=False)

    assert response.status_code == expected_status
    if path == "/item-details":
        assert urlsplit(response.headers["Location"]).path == "/items"


def test_administrator_can_access_database_diagnostic(
    administrator_client,
    fake_db,
):
    connection = fake_db(rows=[("claims",), ("items",), ("users",)])

    response = administrator_client.get("/db-test")

    assert response.status_code == 200
    assert response.get_json() == {
        "message": "Database connection successful.",
        "tables": ["claims", "items", "users"],
    }
    query, parameters = connection.cursor_instance.executed[0]
    assert normalize_sql(query) == "SHOW TABLES"
    assert parameters is None
    assert connection.cursor_instance.closed is True
    assert connection.closed is True


@pytest.mark.parametrize(
    ("path", "table_name", "submitted_data", "selected_item"),
    [
        ("/report-lost-item", "items", lost_item_data(), None),
        (
            "/report-found-item",
            "items",
            {**lost_item_data(), "date-found": "2026-07-13"},
            None,
        ),
        ("/claim-request/7", "claims", claim_data(), sample_found_item()),
    ],
)
def test_administrator_can_create_normal_records_with_own_user_id(
    administrator_client,
    monkeypatch,
    path,
    table_name,
    submitted_data,
    selected_item,
):
    fetchone_results = [selected_item] if selected_item is not None else []
    connection = install_database(
        monkeypatch,
        fetchone_results=fetchone_results,
    )

    response = administrator_client.post(
        path,
        data=submitted_data,
        follow_redirects=False,
    )

    assert response.status_code == 302
    values = insert_values(connection.cursor_instance, table_name)
    assert values["user_id"] == 1


# Shared navigation


def test_logged_out_home_and_navigation_offer_only_login_and_register(client):
    response = client.get("/")

    assert response.status_code == 200
    assert navigation_link_labels(response) == ["Login", "Register"]
    assert b'href="/login"' in response.data
    assert b'href="/register"' in response.data
    for protected_target in (
        b'href="/items"',
        b'href="/report-lost-item"',
        b'href="/report-found-item"',
        b'href="/my-reports"',
        b'href="/admin"',
        b'action="/logout"',
    ):
        assert protected_target not in response.data


def test_logged_out_static_access_is_limited_to_entry_page_assets(
    client,
    monkeypatch,
):
    def fail_if_database_is_opened():
        raise AssertionError("Static access must not query application data")

    monkeypatch.setattr(
        app_module,
        "get_database_connection",
        fail_if_database_is_opened,
    )

    for public_asset in (
        "/static/css/style.css",
        "/static/js/ui-feedback.js",
    ):
        response = client.get(public_asset, follow_redirects=False)
        assert response.status_code == 200

    for protected_asset in (
        "/static/styles.css",
        "/static/script.js",
        "/static/uploads/MacBook_Charger.jpg",
    ):
        response = client.get(protected_asset, follow_redirects=False)
        assert_login_redirect(response, protected_asset)


def test_logged_in_user_navigation_shows_name_my_reports_and_post_logout(client):
    authenticate_session(client, user_id=42, name="Zhihao Tang", role="user")

    response = client.get("/")

    assert response.status_code == 200
    assert navigation_link_labels(response) == [
        "Home",
        "Browse Items",
        "Report Lost Item",
        "Report Found Item",
        "My Reports",
    ]
    text = visible_text(response)
    assert "Zhihao Tang" in text
    assert "Logout" in text
    assert "Admin Dashboard" not in text
    assert "Login" not in navigation_link_labels(response)
    assert "Register" not in navigation_link_labels(response)
    assert b'action="/logout"' in response.data
    assert b'method="post"' in response.data.lower()


def test_admin_navigation_shows_admin_dashboard_and_my_reports(client):
    authenticate_session(client, user_id=1, name="Site Admin", role="admin")

    response = client.get("/")

    assert response.status_code == 200
    assert navigation_link_labels(response) == [
        "Home",
        "Browse Items",
        "Report Lost Item",
        "Report Found Item",
        "My Reports",
        "Admin Dashboard",
    ]
    text = visible_text(response)
    assert "Site Admin" in text
    assert "Logout" in text
    assert b'action="/logout"' in response.data
    assert b'method="post"' in response.data.lower()


# Item and claim ownership


def test_logged_in_item_report_stores_user_id(client, monkeypatch):
    authenticate_session(client, user_id=42)
    connection = install_database(monkeypatch)
    submitted_item = lost_item_data()
    submitted_item["user_id"] = "999"

    response = client.post(
        "/report-lost-item",
        data=submitted_item,
        follow_redirects=False,
    )

    assert response.status_code == 302
    values = insert_values(connection.cursor_instance, "items")
    assert values["user_id"] == 42


@pytest.mark.parametrize(
    ("path", "submitted_data"),
    [
        ("/report-lost-item", lost_item_data()),
        ("/report-found-item", {"date-found": "2026-07-13"}),
        ("/claim-request/7", claim_data()),
        ("/logout", {}),
    ],
)
def test_logged_out_protected_post_redirects_without_database(
    client,
    monkeypatch,
    path,
    submitted_data,
):
    def fail_if_database_is_opened():
        raise AssertionError("A logged-out protected POST must not query data")

    monkeypatch.setattr(
        app_module,
        "get_database_connection",
        fail_if_database_is_opened,
    )

    response = client.post(
        path,
        data=submitted_data,
        follow_redirects=False,
    )

    assert_login_redirect(response, path)


def test_logged_in_claim_stores_user_id(client, monkeypatch):
    authenticate_session(client, user_id=42)
    connection = install_database(
        monkeypatch,
        fetchone_results=[sample_found_item()],
    )
    submitted_claim = claim_data()
    submitted_claim["user_id"] = "999"

    response = client.post(
        "/claim-request/7",
        data=submitted_claim,
        follow_redirects=False,
    )

    assert response.status_code == 302
    values = insert_values(connection.cursor_instance, "claims")
    assert values["user_id"] == 42
    assert values["status"] == "pending"


@pytest.mark.parametrize("invalid_user_id", [None, 0, -1, "42", True])
def test_invalid_session_user_id_cannot_create_item_report(
    client,
    monkeypatch,
    invalid_user_id,
):
    with client.session_transaction() as flask_session:
        flask_session.clear()
        if invalid_user_id is not None:
            flask_session["user_id"] = invalid_user_id
        flask_session["user_name"] = "Invalid Session"
        flask_session["user_role"] = "user"

    def fail_if_database_is_opened():
        raise AssertionError("An invalid session must not create a record")

    monkeypatch.setattr(
        app_module,
        "get_database_connection",
        fail_if_database_is_opened,
    )

    response = client.post(
        "/report-lost-item",
        data=lost_item_data(),
        follow_redirects=False,
    )

    assert_login_redirect(response, "/report-lost-item")


# My Reports


def report_record(item_id, name, user_id):
    return {
        "id": item_id,
        "item_name": name,
        "report_type": "lost",
        "category": "Bag",
        "location": "Computer Lab",
        "report_date": date(2026, 7, item_id),
        "status": "Open",
        "user_id": user_id,
        "created_at": datetime(2026, 7, item_id, 12, 0),
    }


def test_my_reports_filters_query_by_logged_in_user(client, monkeypatch):
    authenticate_session(client, user_id=101, name="First User")
    connection = install_database(
        monkeypatch,
        fetchall_results=[[report_record(1, "First User Backpack", 101)]],
    )

    response = client.get("/my-reports")

    assert response.status_code == 200
    assert b"First User Backpack" in response.data
    query, parameters = matching_execution(connection.cursor_instance, "from items")
    normalized = normalize_sql(query).lower()
    assert "user_id = %s" in normalized
    assert parameters == (101,)
    assert "order by" in normalized
    assert "desc" in normalized
    assert connection.cursor_instance.closed is True
    assert connection.closed is True


def test_my_reports_displays_required_record_fields_and_navigation(
    client,
    monkeypatch,
):
    authenticate_session(client, user_id=101, name="First User")
    install_database(
        monkeypatch,
        fetchall_results=[[report_record(1, "First User Backpack", 101)]],
    )

    response = client.get("/my-reports")

    assert response.status_code == 200
    text = visible_text(response)
    assert "First User Backpack" in text
    assert "Lost" in text
    assert "Bag" in text
    assert "Computer Lab" in text
    assert "2026-07-01" in text
    assert "Open" in text
    assert b'href="/report-lost-item"' in response.data
    assert b'href="/report-found-item"' in response.data
    assert b'href="/items"' in response.data
    assert b'href="/items/1"' in response.data


def test_administrator_my_reports_still_filters_by_own_account(
    client,
    monkeypatch,
):
    authenticate_session(client, user_id=1, name="Site Admin", role="admin")
    connection = install_database(
        monkeypatch,
        fetchall_results=[[report_record(1, "Admin Report", 1)]],
    )

    response = client.get("/my-reports")

    assert response.status_code == 200
    assert b"Admin Report" in response.data
    _, parameters = matching_execution(connection.cursor_instance, "from items")
    assert parameters == (1,)


def test_one_user_cannot_see_another_users_my_reports(client, monkeypatch):
    authenticate_session(client, user_id=101, name="First User")
    first_connection = install_database(
        monkeypatch,
        fetchall_results=[[report_record(1, "First User Backpack", 101)]],
    )

    first_response = client.get("/my-reports")

    assert b"First User Backpack" in first_response.data
    assert b"Second User Bottle" not in first_response.data
    _, first_parameters = matching_execution(
        first_connection.cursor_instance,
        "from items",
    )
    assert first_parameters == (101,)

    authenticate_session(client, user_id=202, name="Second User")
    second_connection = install_database(
        monkeypatch,
        fetchall_results=[[report_record(2, "Second User Bottle", 202)]],
    )

    second_response = client.get("/my-reports")

    assert b"Second User Bottle" in second_response.data
    assert b"First User Backpack" not in second_response.data
    _, second_parameters = matching_execution(
        second_connection.cursor_instance,
        "from items",
    )
    assert second_parameters == (202,)


# Read-only administrator dashboard


def dashboard_records():
    summary = {
        "total_items": 2,
        "total_lost_reports": 1,
        "total_found_reports": 1,
        "total_claims": 2,
        "pending_claims": 1,
    }
    item_rows = [
        {
            "id": 1,
            "item_name": "Registered Backpack",
            "report_type": "lost",
            "category": "Bag",
            "location": "Computer Lab",
            "report_date": date(2026, 7, 1),
            "status": "Open",
            "reporter_name": "First User",
        },
        {
            "id": 2,
            "item_name": "Legacy Umbrella",
            "report_type": "found",
            "category": "Other",
            "location": "Library",
            "report_date": date(2026, 7, 2),
            "status": "Unclaimed",
            "reporter_name": None,
        },
    ]
    claim_rows = [
        {
            "id": 10,
            "item_name": "Registered Backpack",
            "claimant_name": "Claimant One",
            "claimant_contact": "claimant@example.com",
            "verification_details": "Notebook initials are ZT.",
            "status": "pending",
            "registered_account_name": "First User",
            "account_name": "First User",
            "claimant_account_name": "First User",
            "created_at": datetime(2026, 7, 3, 10, 0),
        },
        {
            "id": 11,
            "item_name": "Legacy Umbrella",
            "claimant_name": "Legacy Claimant",
            "claimant_contact": "legacy@example.com",
            "verification_details": "The handle has a silver mark.",
            "status": "reviewed",
            "registered_account_name": None,
            "account_name": None,
            "claimant_account_name": None,
            "created_at": datetime(2026, 7, 4, 10, 0),
        },
    ]
    return summary, item_rows, claim_rows


def install_admin_database(monkeypatch):
    summary, item_rows, claim_rows = dashboard_records()
    return install_database(
        monkeypatch,
        fetchone_results=[summary],
        fetchall_results=[item_rows, claim_rows],
    )


def assert_admin_join_queries(connection):
    normalized_queries = [
        normalize_sql(query).lower()
        for query, _ in connection.cursor_instance.executed
    ]
    item_queries = [
        query
        for query in normalized_queries
        if "from items" in query and "count(" not in query
    ]
    claim_queries = [
        query
        for query in normalized_queries
        if "from claims" in query and "count(" not in query
    ]
    assert item_queries
    assert claim_queries
    assert any("left join users" in query for query in item_queries)
    assert any("left join users" in query for query in claim_queries)


def test_administrator_dashboard_displays_summary_and_all_items(
    client,
    monkeypatch,
):
    authenticate_session(client, user_id=1, name="Site Admin", role="admin")
    connection = install_admin_database(monkeypatch)

    response = client.get("/admin")

    assert response.status_code == 200
    text = visible_text(response).lower()
    expected_counts = {
        "total items": 2,
        "total lost reports": 1,
        "total found reports": 1,
        "total claims": 2,
        "pending claims": 1,
    }
    for label, count in expected_counts.items():
        assert re.search(rf"{re.escape(label)}\s+{count}\b", text)
    assert "registered backpack" in text
    assert "legacy umbrella" in text
    assert "first user" in text
    assert "anonymous / legacy record" in text
    assert any(
        "count(" in normalize_sql(query).lower()
        for query, _ in connection.cursor_instance.executed
    )
    count_query = next(
        (query, parameters)
        for query, parameters in connection.cursor_instance.executed
        if "count(" in normalize_sql(query).lower()
    )
    assert count_query[1] == ("lost", "found", "pending")
    assert_admin_join_queries(connection)
    assert connection.cursor_instance.closed is True
    assert connection.closed is True


def test_administrator_dashboard_displays_registered_and_legacy_claims(
    client,
    monkeypatch,
):
    authenticate_session(client, user_id=1, name="Site Admin", role="admin")
    connection = install_admin_database(monkeypatch)

    response = client.get("/admin")

    assert response.status_code == 200
    text = visible_text(response).lower()
    assert "claimant one" in text
    assert "claimant@example.com" in text
    assert "notebook initials are zt" in text
    assert "legacy claimant" in text
    assert "the handle has a silver mark" in text
    assert "anonymous / legacy claim" in text
    assert_admin_join_queries(connection)


def test_administrator_dashboard_is_read_only(client, monkeypatch):
    authenticate_session(client, user_id=1, name="Site Admin", role="admin")
    connection = install_admin_database(monkeypatch)

    response = client.get("/admin")

    assert response.status_code == 200
    assert connection.committed is False
    assert all(
        normalize_sql(query).lower().startswith("select")
        for query, _ in connection.cursor_instance.executed
    )


def test_administrator_dashboard_does_not_accept_state_changing_post(client):
    authenticate_session(client, user_id=1, name="Site Admin", role="admin")

    response = client.post("/admin", data={"status": "approved"})

    assert response.status_code == 405
