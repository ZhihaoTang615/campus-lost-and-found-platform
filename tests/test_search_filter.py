from datetime import date


def sample_items():
    return [
        {
            "id": 1,
            "item_name": "Blue Water Bottle",
            "category": "Bottle",
            "report_type": "found",
            "location": "Library Entrance",
            "report_date": date(2026, 7, 10),
            "status": "Unclaimed",
        },
        {
            "id": 2,
            "item_name": "Black Backpack",
            "category": "Bag",
            "report_type": "lost",
            "location": "Computer Lab",
            "report_date": date(2026, 7, 11),
            "status": "Open",
        },
    ]


def normalize_query(query):
    """Remove repeated whitespace to make SQL assertions easier."""

    return " ".join(query.split())


# =========================================================
# US03 – Search Items
# =========================================================

def test_browse_items_page_loads(authenticated_client, fake_db):
    """TC07: The Browse Items page should load successfully."""

    fake_db(rows=sample_items())

    response = authenticated_client.get("/items")

    assert response.status_code == 200
    assert b"Blue Water Bottle" in response.data
    assert b"Black Backpack" in response.data


def test_search_uses_keyword_for_name_description_and_location(
    authenticated_client,
    fake_db,
):
    """TC08: A search keyword should check three item fields."""

    connection = fake_db(rows=[sample_items()[0]])

    response = authenticated_client.get("/items?q=bottle")

    assert response.status_code == 200

    query, parameters = connection.cursor_instance.executed[0]
    query = normalize_query(query)

    assert "item_name LIKE %s" in query
    assert "description LIKE %s" in query
    assert "location LIKE %s" in query

    assert parameters == (
        "%bottle%",
        "%bottle%",
        "%bottle%",
    )


def test_search_with_no_matching_result_is_handled(authenticated_client, fake_db):
    """TC09: A search with no match should not crash the system."""

    connection = fake_db(rows=[])

    response = authenticated_client.get("/items?q=no-such-item-xyz")

    assert response.status_code == 200

    _, parameters = connection.cursor_instance.executed[0]

    assert parameters == (
        "%no-such-item-xyz%",
        "%no-such-item-xyz%",
        "%no-such-item-xyz%",
    )


# =========================================================
# US04 – Filter Items
# =========================================================

def test_filter_items_by_report_type(authenticated_client, fake_db):
    """TC10: Users should be able to filter found items."""

    connection = fake_db(rows=[sample_items()[0]])

    response = authenticated_client.get("/items?report_type=found")

    assert response.status_code == 200

    query, parameters = connection.cursor_instance.executed[0]
    query = normalize_query(query)

    assert "report_type = %s" in query
    assert parameters == ("found",)


def test_filter_items_by_category(authenticated_client, fake_db):
    """TC11: Users should be able to filter by category."""

    connection = fake_db(rows=[sample_items()[1]])

    response = authenticated_client.get("/items?category=Bag")

    assert response.status_code == 200

    query, parameters = connection.cursor_instance.executed[0]
    query = normalize_query(query)

    assert "category = %s" in query
    assert parameters == ("Bag",)


def test_combined_search_and_filters(authenticated_client, fake_db):
    """TC12: Search, report type, and category should work together."""

    connection = fake_db(rows=[sample_items()[0]])

    response = authenticated_client.get(
        "/items?q=water"
        "&report_type=found"
        "&category=Bottle"
    )

    assert response.status_code == 200

    query, parameters = connection.cursor_instance.executed[0]
    query = normalize_query(query)

    assert "item_name LIKE %s" in query
    assert "report_type = %s" in query
    assert "category = %s" in query
    assert " AND " in query

    assert parameters == (
        "%water%",
        "%water%",
        "%water%",
        "found",
        "Bottle",
    )
