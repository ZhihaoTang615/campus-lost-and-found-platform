from unittest.mock import MagicMock, patch

import app as app_module


def sample_found_item():
    """Return controlled found-item data for claim-request tests."""
    return {
        "id": 1,
        "item_name": "Student ID Card",
        "category": "student-card",
        "report_type": "found",
        "location": "Cafeteria",
        "report_date": "2026-07-12",
        "description": "Student ID card found near the west entrance.",
        "contact_information": "owner@example.com",
        "status": "active",
        "image_path": None,
    }


def test_claim_request_stores_pending_claim_with_mock_database(client):
    """
    Verify that a submitted claim is stored using a mocked database.

    The test checks that:
    - The selected item is loaded.
    - A new claim is inserted into the claims table.
    - The initial claim status is pending.
    - The transaction is committed.
    - Database resources are closed.
    """

    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = sample_found_item()

    mock_connection = MagicMock()
    mock_connection.cursor.return_value = mock_cursor
    mock_connection.is_connected.return_value = True

    with patch.object(
        app_module,
        "get_database_connection",
        return_value=mock_connection,
    ):
        response = client.post(
            "/claim-request/1",
            data={
                "name": "Zhihao Tang",
                "contact": "zhihao@example.com",
                "message": "The card contains my student number.",
            },
            follow_redirects=False,
        )

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/claim-success/1")

    success_response = client.get(response.headers["Location"])

    assert success_response.status_code == 200
    assert b"zhihao@example.com" not in success_response.data
    assert (
        b"The card contains my student number."
        not in success_response.data
    )

    # First execute: load the selected item.
    # Second execute: insert the submitted claim.
    assert mock_cursor.execute.call_count == 2

    insert_call = mock_cursor.execute.call_args_list[1]
    insert_query = " ".join(insert_call.args[0].split())
    insert_parameters = insert_call.args[1]

    assert "INSERT INTO claims" in insert_query
    assert insert_parameters == (
        1,
        "Zhihao Tang",
        "zhihao@example.com",
        "The card contains my student number.",
        "pending",
    )

    mock_connection.commit.assert_called_once()
    mock_cursor.close.assert_called_once()
    mock_connection.close.assert_called_once()


def test_claim_success_page_loads_with_confirmation(client):
    """Display a dedicated confirmation without private claim details."""
    response = client.get("/claim-success/1")

    assert response.status_code == 200
    assert b"Claim Request Submitted" in response.data
    assert b"successfully recorded" in response.data
    assert b"Current status:" in response.data
    assert b"Pending" in response.data
    assert b"View Item Details" in response.data
    assert b'href="/items/1"' in response.data
    assert b"Browse More Items" in response.data
    assert b'href="/items"' in response.data


def test_empty_claim_request_is_rejected(client):
    """US07 bug regression: empty claim fields must not be stored."""

    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = sample_found_item()

    mock_connection = MagicMock()
    mock_connection.cursor.return_value = mock_cursor
    mock_connection.is_connected.return_value = True

    with patch.object(
        app_module,
        "get_database_connection",
        return_value=mock_connection,
    ):
        response = client.post(
            "/claim-request/1",
            data={
                "name": "",
                "contact": "",
                "message": "",
            },
            follow_redirects=False,
        )

    assert response.status_code == 200
    assert b"All claim fields are required." in response.data

    # Only the SELECT for loading the item should run.
    # No INSERT should happen for an invalid claim.
    assert mock_cursor.execute.call_count == 1
    mock_connection.commit.assert_not_called()


def test_claim_request_for_missing_item_returns_404(client, fake_db):
    """Reject a claim request when its item ID does not exist."""
    connection = fake_db(row=None)

    response = client.get("/claim-request/999")

    assert response.status_code == 404
    assert b"Item not found." in response.data
    assert len(connection.cursor_instance.executed) == 1

    query, parameters = connection.cursor_instance.executed[0]

    assert "SELECT * FROM items WHERE id = %s" in query
    assert parameters == (999,)
    assert connection.committed is False
    assert connection.cursor_instance.closed is True
    assert connection.closed is True
