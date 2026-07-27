# Python Mock Object Research

## 1. Purpose

This document records the mock-object framework selected for automated testing in the Campus Lost and Found Platform.

The project uses Flask, MySQL and pytest. Some application behaviour depends on external or stateful components such as the database connection. Mock objects allow these dependencies to be replaced during automated testing so that tests can run in a controlled and repeatable way.

The selected framework is Python's built-in `unittest.mock`.

---

## 2. What Is a Mock Object?

A mock object is a test double that replaces a real dependency during testing.

Instead of connecting to a real database or external component, a test can provide a controlled replacement that behaves in a predictable way.

Mocks are useful when the real dependency is:

- slow;
- difficult to configure;
- dependent on external state;
- capable of changing production data;
- unnecessary for the specific behaviour being tested.

In this Flask project, mock objects are particularly useful for testing database-dependent behaviour such as claim-request persistence without requiring a real MySQL database for every test run.

---

## 3. Fake vs Stub vs Mock

### Fake

A **fake** is a simplified working implementation of a real dependency.

For example, this project already contains `FakeConnection` and `FakeCursor` classes in `tests/conftest.py`.

They simulate parts of the MySQL connection and cursor behaviour, including:

- `execute()`;
- `fetchone()`;
- `fetchall()`;
- `commit()`;
- `close()`.

The fake database objects allow tests to inspect SQL calls without connecting to a real MySQL database.

### Stub

A **stub** returns predefined data required by a test.

For example, a test may replace the database query result with a predefined item record:

```python
item = {
    "id": 1,
    "item_name": "Student ID Card",
    "report_type": "found"
}
```
The purpose of the stub is mainly to provide controlled input to the code under test.

## Mock

A mock is a configurable test double that can also record how it was used.

A mock can verify:

whether a function was called;
how many times it was called;
which arguments were supplied;
whether database methods such as commit() were executed.

This makes mocks suitable for verifying interactions between the Flask application and its dependencies.

## 4. Why `unittest.mock` Was Selected

Python's unittest.mock was selected because it is included in the Python standard library and integrates well with pytest.

It is appropriate for this project because:

no additional mocking dependency is required;
it works with the existing pytest test suite;
it provides Mock and MagicMock;
it provides patch for replacing dependencies temporarily;
calls and arguments can be inspected;
it supports isolated testing of Flask routes and helper functions;
it is widely used in Python automated testing.

This allows the project to introduce mock-object testing without changing the application architecture or adding an unnecessary external library.


## 5. MagicMock

MagicMock is a flexible mock object provided by unittest.mock.

It can automatically create mock methods and record how those methods are called.

Example:from unittest.mock import MagicMock

connection = MagicMock()
cursor = MagicMock()

connection.cursor.return_value = cursor
The application can now interact with connection and cursor as if they were database objects.

The test can later verify behaviour such as:
cursor.execute.assert_called_once()
connection.commit.assert_called_once()
For US07, this can be used to confirm that a valid claim request causes an SQL insert and database commit.

## 6. patch

patch temporarily replaces an object during a test.

The replacement only exists for the duration of the test or patch context.

For this project, the most relevant dependency is:
get_database_connection()
A test can replace the real database connection with a mock connection:
from unittest.mock import MagicMock, patch

def test_database_connection_is_mocked():
    mock_connection = MagicMock()

    with patch(
        "app.get_database_connection",
        return_value=mock_connection
    ):
        connection = mock_connection

        assert connection is mock_connection
This prevents the test from opening a real MySQL connection.

It is important to patch the dependency where it is used. Because the Flask application accesses get_database_connection through the app module, the correct target is:
app.get_database_connection

## 7. Mock Database Example for US07

US07 requires a valid claim request to be stored with an initial pending status and linked to the correct item.

A simplified mock-based test could use:
from unittest.mock import MagicMock, patch

def test_claim_request_uses_pending_status(client):
    mock_connection = MagicMock()
    mock_cursor = MagicMock()

    mock_connection.cursor.return_value = mock_cursor

    mock_cursor.fetchone.return_value = {
        "id": 1,
        "item_name": "Student ID Card",
        "report_type": "found",
        "status": "available"
    }

    with patch(
        "app.get_database_connection",
        return_value=mock_connection
    ):
        response = client.post(
            "/claim-request/1",
            data={
                "name": "Test Student",
                "contact": "student@example.com",
                "message": "My name is written on the card."
            }
        )

    assert response.status_code == 302
    assert mock_connection.commit.called
The test could also inspect the SQL parameters passed to cursor.execute() to verify that:

the selected item_id is stored;
claimant information is stored;
verification details are stored;
the initial status is pending.

This verifies application behaviour without modifying a real claims table.

## 8. Mock Current-User Example

The current Campus Lost and Found Platform does not currently implement a logged-in user system.

Therefore, current-user mocking is not required by the implemented US01-US07 functionality.

However, if authentication were introduced later, a user dependency could be replaced during testing.

For example:
from unittest.mock import MagicMock

mock_user = MagicMock()

mock_user.id = 10
mock_user.name = "Test Student"
mock_user.is_authenticated = True
A route or authentication helper could then receive the mock user instead of relying on a real login session.

This example demonstrates the testing technique only. It does not indicate that current-user authentication is currently implemented in this project.

## 9. Relationship to Existing Test Doubles

The existing test suite already uses lightweight fake database objects.

tests/conftest.py defines:

FakeCursor;
FakeConnection;
fake_db.

The fixture replaces the real get_database_connection() function with a fake connection during testing.

This approach is useful for many current tests because it gives direct access to:

executed SQL;
supplied SQL parameters;
commit state;
returned rows.

unittest.mock complements this approach.

The project can therefore use:

fake objects where a small reusable database implementation is useful;
MagicMock where call verification is the main purpose;
patch when a dependency must be replaced temporarily.

The two approaches do not conflict and can be used together depending on the goal of each test.

## 10. Benefits

Using mock objects provides several benefits for this Flask project:

Isolation
Tests can focus on one function or route without depending on a live database.
Repeatability
The same predefined conditions can be reproduced every time the test runs.
Speed
Mock-based tests avoid unnecessary network and database operations.
Safety
Automated tests do not need to insert or modify real production data.
Interaction verification
Tests can verify whether functions such as execute() and commit() were called.
Error simulation
Mock objects can be configured to simulate unusual or failing conditions.
TDD support
Dependencies can be controlled while developing RED, GREEN and REFACTOR test cycles.

## 11. Limitations

Mock objects also have limitations.

Mocks do not prove that MySQL itself works

A mock can confirm that the application attempted to execute SQL, but it cannot prove that the SQL is compatible with the real database schema.

Real integration or system testing is still required.

Incorrect mocks can produce misleading tests

If a mock behaves differently from the real dependency, a test may pass even though the real application fails.

Excessive mocking can make tests difficult to understand

Tests should mock only dependencies that need isolation.

Implementation coupling

A test that checks too many internal calls can become tightly coupled to implementation details and may require unnecessary changes after refactoring.

For this reason, the project should combine:

unit/mock tests;
fake-database tests;
regression testing;
manual system testing.

## 12. US07 Mock Test Evidence

The Iteration 3 mock-object implementation is tracked by:

Issue #60 – Implement Python mock object test

The final link to Zhihao's actual US07 mock test must be added here after the implementation has been completed and merged into main.

Status: Pending Issue #60 completion.

Final evidence should include:

actual test file link;
relevant commit;
Pull Request link;
passing pytest result.

This placeholder must not be replaced with an invented link.

## 13. Conclusion

Python unittest.mock is suitable for the Campus Lost and Found Platform because it integrates with the existing pytest-based testing approach and allows Flask dependencies to be isolated without changing production code.

MagicMock can verify interactions, while patch can temporarily replace dependencies such as the database connection.

The framework complements the project's existing fake database fixtures and is particularly useful for testing US07 claim persistence in a controlled and repeatable way.
