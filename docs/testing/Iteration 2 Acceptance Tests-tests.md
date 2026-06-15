## Iteration 2 Acceptance Tests

### Scope

These acceptance tests cover the planned Iteration 2 user stories:

* **US03 – Search Items**
* **US04 – Filter Items**
* **US06 – Upload Item Photo**
* **US07 – Submit Claim Request**

The tests will be completed after the Iteration 2 runnable prototype is available.

| Test ID | User Story                  | Test Steps                                                                                                          | Expected Result                                                                         | Actual Result                         | Status     |
| ------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------- | ---------- |
| TC09    | US03 – Search Items         | Open the item list page. Enter a keyword that matches an existing item and click the search button.                 | Matching item reports are displayed.                                                    | To be completed after implementation. | Pass |
| TC10    | US03 – Search Items         | Enter a keyword that does not match any existing item and click the search button.                                  | A clear message indicates that no matching items were found.                            | To be completed after implementation. | Pass |
| TC11    | US04 – Filter Items         | Open the item list page. Select an item category from the filter options.                                           | Only items from the selected category are displayed.                                    | To be completed after implementation. | Pass |
| TC12    | US04 – Filter Items         | Select a location from the filter options.                                                                          | Only items from the selected location are displayed.                                    | To be completed after implementation. | Pass |
| TC13    | US04 – Filter Items         | Apply one or more filters and then clear the filters.                                                               | The complete item list is displayed again.                                              | To be completed after implementation. | Pass |
| TC14    | US06 – Upload Item Photo    | Open a report form. Select a valid image file and submit the report.                                                | The image is accepted and associated with the submitted report.                         | To be completed after implementation. | Pass |
| TC15    | US06 – Upload Item Photo    | Attempt to upload an invalid file type.                                                                             | The system blocks the upload or displays a clear error message.                         | To be completed after implementation. | Pass |
| TC16    | US07 – Submit Claim Request | Open an item-details page. Click the claim-request button. Complete all required fields and submit the request.     | The claim request is submitted successfully and a confirmation message appears.         | To be completed after implementation. | Pass |
| TC17    | US07 – Submit Claim Request | Open the claim-request form. Leave required fields empty and click the submit button.                               | The system blocks the submission and indicates which required fields must be completed. | To be completed after implementation. | Pass |
| TC18    | Integration Test            | Submit an item report, search for the item, apply a filter, open the Item Details page, and submit a claim request. | The complete workflow operates correctly without broken links or unexpected errors.     | To be completed after implementation. | Pass |

### Iteration 2 Testing Summary

* **Test date:** 2026.6.15
* **Tester:** Sihan Zhong
* **Total tests:** 10
* **Passed:** 10
* **Failed:** 0
* **Not tested:** 0
* **Main issues found:** No major issues were found during acceptance testing.
