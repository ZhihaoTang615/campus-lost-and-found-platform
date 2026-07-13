from datetime import date


def sample_item():
    return {
        "id": 1,
        "item_name": "Student ID Card",
        "category": "Card",
        "report_type": "found",
        "location": "Cafeteria",
        "report_date": date(2026, 7, 12),
        "description": "Student ID card found near the west entrance.",
        "contact_information": "zhihao@example.com",
        "status": "Unclaimed",
        "image_path": None,
    }


# =========================================================
# US05 – View Item Details
# =========================================================

def test_item_details_entry_route_redirects_to_items(client):
    """TC13: The general details route should redirect to Browse Items."""

    response = client.get(
        "/item-details",
        follow_redirects=False,
    )

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/items")


def test_existing_item_details_are_displayed(client, fake_db):
    """TC14: An existing item ID should display its information."""

    connection = fake_db(row=sample_item())

    response = client.get("/items/1")

    assert response.status_code == 200
    assert b"Student ID Card" in response.data
    assert b"Cafeteria" in response.data

    query, parameters = connection.cursor_instance.executed[0]

    assert "WHERE id = %s" in query
    assert parameters == (1,)


def test_missing_item_returns_404(client, fake_db):
    """TC15: An unknown item ID should return a handled 404 response."""

    connection = fake_db(row=None)

    response = client.get("/items/999")

    assert response.status_code == 404
    assert b"Item not found" in response.data

    _, parameters = connection.cursor_instance.executed[0]

    assert parameters == (999,)