# Week 10 System Testing Plan

## 1. Purpose

This document defines the Week 10 system testing plan for the Campus Lost and Found Platform.

The purpose of system testing is to verify that the completed user stories work together correctly in the integrated Flask application before final submission and demonstration.

The plan is designed to be used during the Week 10 demonstration and final regression testing.

---

## 2. Scope

The completed system-testing scope includes:

- **US01 – Report Lost Item**
- **US02 – Report Found Item**
- **US03 – Search Items**
- **US04 – Filter Items**
- **US05 – View Item Details**
- **US06 – Upload/Display Item Photo**
- **US07 – Submit Claim Request**

The following user stories are **not part of the completed Week 10 implementation**:

- **US08**
- **US09**
- **US10**
- **US11**

These stories were deferred from Iteration 3 after the Iteration 2 velocity review so that the team could focus on quality, TDD, US06 completion and US07 persistence.

They must not be reported as completed functionality.

---

## 3. Test Environment

System testing should be performed using the final integrated version of the project.

### Application Environment

- Flask web application
- Python
- MySQL database
- HTML/CSS frontend
- pytest automated testing
- GitHub repository
- GitHub Project Board

### Browser Environment

Testing should be performed using a modern browser such as:

- Google Chrome
- Microsoft Edge
- Safari

### Repository State

Before system testing begins:

- the latest completed Pull Requests should be merged into `main`;
- the working copy should be updated from `main`;
- required database tables should be available;
- test data should be available;
- the application should start without errors.

---

## 4. Preconditions

Before executing the Week 10 system tests:

1. The Flask application starts successfully.
2. The MySQL database connection is available for integration testing.
3. The `items` table is available.
4. The `claims` table is available for US07 testing.
5. At least one lost-item record exists.
6. At least one found-item record exists.
7. At least one found item can be used for claim testing.
8. The upload directory is available.
9. Completed Iteration 3 work has been merged into `main`.
10. The tester has access to the GitHub Issues and Project Board for defect tracking.

---

## 5. System Test Cases

| Test ID | User Story | Test Scenario | Test Steps | Expected Result | Result |
|---|---|---|---|---|---|
| ST01 | US01 | Report a valid lost item | Open Report Lost Item, enter all required fields, submit the form | The lost-item report is accepted, stored successfully and the success feedback is displayed | Not Run |
| ST02 | US02 | Report a valid found item | Open Report Found Item, enter all required fields, submit the form | The found-item report is accepted, stored successfully and the success feedback is displayed | Not Run |
| ST03 | US03 | Search for an existing item | Open Browse Items, enter a keyword matching an item name, description or location | Matching items are displayed and unrelated items are excluded where applicable | Not Run |
| ST04 | US04 | Filter item results | Open Browse Items and select an implemented report-type or category filter | The displayed item list is restricted according to the selected filter | Not Run |
| ST05 | US05 | View item details | Select an existing item from Browse Items | The correct Item Details page loads and shows the stored item information | Not Run |
| ST06 | US06 | Upload and display a valid photo | Submit an item report with a supported image, then open the related Item Details page | The report is stored and the uploaded image is displayed on the correct Item Details page | Not Run |
| ST07 | US06 | Handle an item with no photo | Submit or open an item that has no uploaded photo | The Item Details page loads normally and shows the no-photo placeholder instead of crashing | Not Run |
| ST08 | US07 | Submit a valid claim request | Open a found item's Item Details page, select Submit Claim Request, complete all required fields and submit | The claim is stored, linked to the selected item, assigned initial status `pending`, and the user is redirected successfully | Not Run |
| ST09 | US07 | Handle missing claim form data | Open the claim form and attempt normal browser submission with a required field empty | Browser required-field validation prevents normal submission until all required fields are completed | Not Run |
| ST10 | US01-US07 | Full regression test | Run the complete pytest suite after the final Iteration 3 integration | All relevant automated tests pass and no completed user story is broken by Iteration 3 changes | Not Run |

---

## 6. Expected Results

A system test is considered successful when:

- the observed behaviour matches the expected result;
- no application crash occurs;
- previously completed functionality continues to work;
- database-dependent actions store or retrieve the expected data;
- navigation returns the user to the expected page;
- invalid or missing data is handled according to the implemented behaviour.

The **Result** field should be updated during Week 10 testing using values such as:

- `Pass`
- `Fail`
- `Blocked`
- `Not Run`

If a test fails, the tester should not simply change the expected result. The failure must be investigated and, when appropriate, recorded as a GitHub Issue.

---

## 7. Bug and Error Tracking Process

The project uses:

- GitHub Issues
- GitHub Project Board
- Pull Requests

for bug and error tracking.

The required workflow is:

```text
System test fails
→ create GitHub Issue
→ add labels: bug, testing, iteration-3
→ assign developer
→ Board: Todo
→ Board: In Progress
→ create fix branch
→ fix bug
→ add or update regression test
→ create Pull Request
→ Board: Testing
→ review and test
→ merge Pull Request
→ re-test failed system test
→ close Issue
→ Board: Done
```
A bug must not be moved to Done until:

the fix exists;
the relevant Pull Request is merged;
the failed test has been re-run;
verification evidence exists.

## 8. Bug Report Template

When a real defect is discovered during system testing, the GitHub Issue should contain the following information.

Bug Description

A short explanation of the observed defect.

Related User Story

Example:US07 – Submit Claim Request
Steps to Reproduce
Open the relevant page.
Perform the required action.
Enter the test data.
Submit or continue the workflow.
Observe the failure.
Expected Result

Describe what should happen according to the implemented acceptance criterion.

Actual Result

Describe what actually happened during testing.

Root Cause

Document the confirmed technical cause after investigation.

Fix

Describe the implemented correction.

Verification

Record:

regression-test result;
manual re-test result;
related commit;
related Pull Request.

No bug should be invented only to create evidence.

## 9. Historical Defect Evidence

Historical defects may be referenced only when repository evidence exists.

Examples that may be relevant include:

claim storage or database schema mismatch;
missing claimant contact field;
routing or static-resource problems.

For any historical bug included in final evidence, the team must confirm that repository evidence exists for:

the original problem;
the implemented fix;
the verification result.

If the evidence cannot be confirmed, the defect should not be presented as a verified project bug.

## 10. Exit Criteria

Week 10 system testing is complete when all of the following conditions are satisfied:

ST01-ST10 have been executed or have a documented reason for being blocked.
All critical US01-US07 workflows have been manually checked.
The final pytest regression suite passes.
Any discovered blocking defects have been fixed or formally documented.
Fixed bugs have been re-tested.
Relevant Pull Requests have been merged.
GitHub Board status matches the actual state of work.
Completed stories have evidence.
Deferred stories are not described as completed.
Final evidence is ready for Iteration 3 documentation.

## 11. Week 10 Demo Flow

The following sequence can be used during the final demonstration.

Step 1 – Home Page

Open the Campus Lost and Found Platform and briefly show the main navigation.

Step 2 – US01 Report Lost Item

Open Report Lost Item.

Enter valid lost-item data and submit the report.

Confirm that the workflow completes successfully.

Step 3 – US02 Report Found Item

Open Report Found Item.

Enter valid found-item data.

Upload a supported item photo.

Submit the report.

Step 4 – US03 Search Items

Open Browse Items.

Search using a keyword that matches an existing item.

Confirm that the matching result is displayed.

Step 5 – US04 Filter Items

Apply one of the implemented filters.

Confirm that the displayed results match the selected filter.

Step 6 – US05 View Item Details

Open one of the item results.

Show:

item name;
report type;
category;
status;
location;
date;
description;
contact information.
Step 7 – US06 Upload/Display Item Photo

Use an item that has an uploaded image.

Confirm that the image is displayed on Item Details.

Also show an item without a photo if time permits and confirm that the no-photo placeholder is displayed.

Step 8 – US07 Submit Claim Request

Open the Item Details page for a found item.

Select Submit Claim Request.

Enter:

Your Name;
Contact Information;
Claim Message.

Submit the claim.

Confirm successful submission and return to the related Item Details page.

Step 9 – Automated Regression Testing

Run:python -m pytest -v
Show the final passing pytest result.

Step 10 – GitHub Evidence

Show:

relevant GitHub Issues;
completed Pull Requests;
Iteration 3 Project Board;
testing documentation;
final evidence;
GitHub Pages if available.

## 12. Deferred Iteration 3 Backlog

US08, US09, US10 and US11 were originally part of the Iteration 3 backlog but were deferred after reviewing Iteration 2 delivery performance.

The Iteration 2 planning figures are:

Capacity: 45 person-days
Estimated story work completed: 14 person-days
Velocity ratio:
14 / 45 = 0.31
Therefore, the recorded Iteration 2 velocity is:

0.31

The Iteration 3 scope was reduced so that the team could prioritise:

quality;
TDD;
regression testing;
completion of US06 photo functionality;
completion of US07 claim persistence;
mock-object testing;
final system evidence.

US08-US11 remain deferred backlog items and must not be represented as completed in the final submission.

## 13. Final Test Evidence
The final system-testing evidence should include, where available:

completed ST01-ST10 results;
final pytest screenshot;
relevant bug Issue links;
regression-test evidence;
Pull Request links;
GitHub Board screenshot;
GitHub Pages link;
Iteration 3 TDD evidence.

These items will support the final Iteration 3 evidence document.

