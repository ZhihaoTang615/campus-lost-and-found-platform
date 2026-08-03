# Final System Testing Plan

## Purpose

This plan defines repeatable system checks for the delivered Flask/MySQL
application. It is a plan, not a claim that every row has a recorded final
execution result.

## Scope

Included: US01 Report Lost Item, US02 Report Found Item, US03 Search Items, US04
Filter Items, US05 View Item Details, US06 Upload Item Photo, and US07 Submit
Claim Request. The completed 21-test US01–US07 baseline is preserved.

Also included is the later refinement for the confirmed lecturer request that
the final version include a user system and an administrator system for viewing
lost-and-found records: registration, login, POST logout, authenticated-only
operational routes, required ownership for every new report/claim, My Reports
isolation, nullable pre-enhancement legacy compatibility, and the read-only
Admin Dashboard.

Deferred and excluded: US08 Track Claim Status, US09 approval/rejection and
other state-changing claim review, and US10 Update Item Status. My Reports now
covers the viewing intent of US11; report editing is not included.

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
4. For a fresh database, import `database.sql` and confirm `users`, `items`, and
   `claims` exist. For an existing baseline database, back it up and run
   `migrations/001_add_user_admin_system.sql` once.
5. Create a test administrator with `python scripts/create_admin.py`; do not use
   real or hard-coded credentials.
6. Confirm `static/uploads/` exists and is writable.
7. Start Flask with `flask --app app run --debug`.
8. Register a synthetic normal-user account for functional checks.
9. Use synthetic test data that contains no real personal information.

## Testing Perspectives

### Black-box

Observe page loading, form behaviour, shared session-aware navigation,
registration/login/logout feedback, search/filter results, item details, photo
display, My Reports isolation, administrator authorization and records, redirects,
and the claim-success page.

### Grey-box

After relevant authenticated user actions, inspect password hashes, normalized
emails, required ownership links, item/claim relationships, `image_path`,
status, and absence of an invalid claim row. Confirm only seeded
pre-enhancement legacy rows have `NULL` ownership, that those rows remain
visible to the administrator, and that new runtime uploads are ignored by Git.

### White-box

Run pytest to exercise route branches, fake/mock SQL calls, password hashing and
checking, safe redirects, logged-out operational-route guards, session state,
authorization, required insert ownership, ownership filters, legacy `LEFT JOIN`
output, missing items, invalid extensions, empty inputs, redirects, commits,
and cleanup.

## Manual/System Test Cases

Unless a case explicitly tests logged-out behavior, run it after signing in as
the appropriate synthetic normal user or administrator.

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
| ST10 | US01–US07 plus final user/admin refinement | Run `python -m pytest -v` | All tests pass | Tests use fake/mock databases and temporary uploads, not live MySQL | Current automated result: 95 passed; the older 21-pass screenshot is baseline evidence |
| ST11 | User registration | Register with mixed-case email and a valid password; repeat with duplicate, invalid, short, mismatched, missing, and whitespace-only values | Valid account redirects to Login with success feedback; invalid cases remain safe and public registration never creates admin | Stored email is lowercase, password value is a hash rather than raw text, and role is `user` | Automated coverage passes; repeat with live MySQL for final manual sign-off |
| ST12 | Login/logout and authorization | Log in as a user and administrator; try invalid credentials, an external `next`, GET logout, each report/browse/details/claim/My Reports route while logged out, and Admin as a normal user | Generic invalid message; safe role-based redirects; session-aware navigation; all operational routes redirect to Login; POST logout clears session; normal-user Admin returns 403 | Session contains only user ID, name, and role; no password/hash; no unsafe external redirect | Automated coverage passes; repeat in browser for final manual sign-off |
| ST13 | Ownership and My Reports | Submit reports and claims from two authenticated accounts; attempt helper calls without session state; compare both My Reports lists | Every accepted submission is owned, missing-session persistence is rejected, and each account sees only its own item reports newest first | Every new `user_id` matches the session; ownership query is parameterised by the logged-in ID; no new `NULL` owner is inserted | Automated coverage passes; repeat with live MySQL for final manual sign-off |
| ST14 | Read-only administrator view | Seed pre-enhancement `NULL`-owner rows, then open Admin as administrator alongside current owned rows | Summary, all items, all claims, account labels, and legacy fallbacks display; no mutation controls exist | Queries use `LEFT JOIN`; only seeded legacy rows are unowned; POST Admin is rejected; no commit or state-changing SQL occurs | Automated coverage passes; repeat in browser/live MySQL for final manual sign-off |

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
- the complete suite passes all 95 tests;
- no known critical defect remains;
- privacy-sensitive test data is removed from submission evidence;
- US08, state-changing US09, and US10 remain explicitly deferred; and
- the final Board and demonstration/feedback evidence are manually confirmed.

See [Final Testing Evidence](final-testing-evidence.md) for the current automated
result, repository-recorded manual artefacts, limitations, and privacy review.
