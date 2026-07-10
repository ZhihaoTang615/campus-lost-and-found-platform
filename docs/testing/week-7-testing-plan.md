# Week 7 Testing Plan

## Context

This document records the Week 7 testing plan for the Campus Lost and Found Platform.

The project is currently focused on Iteration 2 features, including search items, filter items, upload item photo, and submit claim request. Week 7 focuses on testing and continuous integration. The goal is to check whether the prototype works correctly from user, tester, and developer perspectives.

---

## 1. Testing Goals

The main testing goals are:

1. Check that completed or partially completed Iteration 2 user stories work as expected.
2. Test both success cases and failure cases.
3. Test user input validation.
4. Check whether data is stored and displayed correctly.
5. Identify unfinished or failing areas before the next demonstration.
6. Prepare the project for future automated testing and continuous integration.

---

## 2. Testing Views

The team will use three testing views.

| Testing Type | Meaning | How it applies to this project |
|---|---|---|
| Black-box testing | Test the system from the user's point of view without looking at the code | Check whether users can search, filter, upload photos, and submit claim requests through the interface |
| Grey-box testing | Test the system while checking some internal data or files | Check database records, uploaded photo paths, and stored claim request information |
| White-box testing | Test the internal logic of the code | Check route logic, form validation, search/filter logic, and claim status update logic |

---

## 3. User Stories Covered

| User Story | Feature | Testing Priority |
|---|---|---|
| US03 - Search Items | Search lost and found items by keyword | High |
| US04 - Filter Items | Filter items by report type and category | High |
| US06 - Upload Item Photo | Upload a photo when submitting a lost or found item report | High |
| US07 - Submit Claim Request | Submit a claim request for a found item | High |

---

## 4. Black-box Test Cases

| Test ID | User Story | Test Case | Steps | Expected Result | Status |
|---|---|---|---|---|---|
| TC-W7-01 | US03 | Search with a valid keyword | Open Browse Items page, enter an existing item keyword, submit search | Matching items are displayed | To be tested |
| TC-W7-02 | US03 | Search with no matching keyword | Open Browse Items page, enter a keyword that does not exist | A no results message or empty result state is shown | To be tested |
| TC-W7-03 | US04 | Filter by report type | Select Lost or Found filter on Browse Items page | Only matching report type items are displayed | To be tested |
| TC-W7-04 | US04 | Filter by category | Select a category filter | Only items from that category are displayed | To be tested |
| TC-W7-05 | US06 | Submit lost item with photo | Open Report Lost Item page, complete the form, attach a valid image, submit | The lost item report is submitted successfully | To be tested |
| TC-W7-06 | US06 | Submit found item with photo | Open Report Found Item page, complete the form, attach a valid image, submit | The found item report is submitted successfully | To be tested |
| TC-W7-07 | US06 | Upload invalid file type | Try to upload a non-image file | The system should reject the file or avoid saving it as a valid image | To be tested |
| TC-W7-08 | US07 | Submit valid claim request | Open item details page, complete claim request form, submit | Claim request is submitted or recorded successfully | To be tested |
| TC-W7-09 | US07 | Submit claim request with missing required fields | Leave required fields empty and submit | Validation message is shown and the claim is not submitted | To be tested |

---

## 5. Grey-box Test Cases

| Test ID | Feature | Test Case | Internal Check | Expected Result | Status |
|---|---|---|---|---|---|
| TC-W7-10 | Upload Photo | Check uploaded photo path | Inspect database or stored item data after submitting a report with photo | The photo filename or path is stored correctly | To be tested |
| TC-W7-11 | Item Report | Check submitted item record | Inspect database after submitting a lost or found report | New item record exists with correct item name, category, location, status, and contact info | To be tested |
| TC-W7-12 | Claim Request | Check claim request data | Inspect database or backend data after submitting a claim | Claim request is stored with item ID and user details | To be tested |
| TC-W7-13 | Search / Filter | Check backend result consistency | Compare displayed results with database records | Displayed results match stored item data | To be tested |

---

## 6. White-box Test Ideas

The following white-box tests can be automated later using a Python testing framework such as pytest.

| Test ID | Code Area | Test Idea | Expected Result |
|---|---|---|---|
| TC-W7-14 | Search logic | Pass a keyword that matches an item name | Matching item is returned |
| TC-W7-15 | Search logic | Pass a keyword that does not match any item | Empty list is returned |
| TC-W7-16 | Filter logic | Pass report type = Lost | Only lost items are returned |
| TC-W7-17 | Form validation | Submit required fields as empty | Validation error is returned |
| TC-W7-18 | Claim status logic | Create a new claim request | Claim status starts as Pending |

---

## 7. Test Data

The following sample data can be used for testing:

| Item Name | Report Type | Category | Location | Status |
|---|---|---|---|---|
| Blue Water Bottle | Found | Bottle | Library entrance | Unclaimed |
| Student ID Card | Found | Card | Cafeteria | Unclaimed |
| Black Backpack | Lost | Bag | Computer Lab | Open |
| Wireless Earbuds | Lost | Electronics | Study area | Open |

---

## 8. Continuous Integration Plan

The project currently uses GitHub for version control. A future improvement is to add continuous integration using GitHub Actions.

The planned CI workflow would:

1. Run when code is pushed to the repository.
2. Install project dependencies.
3. Run basic automated tests.
4. Fail the build if any test fails.
5. Show the result to the team in GitHub.

This will help the team detect broken code earlier and avoid discovering problems only during demonstrations.

---

## 9. Current Testing Limitations

Current limitations include:

1. Some tests are still manual because the project is a prototype.
2. Full automated backend testing has not been completed yet.
3. Photo preview and uploaded image display still need improvement.
4. Claim request workflow still needs final end-to-end testing.
5. GitHub Actions CI has not yet been fully configured.

---

## 10. Summary

Week 7 testing focuses on checking the quality of the Iteration 2 prototype. The team will test the system from black-box, grey-box, and white-box perspectives. The most important features to test are search, filter, photo upload, and claim request.

The testing plan also prepares the project for future automated testing and continuous integration.
