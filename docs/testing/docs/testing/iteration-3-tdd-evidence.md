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

The US07 implementation was refactored while maintaining passing tests.

Refactor evidence must reference the actual refactor commit or PR commit from the merged US07 work.

**Status:** Link to the exact refactor commit to be confirmed before final merge.

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

The final Iteration 3 regression test is tracked by:

- Issue #61 – Run final Iteration 3 regression testing

**Status:** Pending final Issue #61 completion.

The final result must only be added after the complete pytest suite has been run against the final integrated `main` branch.

Required final evidence:

- final pytest result;
- number of tests passed;
- screenshot path;
- confirmation that no regression failure remains.

This section must be updated before Issue #63 is moved to Done.

---

## 8. GitHub Board Evidence

The Iteration 3 Project Board currently records:

- completed implementation and documentation tasks in Done;
- Issue #61 in Testing while final regression testing is active;
- Issue #63 in In Progress while final evidence is being collected.

Final Board screenshot:

**Pending final Board screenshot after Issue #61 is completed.**

The final screenshot must show the Board status matching the actual repository state.

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
- [ ] exact REFACTOR commit confirmed
- [x] mock test exists
- [ ] final pytest result added
- [ ] final Board screenshot added
- [x] Issue references collected
- [x] Pull Request references collected
- [ ] final GitHub Pages URL verified
- [x] team responsibility summary completed
- [ ] final links checked
- [ ] Issue #61 moved to Done after final regression testing
- [ ] Issue #63 moved to Done only after this evidence is complete
