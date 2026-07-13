# Week 7 Test Cases

## Context

This document records the Week 7 testing plan and test cases for the Campus Lost and Found Platform.

Practical 7 focuses on Test-driven Development. Based on Chapter 7, testing should check the system from different views: black-box testing, grey-box testing, and white-box testing. The project also needs automated tests so that important functionality can be checked repeatedly.

The selected user stories are:

- US01 - Report Lost Item
- US02 - Report Found Item
- US03 - Search Items
- US04 - Filter Items
- US05 - View Item Details

Each selected user story includes at least three test cases.

---

## 1. Testing Approach

| Testing Type | Meaning | Project Application |
|---|---|---|
| Black-box testing | Test from the user point of view without looking at the code | Check whether the web pages and forms behave correctly |
| Grey-box testing | Test from the user point of view while checking some internal data | Check stored item data, uploaded photo paths, and database-backed results |
| White-box testing | Test internal code logic | Check Flask routes, search logic, filter logic, form handling, and error handling |

---

## 2. US01 - Report Lost Item

### Test Case 1: Open Report Lost Item page

| Field | Details |
|---|---|
| Test Type | Black-box |
| Input | User opens the Report Lost Item page |
| Steps | Go to `/report-lost-item` |
| Expected Result | The page loads successfully and displays the lost item report form |

### Test Case 2: Submit valid lost item report

| Field | Details |
|---|---|
| Test Type | Black-box / Grey-box |
| Input | Valid item name, category, location, description, date, and contact information |
| Steps | Fill in the form and submit |
| Expected Result | The system accepts the lost item report and does not return a server error |

### Test Case 3: Submit missing required fields

| Field | Details |
|---|---|
| Test Type | Black-box |
| Input | Empty item name or missing required fields |
| Steps | Submit the form with incomplete data |
| Expected Result | The system should reject the incomplete report or handle it without crashing |

---

## 3. US02 - Report Found Item

### Test Case 1: Open Report Found Item page

| Field | Details |
|---|---|
| Test Type | Black-box |
| Input | User opens the Report Found Item page |
| Steps | Go to `/report-found-item` |
| Expected Result | The page loads successfully and displays the found item report form |

### Test Case 2: Submit valid found item report

| Field | Details |
|---|---|
| Test Type | Black-box / Grey-box |
| Input | Valid item details |
| Steps | Fill in the found item form and submit |
| Expected Result | The system accepts the found item report and does not return a server error |

### Test Case 3: Submit found item report with photo

| Field | Details |
|---|---|
| Test Type | Black-box / Grey-box |
| Input | Valid found item data and a valid image file |
| Steps | Attach a valid image and submit the form |
| Expected Result | The system accepts the report and stores or handles the uploaded photo |

---

## 4. US03 - Search Items

### Test Case 1: Open Browse Items page

| Field | Details |
|---|---|
| Test Type | Black-box |
| Input | User opens Browse Items page |
| Steps | Go to `/items` |
| Expected Result | The browse page loads successfully |

### Test Case 2: Search with matching keyword

| Field | Details |
|---|---|
| Test Type | Black-box |
| Input | Keyword such as `bottle` or `card` |
| Steps | Enter keyword into search field and submit |
| Expected Result | The system returns matching items or handles the search request without crashing |

### Test Case 3: Search with no matching keyword

| Field | Details |
|---|---|
| Test Type | Black-box |
| Input | A keyword that should not exist |
| Steps | Search for a random keyword |
| Expected Result | The system shows no results or an empty result state without crashing |

---

## 5. US04 - Filter Items

### Test Case 1: Filter by report type

| Field | Details |
|---|---|
| Test Type | Black-box |
| Input | Report type = Lost or Found |
| Steps | Apply report type filter |
| Expected Result | The system displays matching items or handles the filter request correctly |

### Test Case 2: Filter by category

| Field | Details |
|---|---|
| Test Type | Black-box |
| Input | Category such as Card, Bag, Bottle, or Electronics |
| Steps | Apply category filter |
| Expected Result | The system displays items from the selected category or handles the request correctly |

### Test Case 3: Combine search and filter

| Field | Details |
|---|---|
| Test Type | Black-box |
| Input | Keyword + report type + category |
| Steps | Apply search and filter together |
| Expected Result | The system returns results matching all selected conditions or shows no results without crashing |

---

## 6. US05 - View Item Details

### Test Case 1: Open static item details page

| Field | Details |
|---|---|
| Test Type | Black-box |
| Input | User opens `/item-details` |
| Steps | Go to the item details page |
| Expected Result | The page loads successfully |

### Test Case 2: Open dynamic item details page

| Field | Details |
|---|---|
| Test Type | Black-box / Grey-box |
| Input | A specific item ID, such as `/items/1` |
| Steps | Open the dynamic item details page |
| Expected Result | The system displays item details or returns a handled not-found page without crashing |

### Test Case 3: Check item details content

| Field | Details |
|---|---|
| Test Type | Black-box |
| Input | Item details page |
| Steps | Open the item details page and check visible fields |
| Expected Result | Item name, category, location, description, status, or related item information should be displayed |

---

## 7. Automated Testing Plan

The project will use Python `pytest` for automated testing. The first automated test suite focuses on Flask route testing and basic functional checks.

The automated tests will check:

- Page loading
- Important page content
- Search request handling
- Filter request handling
- Report form GET requests
- Report form POST requests
- Item details routes
- Static CSS and JavaScript file loading

---

## 8. Limitations

Some tests are still basic route and smoke tests because the project is a prototype. More strict database and end-to-end tests can be added later after the backend and database structure become more stable.

Future tests should include:

- Database record verification
- Uploaded photo path verification
- Claim request workflow testing
- GitHub Actions continuous integration
- Test coverage report

---

## Summary

This Week 7 testing plan applies Chapter 7 testing concepts to the Campus Lost and Found Platform. The selected user stories are tested using black-box, grey-box, and white-box thinking. The project will also include at least 15 automated tests using pytest.
