# Week 7 Test Cases

## Context

This document records the Week 7 testing discussion, plan, test cases, automated testing implementation, and results for the Campus Lost and Found Platform.

Practical 7 focuses on Test-driven Development. Based on Chapter 7, testing should examine the system from different perspectives, including black-box testing, grey-box testing, and white-box testing.

The team selected the following five user stories:

- US01 - Report Lost Item
- US02 - Report Found Item
- US03 - Search Items
- US04 - Filter Items
- US05 - View Item Details

Three test cases were designed and automated for each selected user story. Therefore, the project includes a total of 15 documented test cases and 15 automated pytest tests.

---

## 1. Testing Approach

| Testing Type      | Meaning                                                                                                     | Application in This Project                                                                                                             |
| ----------------- | ----------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Black-box testing | Tests the visible system behaviour from the user's point of view without relying on internal code knowledge | Check whether pages load, forms can be submitted, search and filters work, redirects occur, and correct error responses are displayed   |
| Grey-box testing  | Tests visible behaviour while examining some internal data or system operations                             | Check SQL queries, query parameters, database commits, uploaded image paths, and stored report types                                    |
| White-box testing | Tests internal code logic, conditions, branches, and error handling                                         | Check Flask routes, valid and invalid file branches, search and filter conditions, redirects, existing items, and missing-item handling |

The test suite includes successful operations, invalid input, empty results, redirects, database behaviour, file upload behaviour, and error handling.

---

## 2. Test Environment

The automated testing environment uses:

- Python
- Flask test client
- pytest
- Fake database connections
- Fake database cursors
- Temporary upload directories
- Controlled sample data

The fake database prevents automated tests from changing the real MySQL database.

The temporary upload directory prevents test image files from being saved in the real `static/uploads` folder.

The test files are organised as follows:

```text
tests/
├── conftest.py
├── test_report_items.py
├── test_search_filter.py
└── test_item_details.py
```

### File Responsibilities

| File                    | Responsibility                                                                                                      |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `conftest.py`           | Provides the Flask test client, fake database connection, fake cursor, temporary upload folder, and shared fixtures |
| `test_report_items.py`  | Contains tests for US01 - Report Lost Item and US02 - Report Found Item                                             |
| `test_search_filter.py` | Contains tests for US03 - Search Items and US04 - Filter Items                                                      |
| `test_item_details.py`  | Contains tests for US05 - View Item Details                                                                         |

---

# 3. US01 - Report Lost Item

## TC01 - Open Report Lost Item Page

| Field           | Details                                                                                                          |
| --------------- | ---------------------------------------------------------------------------------------------------------------- |
| Test Case ID    | TC01                                                                                                             |
| User Story      | US01 - Report Lost Item                                                                                          |
| Test Type       | Black-box                                                                                                        |
| Objective       | Confirm that the Report Lost Item page loads successfully                                                        |
| Preconditions   | The Flask application and test client are available                                                              |
| Input           | GET request to `/report-lost-item`                                                                               |
| Steps           | 1. Open `/report-lost-item`.<br>2. Check the HTTP response status.<br>3. Check whether the page contains a form. |
| Expected Result | The page returns HTTP status 200 and displays the lost-item report form.                                         |
| Actual Result   | The page returned HTTP status 200 and the report form was displayed.                                             |
| Status          | Pass                                                                                                             |
| Automated Test  | `test_report_lost_item_page_loads`                                                                               |

---

## TC02 - Submit a Valid Lost Item Report

| Field           | Details                                                                                                                                                                                                  |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Test Case ID    | TC02                                                                                                                                                                                                     |
| User Story      | US01 - Report Lost Item                                                                                                                                                                                  |
| Test Type       | Black-box / Grey-box                                                                                                                                                                                     |
| Objective       | Confirm that a valid lost-item report can be processed and stored                                                                                                                                        |
| Preconditions   | The Flask test client and fake database connection are available                                                                                                                                         |
| Input           | Item Name: Black Backpack<br>Category: Bag<br>Location: Computer Lab<br>Date Lost: 2026-07-13<br>Description: Black backpack with notebooks inside.<br>Contact: zhihao@example.com                       |
| Steps           | 1. Enter all required lost-item information.<br>2. Submit the form.<br>3. Check the redirect response.<br>4. Check the database query and parameters.<br>5. Check whether the transaction was committed. |
| Expected Result | The system redirects to `/report-lost-item`, inserts the correct information, records the report type as `lost`, and commits the transaction.                                                            |
| Actual Result   | The correct parameters were inserted into the fake database and the transaction was committed.                                                                                                           |
| Status          | Pass                                                                                                                                                                                                     |
| Automated Test  | `test_valid_lost_item_report_is_saved`                                                                                                                                                                   |

---

## TC03 - Reject an Invalid Lost Item Photo

| Field           | Details                                                                                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Test Case ID    | TC03                                                                                                                                                                |
| User Story      | US01 - Report Lost Item                                                                                                                                             |
| Test Type       | Black-box / White-box                                                                                                                                               |
| Objective       | Confirm that the system rejects an unsupported uploaded file type                                                                                                   |
| Preconditions   | The Report Lost Item form is available                                                                                                                              |
| Input           | Completed lost-item form with the file `malicious-file.exe`                                                                                                         |
| Steps           | 1. Complete the required lost-item fields.<br>2. Attach `malicious-file.exe` as the item photo.<br>3. Submit the form.<br>4. Check the response and flash messages. |
| Expected Result | The system rejects the file, displays an invalid image file type message, displays an unsuccessful submission message, and does not crash.                          |
| Actual Result   | The invalid file was rejected and the correct messages were displayed.                                                                                              |
| Status          | Pass                                                                                                                                                                |
| Automated Test  | `test_lost_item_rejects_invalid_photo_type`                                                                                                                         |

---

# 4. US02 - Report Found Item

## TC04 - Open Report Found Item Page

| Field           | Details                                                                                                           |
| --------------- | ----------------------------------------------------------------------------------------------------------------- |
| Test Case ID    | TC04                                                                                                              |
| User Story      | US02 - Report Found Item                                                                                          |
| Test Type       | Black-box                                                                                                         |
| Objective       | Confirm that the Report Found Item page loads successfully                                                        |
| Preconditions   | The Flask application and test client are available                                                               |
| Input           | GET request to `/report-found-item`                                                                               |
| Steps           | 1. Open `/report-found-item`.<br>2. Check the HTTP response status.<br>3. Check whether the page contains a form. |
| Expected Result | The page returns HTTP status 200 and displays the found-item report form.                                         |
| Actual Result   | The page returned HTTP status 200 and the report form was displayed.                                              |
| Status          | Pass                                                                                                              |
| Automated Test  | `test_report_found_item_page_loads`                                                                               |

---

## TC05 - Submit a Valid Found Item Report

| Field           | Details                                                                                                                                                                                                   |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Test Case ID    | TC05                                                                                                                                                                                                      |
| User Story      | US02 - Report Found Item                                                                                                                                                                                  |
| Test Type       | Black-box / Grey-box                                                                                                                                                                                      |
| Objective       | Confirm that a valid found-item report can be processed and stored                                                                                                                                        |
| Preconditions   | The Flask test client and fake database connection are available                                                                                                                                          |
| Input           | Item Name: Blue Water Bottle<br>Category: Bottle<br>Location: Library Entrance<br>Date Found: 2026-07-13<br>Description: Blue bottle found near the library.<br>Contact: zhihao@example.com               |
| Steps           | 1. Enter all required found-item information.<br>2. Submit the form.<br>3. Check the redirect response.<br>4. Check the database query and parameters.<br>5. Check whether the transaction was committed. |
| Expected Result | The system redirects to `/report-found-item`, stores the correct information, records the report type as `found`, and commits the transaction.                                                            |
| Actual Result   | The found-item information was inserted correctly and the transaction was committed.                                                                                                                      |
| Status          | Pass                                                                                                                                                                                                      |
| Automated Test  | `test_valid_found_item_report_is_saved`                                                                                                                                                                   |

---

## TC06 - Submit a Found Item Report with a Valid Photo

| Field           | Details                                                                                                                                                                                |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Test Case ID    | TC06                                                                                                                                                                                   |
| User Story      | US02 - Report Found Item                                                                                                                                                               |
| Test Type       | Black-box / Grey-box                                                                                                                                                                   |
| Objective       | Confirm that a valid image can be uploaded with a found-item report                                                                                                                    |
| Preconditions   | A temporary upload folder and fake database connection are available                                                                                                                   |
| Input           | Valid found-item data and an image named `test photo.jpg`                                                                                                                              |
| Steps           | 1. Complete the found-item form.<br>2. Attach the JPG image.<br>3. Submit the form.<br>4. Check the temporary upload directory.<br>5. Check the image path in the database parameters. |
| Expected Result | The system saves the file as `test_photo.jpg`, stores the path `uploads/test_photo.jpg`, and commits the transaction.                                                                  |
| Actual Result   | The image was saved in the temporary upload directory and the correct image path was stored.                                                                                           |
| Status          | Pass                                                                                                                                                                                   |
| Automated Test  | `test_found_item_report_saves_valid_photo`                                                                                                                                             |

---

# 5. US03 - Search Items

## TC07 - Open the Browse Items Page

| Field           | Details                                                                                                           |
| --------------- | ----------------------------------------------------------------------------------------------------------------- |
| Test Case ID    | TC07                                                                                                              |
| User Story      | US03 - Search Items                                                                                               |
| Test Type       | Black-box                                                                                                         |
| Objective       | Confirm that the Browse Items page loads and displays available records                                           |
| Preconditions   | The fake database contains sample item records                                                                    |
| Input           | Blue Water Bottle and Black Backpack sample records                                                               |
| Steps           | 1. Open `/items`.<br>2. Check the HTTP response status.<br>3. Check whether both sample item names are displayed. |
| Expected Result | The page returns HTTP status 200 and displays both sample items.                                                  |
| Actual Result   | The Browse Items page loaded and displayed both sample items.                                                     |
| Status          | Pass                                                                                                              |
| Automated Test  | `test_browse_items_page_loads`                                                                                    |

---

## TC08 - Search with a Matching Keyword

| Field           | Details                                                                                               |
| --------------- | ----------------------------------------------------------------------------------------------------- |
| Test Case ID    | TC08                                                                                                  |
| User Story      | US03 - Search Items                                                                                   |
| Test Type       | Grey-box / White-box                                                                                  |
| Objective       | Confirm that a search keyword is applied to the correct database fields                               |
| Preconditions   | The Browse Items route and fake database are available                                                |
| Input           | Search keyword: `bottle`                                                                              |
| Steps           | 1. Open `/items?q=bottle`.<br>2. Check the generated SQL query.<br>3. Check the SQL query parameters. |
| Expected Result | The SQL query searches `item_name`, `description`, and `location` using the parameter `%bottle%`.     |
| Actual Result   | All three fields were included in the SQL query and the correct parameters were used.                 |
| Status          | Pass                                                                                                  |
| Automated Test  | `test_search_uses_keyword_for_name_description_and_location`                                          |

---

## TC09 - Search with No Matching Results

| Field           | Details                                                                                                                                                         |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Test Case ID    | TC09                                                                                                                                                            |
| User Story      | US03 - Search Items                                                                                                                                             |
| Test Type       | Black-box / Grey-box                                                                                                                                            |
| Objective       | Confirm that a search with no matching items is handled safely                                                                                                  |
| Preconditions   | The fake database returns an empty result list                                                                                                                  |
| Input           | Search keyword: `no-such-item-xyz`                                                                                                                              |
| Steps           | 1. Open `/items?q=no-such-item-xyz`.<br>2. Check the HTTP response status.<br>3. Check the SQL query parameters.<br>4. Confirm that the request does not crash. |
| Expected Result | The page returns HTTP status 200 and handles the empty result without a server error.                                                                           |
| Actual Result   | The request returned HTTP status 200 and the empty result was handled correctly.                                                                                |
| Status          | Pass                                                                                                                                                            |
| Automated Test  | `test_search_with_no_matching_result_is_handled`                                                                                                                |

---

# 6. US04 - Filter Items

## TC10 - Filter Items by Report Type

| Field           | Details                                                                                                                                          |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Test Case ID    | TC10                                                                                                                                             |
| User Story      | US04 - Filter Items                                                                                                                              |
| Test Type       | Grey-box / White-box                                                                                                                             |
| Objective       | Confirm that users can filter items by report type                                                                                               |
| Preconditions   | The Browse Items route and fake database are available                                                                                           |
| Input           | Report Type: `found`                                                                                                                             |
| Steps           | 1. Open `/items?report_type=found`.<br>2. Check the HTTP response status.<br>3. Check the generated SQL query.<br>4. Check the query parameters. |
| Expected Result | The SQL query includes `report_type = %s` and uses `found` as the parameter.                                                                     |
| Actual Result   | The correct report type condition and parameter were generated.                                                                                  |
| Status          | Pass                                                                                                                                             |
| Automated Test  | `test_filter_items_by_report_type`                                                                                                               |

---

## TC11 - Filter Items by Category

| Field           | Details                                                                                                                                     |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Test Case ID    | TC11                                                                                                                                        |
| User Story      | US04 - Filter Items                                                                                                                         |
| Test Type       | Grey-box / White-box                                                                                                                        |
| Objective       | Confirm that users can filter items by category                                                                                             |
| Preconditions   | The Browse Items route and fake database are available                                                                                      |
| Input           | Category: `Bag`                                                                                                                             |
| Steps           | 1. Open `/items?category=Bag`.<br>2. Check the HTTP response status.<br>3. Check the generated SQL query.<br>4. Check the query parameters. |
| Expected Result | The SQL query includes `category = %s` and uses `Bag` as the parameter.                                                                     |
| Actual Result   | The correct category condition and parameter were generated.                                                                                |
| Status          | Pass                                                                                                                                        |
| Automated Test  | `test_filter_items_by_category`                                                                                                             |

---

## TC12 - Combine Search and Filters

| Field           | Details                                                                                                                                                                                          |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Test Case ID    | TC12                                                                                                                                                                                             |
| User Story      | US04 - Filter Items                                                                                                                                                                              |
| Test Type       | Grey-box / White-box                                                                                                                                                                             |
| Objective       | Confirm that search, report type, and category filters work together                                                                                                                             |
| Preconditions   | The Browse Items route and fake database are available                                                                                                                                           |
| Input           | Keyword: `water`<br>Report Type: `found`<br>Category: `Bottle`                                                                                                                                   |
| Steps           | 1. Open `/items?q=water&report_type=found&category=Bottle`.<br>2. Check the generated SQL query.<br>3. Confirm that the conditions are joined using `AND`.<br>4. Check all SQL query parameters. |
| Expected Result | The SQL query combines the keyword search, report type, and category conditions using `AND` and passes the correct parameters.                                                                   |
| Actual Result   | All three conditions were combined correctly and the expected parameters were used.                                                                                                              |
| Status          | Pass                                                                                                                                                                                             |
| Automated Test  | `test_combined_search_and_filters`                                                                                                                                                               |

---

# 7. US05 - View Item Details

## TC13 - Redirect the General Item Details Route

| Field           | Details                                                                                           |
| --------------- | ------------------------------------------------------------------------------------------------- |
| Test Case ID    | TC13                                                                                              |
| User Story      | US05 - View Item Details                                                                          |
| Test Type       | Black-box                                                                                         |
| Objective       | Confirm that the general Item Details route redirects users to Browse Items                       |
| Preconditions   | The Flask application and test client are available                                               |
| Input           | GET request to `/item-details`                                                                    |
| Steps           | 1. Open `/item-details`.<br>2. Check the HTTP response status.<br>3. Check the redirect location. |
| Expected Result | The route returns HTTP status 302 and redirects the user to `/items`.                             |
| Actual Result   | The route returned HTTP status 302 and redirected to the Browse Items page.                       |
| Status          | Pass                                                                                              |
| Automated Test  | `test_item_details_entry_route_redirects_to_items`                                                |

---

## TC14 - Display an Existing Item

| Field           | Details                                                                                                                                             |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Test Case ID    | TC14                                                                                                                                                |
| User Story      | US05 - View Item Details                                                                                                                            |
| Test Type       | Black-box / Grey-box                                                                                                                                |
| Objective       | Confirm that an existing item record is displayed correctly                                                                                         |
| Preconditions   | The fake database contains an item with ID 1                                                                                                        |
| Input           | Item ID: 1<br>Item Name: Student ID Card<br>Location: Cafeteria                                                                                     |
| Steps           | 1. Open `/items/1`.<br>2. Check the HTTP response status.<br>3. Check the visible item name and location.<br>4. Check the database query parameter. |
| Expected Result | The page returns HTTP status 200, displays the selected item details, and queries item ID 1.                                                        |
| Actual Result   | The item name and location were displayed and the database query used item ID 1.                                                                    |
| Status          | Pass                                                                                                                                                |
| Automated Test  | `test_existing_item_details_are_displayed`                                                                                                          |

---

## TC15 - Handle a Missing Item

| Field           | Details                                                                                                                                 |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Test Case ID    | TC15                                                                                                                                    |
| User Story      | US05 - View Item Details                                                                                                                |
| Test Type       | Black-box / White-box                                                                                                                   |
| Objective       | Confirm that an unknown item ID is handled correctly                                                                                    |
| Preconditions   | The fake database returns no matching record                                                                                            |
| Input           | Item ID: 999                                                                                                                            |
| Steps           | 1. Open `/items/999`.<br>2. Check the HTTP response status.<br>3. Check the response message.<br>4. Check the database query parameter. |
| Expected Result | The system returns HTTP status 404 and displays `Item not found.`                                                                       |
| Actual Result   | The route returned a handled 404 response and displayed the correct message.                                                            |
| Status          | Pass                                                                                                                                    |
| Automated Test  | `test_missing_item_returns_404`                                                                                                         |

---

## 8. Automated Testing Implementation

The project uses Python `pytest` and the Flask test client to implement the automated tests.

The automated test suite checks:

- Lost-item report page loading
- Valid lost-item report submission
- Invalid lost-item photo rejection
- Found-item report page loading
- Valid found-item report submission
- Valid found-item photo upload
- Browse Items page loading
- Matching keyword searches
- Searches with no matching results
- Report type filtering
- Category filtering
- Combined search and filtering
- General Item Details route redirection
- Existing item details
- Missing item handling with HTTP 404

The tests are executed using:

```bash
python -m pytest -v
```

The final result was:

```text
15 passed
```

Testing evidence is stored at:

```text
docs/testing/images/week-7-pytest-15-passed.png
```

---

## 9. Defects Found During Testing

### 9.1 Incorrect Claim Request Endpoint

The Item Details template originally used an incorrect Flask endpoint:

```text
claim
```

The correct Flask endpoint was:

```text
claim_request
```

This error prevented the Item Details page from loading correctly. The endpoint was corrected and the test suite was run again.

### 9.2 Browse Items Template Syntax Error

A Jinja condition in `templates/items.html` was incorrectly formatted. This caused the Browse Items page and all related search and filter tests to fail.

The Jinja condition was corrected, and the automated test suite was run again successfully.

These defects show that automated testing can identify regression errors after code and template changes.

---

## 10. Test Case Summary

| User Story               | Test Cases | Automated Tests | Result        |
| ------------------------ | ---------: | --------------: | ------------- |
| US01 - Report Lost Item  |  TC01-TC03 |               3 | Passed        |
| US02 - Report Found Item |  TC04-TC06 |               3 | Passed        |
| US03 - Search Items      |  TC07-TC09 |               3 | Passed        |
| US04 - Filter Items      |  TC10-TC12 |               3 | Passed        |
| US05 - View Item Details |  TC13-TC15 |               3 | Passed        |
| **Total**                |     **15** |          **15** | **15 Passed** |

---

## 11. Limitations

The current automated test suite covers five selected user stories and their main Flask route, database, search, filter, upload, redirect, and error-handling behaviours.

However, the tests use fake database connections instead of a real MySQL testing database. Therefore, the suite does not verify the complete connection between Flask and a real MySQL server.

The current tests also do not fully cover the Claim Request workflow.

Future testing should include:

- US06 - Upload Item Photo as a separate user story
- US07 - Submit Claim Request
- Real MySQL integration testing
- Claim request database storage
- Browser-based end-to-end testing
- File size validation
- Duplicate filename handling
- Security testing
- SQL injection testing
- Cross-site scripting testing
- Automated test coverage reporting
- GitHub Actions continuous integration

---

## Summary

This Week 7 testing document applies black-box, grey-box, and white-box testing concepts to the Campus Lost and Found Platform.

The team selected five user stories and designed three test cases for each user story. A total of 15 test cases were documented and implemented using pytest.

The automated tests use fake database connections and temporary upload directories to avoid changing the real database and project files.

All 15 automated tests passed successfully. Therefore, the project satisfies the Practical 7 requirements for selected user stories, documented test cases, and automated testing.
