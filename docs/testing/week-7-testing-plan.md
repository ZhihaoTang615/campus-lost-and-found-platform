# Week 7 Testing Plan

## 1. Overview

This document discusses and plans the testing activities for the Campus Lost and Found Platform during Practical 7.

The objective of Practical 7 is Test-driven Development. The team selected five user stories and designed at least three test cases for each user story. The project also includes at least 15 automated tests implemented using pytest and the Flask test client.

The selected user stories are:

- US01 - Report Lost Item
- US02 - Report Found Item
- US03 - Search Items
- US04 - Filter Items
- US05 - View Item Details

---

## 2. Testing Objectives

The main objectives of testing are:

1. Confirm that the implemented features satisfy the selected user stories.
2. Check both successful and unsuccessful user actions.
3. Identify route, form, database, file upload, and template errors.
4. Prevent previously working features from breaking after new changes.
5. Allow the team to run the same tests repeatedly using one command.
6. Provide clear evidence that the Iteration 2 prototype works correctly.

---

## 3. Testing Approaches

### 3.1 Black-box Testing

Black-box testing checks the system from the user's point of view. The tester provides input and checks the visible output without depending on the internal implementation.

Black-box testing in this project includes:

- Opening web pages
- Submitting lost and found item forms
- Searching for items
- Applying filters
- Viewing item details
- Checking validation messages
- Checking handled 404 responses

### 3.2 Grey-box Testing

Grey-box testing checks visible behaviour while also examining some internal data or system behaviour.

Grey-box testing in this project includes:

- Checking SQL queries and query parameters
- Confirming that database commit is called
- Checking that uploaded image paths are stored correctly
- Confirming that the correct report type is saved
- Checking that search and filter parameters are sent correctly

### 3.3 White-box Testing

White-box testing uses knowledge of the application code and its branches.

White-box testing in this project includes:

- Testing the Flask route logic
- Testing lost and found report branches
- Testing valid and invalid image file branches
- Testing search and filter condition branches
- Testing existing and missing item branches
- Testing redirects and HTTP status codes

---

## 4. Test Environment

The automated tests use:

- Python
- Flask test client
- pytest
- Fake database connections
- Temporary upload directories

The fake database prevents automated tests from changing the real MySQL database. Temporary upload directories also prevent test images from being saved in the real project upload folder.

The automated test command is:

```bash
python -m pytest -v
```
