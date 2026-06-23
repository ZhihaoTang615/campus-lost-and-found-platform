# Iteration 2 Acceptance Tests

## Scope

These acceptance tests cover the planned Iteration 2 user stories:

* **US03 – Search Items**
* **US04 – Filter Items**
* **US06 – Upload Item Photo**
* **US07 – Submit Claim Request**

The purpose of these tests is to check whether the main Iteration 2 features work correctly in the runnable prototype.

| Test ID | User Story                  | Test Steps                                                                                                          | Expected Result                                                                         | Actual Result                                                                               | Status |
| ------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------ |
| TC09    | US03 – Search Items         | Open the item list page. Enter a keyword that matches an existing item and click the search button.                 | Matching item reports are displayed.                                                    | Matching item reports were displayed correctly.                                             | Pass   |
| TC10    | US03 – Search Items         | Enter a keyword that does not match any existing item and click the search button.                                  | A clear message indicates that no matching items were found.                            | The system showed a clear no-result message.                                                | Pass   |
| TC11    | US04 – Filter Items         | Open the item list page. Select an item category from the filter options.                                           | Only items from the selected category are displayed.                                    | Only items from the selected category were displayed.                                       | Pass   |
| TC12    | US04 – Filter Items         | Select a location from the filter options.                                                                          | Only items from the selected location are displayed.                                    | Only items from the selected location were displayed.                                       | Pass   |
| TC13    | US04 – Filter Items         | Apply one or more filters and then clear the filters.                                                               | The complete item list is displayed again.                                              | The full item list was displayed again after clearing filters.                              | Pass   |
| TC14    | US06 – Upload Item Photo    | Open a report form. Select a valid image file and submit the report.                                                | The image is accepted and associated with the submitted report.                         | The image file was accepted and linked to the submitted report.                             | Pass   |
| TC15    | US06 – Upload Item Photo    | Attempt to upload an invalid file type.                                                                             | The system blocks the upload or displays a clear error message.                         | The system showed a validation message for the invalid file type.                           | Pass   |
| TC16    | US07 – Submit Claim Request | Open an item-details page. Click the claim-request button. Complete all required fields and submit the request.     | The claim request is submitted successfully and a confirmation message appears.         | The claim request was submitted successfully and a confirmation message appeared.           | Pass   |
| TC17    | US07 – Submit Claim Request | Open the claim-request form. Leave required fields empty and click the submit button.                               | The system blocks the submission and indicates which required fields must be completed. | The system blocked the submission and showed validation feedback.                           | Pass   |
| TC18    | Integration Test            | Submit an item report, search for the item, apply a filter, open the item details page, and submit a claim request. | The complete workflow operates correctly without broken links or unexpected errors.     | The main Iteration 2 workflow operated correctly without broken links or unexpected errors. | Pass   |

## Iteration 2 Testing Summary

* **Test date:** 2026-06-15
* **Tester:** Sihan Zhong
* **Total tests:** 10
* **Passed:** 10
* **Failed:** 0
* **Not tested:** 0
* **Main issues found:** No major issues were found during acceptance testing.

## Notes

These tests show that the main Iteration 2 prototype features can support searching items, filtering results, uploading item photos, and submitting claim requests. The results also help the team decide which features are stable and which advanced features should be moved to the Next column for a future iteration.
