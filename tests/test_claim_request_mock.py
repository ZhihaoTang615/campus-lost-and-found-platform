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
    assert response.headers["Location"].endswith("/items/1")

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