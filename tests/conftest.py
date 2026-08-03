from pathlib import Path

import pytest

import app as app_module


class FakeCursor:
    """A small fake MySQL cursor used by automated tests."""

    def __init__(self, rows=None, row=None):
        self.rows = rows or []
        self.row = row
        self.executed = []
        self.dictionary = False
        self.closed = False

    def execute(self, query, parameters=None):
        self.executed.append((query, parameters))

    def fetchall(self):
        return list(self.rows)

    def fetchone(self):
        return self.row

    def close(self):
        self.closed = True


class FakeConnection:
    """A small fake MySQL connection used by automated tests."""

    def __init__(self, rows=None, row=None):
        self.cursor_instance = FakeCursor(rows=rows, row=row)
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


@pytest.fixture
def client(monkeypatch, tmp_path):
    """Create a Flask test client with a temporary upload folder."""

    upload_folder = tmp_path / "uploads"
    upload_folder.mkdir(parents=True, exist_ok=True)

    monkeypatch.setitem(app_module.app.config, "TESTING", True)
    monkeypatch.setitem(
        app_module.app.config,
        "SECRET_KEY",
        "week-7-test-secret-key",
    )
    monkeypatch.setitem(
        app_module.app.config,
        "UPLOAD_FOLDER",
        str(upload_folder),
    )

    with app_module.app.test_client() as test_client:
        yield test_client


@pytest.fixture
def authenticated_session(client):
    """Return a helper that installs trusted authentication session values."""

    def authenticate(
        user_id=42,
        user_name="Test User",
        user_role="user",
    ):
        with client.session_transaction() as flask_session:
            flask_session.clear()
            flask_session["user_id"] = user_id
            flask_session["user_name"] = user_name
            flask_session["user_role"] = user_role

        return client

    return authenticate


@pytest.fixture
def authenticated_client(authenticated_session):
    """Provide a normal signed-in user for the original US01-US07 tests."""

    return authenticated_session()


@pytest.fixture
def administrator_client(authenticated_session):
    """Provide a signed-in administrator for access-control tests."""

    return authenticated_session(
        user_id=1,
        user_name="Site Admin",
        user_role="admin",
    )


@pytest.fixture
def fake_db(monkeypatch):
    """Replace the real database connection with a fake connection."""

    def install_fake_database(rows=None, row=None):
        connection = FakeConnection(rows=rows, row=row)

        monkeypatch.setattr(
            app_module,
            "get_database_connection",
            lambda: connection,
        )

        return connection

    return install_fake_database
