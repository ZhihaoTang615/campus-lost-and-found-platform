# Final System Testing Plan

## Purpose

This plan defines repeatable system checks for the delivered Flask/MySQL
application. It is a plan, not a claim that every row has a recorded final
execution result.

## Scope

Included: US01 Report Lost Item, US02 Report Found Item, US03 Search Items, US04
Filter Items, US05 View Item Details, US06 Upload Item Photo, and US07 Submit
Claim Request.

Deferred and excluded: US08 Track Claim Status, US09 Review Claim Requests, US10
Update Item Status, and US11 View My Reports.

For US04, test only the implemented report-type and category filters. Formal
confirmation of the difference from historical location/date/status criteria is
still required.

## Test Environment

- running Python/Flask application;
- local MySQL database created from `database.sql`;
- HTML/CSS/Jinja interface in a modern browser;
- writable `static/uploads/` directory; and
- pytest regression suite in an isolated virtual environment.

Repository screenshots show selected Chrome/macOS runs, but this plan does not
require or claim one exclusive browser/operating-system configuration.

## Preconditions

1. Create and activate `.venv`.
2. Install `requirements.txt`.
3. Configure untracked local values for `APP_SECRET_KEY`, `DB_HOST`, `DB_USER`,
   `DB_PASSWORD`, and `DB_NAME`.
4. Import `database.sql` and confirm `items` and `claims` exist.
5. Confirm `static/uploads/` exists and is writable.
6. Start Flask with `flask --app app run --debug`.
7. Use synthetic test data that contains no real personal information.

## Testing Perspectives

### Black-box

Observe page loading, form behaviour, search/filter results, item details,
photo display, validation feedback, redirects, and the claim-success page.

### Grey-box

After relevant user actions, inspect the MySQL row, relationship, `image_path`,
status, and absence of an invalid claim row. Check that new runtime uploads are
ignored by Git.

### White-box

Run pytest to exercise route branches, fake/mock SQL calls, missing items,
invalid extensions, empty inputs, redirects, commits, and cleanup.

## Manual/System Test Cases

| ID | Story | User Action / Input | Expected Black-box Result | Grey-box Check | Final Recorded Result |
|---|---|---|---|---|---|
| ST01 | US01 | Submit a valid lost-item report | Success feedback is displayed and the page remains usable | One `items` row has `report_type='lost'` and the entered fields | Not recorded in this plan |
| ST02 | US02/US06 | Submit a valid found-item report with a supported photo | Success feedback is displayed; Item Details displays the photo | One `items` row has `report_type='found'` and the expected `image_path` | Not recorded in this plan |
| ST03 | US03 | Search using a matching name, description, or location keyword | Matching results are displayed | Returned rows match the search condition | Not recorded in this plan |
| ST04 | US03 | Search using a value with no match | No Items Found is displayed without a crash | Query completes with no rows | Not recorded in this plan |
| ST05 | US04 | Apply report-type and category filters separately and together with search | Only matching results are displayed; Clear Filters resets controls | Query conditions and returned rows reflect only implemented filters | Not recorded in this plan |
| ST06 | US05/US06 | Open an existing item with a photo, then one without a photo | Stored details display; photo or no-photo placeholder appears | Displayed `image_path` and item ID match the selected row | Not recorded in this plan |
| ST07 | US07 | Submit all claim fields for an existing found item | Redirect to Claim Request Submitted; Pending, View Item Details, and Browse More Items are visible | Exactly one linked `claims` row exists with status `pending` | Repository evidence exists; repeat for final sign-off |
| ST08 | US07/Bug #72 | Send an empty/whitespace claim POST, including a direct request that bypasses browser `required` attributes | Validation message appears and no success redirect occurs | No claim INSERT or commit; no new claim row | Repository before/fixed evidence exists; repeat for final sign-off |
| ST09 | US05/US07 | Request a missing item ID | HTTP 404 with Item not found | No insert or commit | Not recorded in this plan |
| ST10 | US01–US07 | Run `python -m pytest -v` | All tests pass | Tests use fake/mock databases and temporary uploads, not live MySQL | Current automated result: 21 passed |

## Defect Workflow

```text
failed system check
→ record a GitHub Issue with steps, expected result, and actual result
→ reproduce with a focused regression where practical
→ implement the smallest correction
→ run the focused test
→ review and merge through a Pull Request
→ repeat the failed manual/system check
→ run the complete regression suite
→ update evidence and Board state manually
```

Bug #72 follows this evidenced chain for US07. Do not infer severity, estimate,
assignee, customer notification, or live Board state from this plan.

## Exit Criteria

System testing is complete only when:

- every applicable row has an observed result and evidence reference;
- database effects are verified for persistence workflows;
- fixed defects have focused and full regression results;
- the complete suite passes all 21 tests;
- no known critical defect remains;
- privacy-sensitive test data is removed from submission evidence;
- US08–US11 remain explicitly deferred; and
- the final Board and demonstration/feedback evidence are manually confirmed.

See [Final Testing Evidence](final-testing-evidence.md) for the current automated
result, repository-recorded manual artefacts, limitations, and privacy review.
