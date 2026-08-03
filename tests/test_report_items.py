from io import BytesIO
from pathlib import Path

import app as app_module


def lost_item_data():
    return {
        "item-name": "Black Backpack",
        "category": "Bag",
        "location": "Computer Lab",
        "date-lost": "2026-07-13",
        "description": "Black backpack with notebooks inside.",
        "contact": "zhihao@example.com",
    }


def found_item_data():
    return {
        "item-name": "Blue Water Bottle",
        "category": "Bottle",
        "location": "Library Entrance",
        "date-found": "2026-07-13",
        "description": "Blue bottle found near the library.",
        "contact": "zhihao@example.com",
    }


# =========================================================
# US01 – Report Lost Item
# =========================================================

def test_report_lost_item_page_loads(authenticated_client):
    """TC01: The lost-item report page should load successfully."""

    response = authenticated_client.get("/report-lost-item")

    assert response.status_code == 200
    assert b"<form" in response.data.lower()


def test_valid_lost_item_report_is_saved(authenticated_client, fake_db):
    """TC02: A valid lost-item report should be stored."""

    connection = fake_db()

    response = authenticated_client.post(
        "/report-lost-item",
        data=lost_item_data(),
        follow_redirects=False,
    )

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/report-lost-item")
    assert connection.committed is True

    query, parameters = connection.cursor_instance.executed[0]

    assert "INSERT INTO items" in query
    assert parameters[0] == "Black Backpack"
    assert parameters[1] == "Bag"
    assert parameters[2] == "lost"
    assert parameters[3] == "Computer Lab"
    assert parameters[4] == "2026-07-13"
    assert parameters[7] is None
    assert parameters[8] == 42


def test_lost_item_rejects_invalid_photo_type(authenticated_client):
    """TC03: A non-image upload should be rejected."""

    form_data = lost_item_data()
    form_data["item-photo"] = (
        BytesIO(b"not an image"),
        "malicious-file.exe",
    )

    response = authenticated_client.post(
        "/report-lost-item",
        data=form_data,
        content_type="multipart/form-data",
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Invalid image file type" in response.data
    assert b"Unable to save the lost item report" in response.data


# =========================================================
# US02 – Report Found Item
# =========================================================

def test_report_found_item_page_loads(authenticated_client):
    """TC04: The found-item report page should load successfully."""

    response = authenticated_client.get("/report-found-item")

    assert response.status_code == 200
    assert b"<form" in response.data.lower()


def test_valid_found_item_report_is_saved(authenticated_client, fake_db):
    """TC05: A valid found-item report should be stored."""

    connection = fake_db()

    response = authenticated_client.post(
        "/report-found-item",
        data=found_item_data(),
        follow_redirects=False,
    )

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/report-found-item")
    assert connection.committed is True

    query, parameters = connection.cursor_instance.executed[0]

    assert "INSERT INTO items" in query
    assert parameters[0] == "Blue Water Bottle"
    assert parameters[1] == "Bottle"
    assert parameters[2] == "found"
    assert parameters[3] == "Library Entrance"
    assert parameters[4] == "2026-07-13"
    assert parameters[8] == 42


def test_found_item_report_saves_valid_photo(authenticated_client, fake_db):
    """TC06: A valid image should be saved with the found-item report."""

    connection = fake_db()

    form_data = found_item_data()
    form_data["item-photo"] = (
        BytesIO(b"fake image content"),
        "test photo.jpg",
    )

    response = authenticated_client.post(
        "/report-found-item",
        data=form_data,
        content_type="multipart/form-data",
        follow_redirects=False,
    )

    assert response.status_code == 302
    assert connection.committed is True

    saved_file = (
        Path(app_module.app.config["UPLOAD_FOLDER"])
        / "test_photo.jpg"
    )

    assert saved_file.exists()

    _, parameters = connection.cursor_instance.executed[0]

    assert parameters[2] == "found"
    assert parameters[7] == "uploads/test_photo.jpg"
    assert parameters[8] == 42
