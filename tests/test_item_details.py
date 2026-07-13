"""Automated tests for US05 - View Item Details."""

import app as app_module
import pytest


class FakeCursor:
    """A fake database cursor used during automated testing."""

    def __init__(self, item):
        self.item = item
        self.executed_query = None
        self.executed_parameters = None
        self.closed = False

    def execute(self, query, parameters):
        self.executed_query = query
        self.executed_parameters = parameters

    def fetchone(self):
        return self.item

    def close(self):
        self.closed = True


class FakeConnection:
    """A fake database connection that avoids using the real MySQL database."""

    def __init__(self, item):
        self.fake_cursor = FakeCursor(item)
        self.closed = False

    def cursor(self, dictionary=False):
        assert dictionary is True
        return self.fake_cursor

    def is_connected(self):
        return not self.closed

    def close(self):
        self.closed = True


@pytest.fixture
def client():
    """Create a Flask test client."""
    app_module.app.config.update(TESTING=True)

    with app_module.app.test_client() as test_client:
        yield test_client


@pytest.fixture
def sample_item():
    """Provide sample item data for the item details tests."""
    return {
        "id": 1,
        "item_name": "Black Backpack",
        "category": "Bag",
        "report_type": "Lost",
        "location": "JCU Library",
        "report_date": "2026-07-10",
        "description": "A black backpack with a laptop compartment.",
        "contact_information": "student@example.com",
        "status": "Open",
        "image_path": None,
    }


@pytest.fixture
def fake_database(monkeypatch, sample_item):
    """Replace the real database connection with a fake connection."""
    connection = FakeConnection(sample_item)

    monkeypatch.setattr(
        app_module,
        "get_database_connection",
        lambda: connection,
    )

    return connection


def test_item_details_redirects_to_item_list(client):
    """US05-TC01: The old item details route redirects to the item list."""
    response = client.get("/item-details", follow_redirects=False)

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/items")


def test_dynamic_item_details_route_loads(client, fake_database):
    """US05-TC02: A valid dynamic item details page loads successfully."""
    response = client.get("/items/1")

    assert response.status_code == 200
    assert fake_database.fake_cursor.executed_parameters == (1,)


def test_item_details_page_displays_item_information(client, fake_database):
    """US05-TC03: The page displays important information about the item."""
    response = client.get("/items/1")

    page_content = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "Black Backpack" in page_content
    assert "Bag" in page_content
    assert "JCU Library" in page_content