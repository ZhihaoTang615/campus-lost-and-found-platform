# Iteration 3 TDD and Final Evidence

## 1. Purpose

This document collects the final Iteration 3 TDD, testing, implementation, project-management, and repository evidence for the Campus Lost and Found Platform.

The final evidence focuses only on work that has been implemented, tested, merged, and supported by repository evidence.

---

## 2. Iteration 3 Scope

The final completed scope includes:

- US01 – Report Lost Item
- US02 – Report Found Item
- US03 – Search Items
- US04 – Filter Items
- US05 – View Item Details
- US06 – Upload/Display Item Photo
- US07 – Submit Claim Request

The following stories remain deferred:

- US08
- US09
- US10
- US11

They are not presented as completed functionality.

---

## 3. US07 TDD Evidence

### RED

The US07 claim persistence work used a failing automated mock-object test before the persistence implementation was completed.

Evidence image:

`docs/testing/images/us07-claim-storage-red.png`

Related implementation PR:

- PR #52 – Complete US07 claim request storage using TDD

### GREEN

After the minimum claim-storage implementation was added, the mock-object test passed.

Evidence image:

`docs/testing/images/us07-claim-storage-green.png`

The implementation stores:

- selected item ID;
- claimant name;
- claimant contact;
- verification details;
- initial status `pending`.


### REFACTOR

After the GREEN stage, the US07 claim persistence implementation was refactored to improve separation of responsibilities while preserving the required behaviour.

The claim persistence logic was extracted into a dedicated helper function.

**Refactor commit:**

- `876f0be5518e76411ba7260ea1c6e7c577a1b851` – `refactor: extract claim persistence helper`

Related Pull Request:

- PR #52 – Complete US07 claim request storage using TDD

The refactor maintained the passing claim-storage test and kept the claim persistence behaviour unchanged.


---

## 4. Mock Object Test Evidence

The US07 automated test uses Python `unittest.mock`.

The implementation uses:

- `MagicMock`;
- `patch`;
- mocked database connection;
- mocked database cursor.

Actual test file:

`tests/test_claim_request_mock.py`

The test verifies that:

- the selected item is retrieved;
- a claim INSERT is executed;
- the correct item ID is stored;
- claimant information is stored;
- verification details are stored;
- status is `pending`;
- the database transaction is committed.

Related Pull Request:

- PR #52 – Complete US07 claim request storage using TDD

Related research:

- Issue #59 – Research Python mock object framework
- PR #70 – docs: add Python mock object research

---

## 5. US06 Photo Evidence

US06 photo display functionality is supported by implementation and regression-test evidence.

Related Pull Requests:

- PR #65 – Frontend/iteration3 photo display
- PR #68 – Add US06 photo display regression tests

The regression tests verify:

- an uploaded image path is rendered on Item Details;
- an item without a photo displays the fallback placeholder.

Recorded regression result for the US06 work:

- Full regression suite: 18 passed

Evidence image:

`docs/testing/images/us06-full-regression-18-passed.png`

---

## 6. US07 Evidence Images

The following evidence images were added through PR #58:

- `docs/testing/images/us07-claim-storage-red.png`
- `docs/testing/images/us07-claim-storage-green.png`
- `docs/testing/images/us07-full-regression-16-passed.png`
- `docs/testing/images/us07-real-database-claim-saved.png`

These images provide evidence for:

- RED;
- GREEN;
- regression testing;
- real database claim persistence.

---

## 7. Final Pytest Result

The final Iteration 3 regression test was completed on the latest integrated `main` branch.

Final result:

- **19 tests collected**
- **19 tests passed**
- **0 failures**
- **Runtime: 0.08 seconds**

The final regression suite includes coverage for:

- US01 – Report Lost Item
- US02 – Report Found Item
- US03 – Search Items
- US04 – Filter Items
- US05 – View Item Details
- US06 – Upload/Display Item Photo
- US07 – Submit Claim Request
- Empty claim validation regression for Bug #72

Final evidence image:

`docs/testing/images/iteration-3-final-regression-19-passed.png`

Related Issue:

- Issue #61 – Run final Iteration 3 regression testing

**Status:** Completed.

---

## 8. GitHub Board Evidence

The final Iteration 3 Project Board was reviewed against the actual repository state.

At the time the final evidence was collected:

- Issue #61 – Run final Iteration 3 regression testing was completed and moved to Done.
- Issue #63 – Collect Iteration 3 TDD and final evidence remained In Progress while this document was being finalised.
- The Testing column contained no remaining tasks.
- Completed implementation, testing, documentation, bug-fix, UI and GitHub Pages tasks were recorded in Done.

Final Board screenshot:

`docs/testing/images/iteration-3-final-board.png`

The Board status matches the actual Iteration 3 work and supporting repository evidence.

---

## 9. Issue Evidence

Relevant Iteration 3 Issues include:

- #53 – Display uploaded photos on item details
- #54 – Store basic claim request with Pending status
- #55 – Create Iteration 3 UI design for photo and claim workflows
- #56 – Implement Iteration 3 templates and CSS
- #57 – Write Iteration 3 test specifications
- #58 – Add US07 TDD evidence images
- #59 – Research Python mock object framework
- #60 – Implement Python mock object test
- #61 – Run final Iteration 3 regression testing
- #62 – Publish completed story evidence to GitHub Pages
- #63 – Collect Iteration 3 TDD and final evidence

Issues must only be treated as complete when the required implementation or document exists, relevant evidence exists, and the associated Pull Request has been merged.

---

## 10. Pull Request Evidence

Relevant merged Pull Requests include:

- PR #52 – Complete US07 claim request storage using TDD
- PR #58 – Add US07 TDD evidence images
- PR #64 – docs: add Iteration 3 photo and claim UI design
- PR #65 – Frontend/iteration3 photo display
- PR #66 – Add Iteration 3 GitHub Pages documentation
- PR #67 – docs: add Iteration 3 test specifications
- PR #68 – Add US06 photo display regression tests
- PR #70 – docs: add Python mock object research

Additional final documentation PRs should be added before Issue #63 is completed.

---

## 11. GitHub Pages Evidence

Iteration 3 completed functionality is documented through the project's GitHub Pages work.

Related Pull Request:

- PR #66 – Add Iteration 3 GitHub Pages documentation

The published page documents:

- US06 uploaded photo display;
- US07 claim request workflow;
- testing evidence;
- completed Iteration 3 functionality only.

**Final GitHub Pages URL:** Pending final URL verification.

---

## 12. Iteration 3 Planning Consistency

The final project documentation uses:

- Capacity: 45 person-days
- Estimated user-story work: 14 person-days
- Velocity: 14 / 45 = 0.31

US08-US11 remain deferred.

The Iteration 3 scope was reduced to prioritise:

- US06 completion;
- US07 persistence;
- TDD;
- mock-object testing;
- regression testing;
- system testing;
- final evidence.

---

## 13. Final Team Responsibility Summary

### Zhihao Tang

Primary responsibility:

- technical lead;
- backend implementation;
- TDD;
- US07 persistence;
- Python mock test;
- automated regression testing;
- final technical integration.

### Sihan Zhong

Primary responsibility:

- documentation;
- testing specifications;
- mock-object research;
- GitHub Board management;
- deferred backlog documentation;
- system-testing plan;
- final evidence collection;
- documentation consistency audit.

### Jingyang Cai

Primary responsibility:

- UI/UX;
- Iteration 3 UI design;
- templates and CSS;
- uploaded-photo display UI;
- GitHub Pages evidence.

---

## 14. Final Completion Checklist

Before Issue #63 can move to Done:

- [x] RED evidence exists
- [x] GREEN evidence exists
- [x] exact REFACTOR commit confirmed
- [x] mock test exists
- [x] final pytest result added
- [ ] final Board screenshot added
- [x] Issue references collected
- [x] Pull Request references collected
- [x] final GitHub Pages URL verified
- [x] team responsibility summary completed
- [ ] final links checked
- [x] Issue #61 moved to Done after final regression testing
- [ ] Issue #63 moved to Done only after this evidence is complete
