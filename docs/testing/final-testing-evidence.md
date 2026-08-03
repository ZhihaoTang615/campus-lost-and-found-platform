# Final Testing Evidence

## Testing Strategy

The final evidence combines three different levels and keeps their limitations
explicit:

1. **Automated Flask tests** use the Flask test client with fake or mocked
   database objects. They verify route behaviour, generated SQL parameters,
   redirects, response content, and selected validation paths without requiring
   a live MySQL server.
2. **Repository system-test records and screenshots** show selected manual
   Flask/MySQL workflows. These artefacts are historical evidence; they are not a
   reproducible browser-automation suite and were not independently witnessed
   during this audit.
3. **Acceptance-test documents** record expected scenarios and claimed outcomes.
   Conflicts between those records and current evidence are not silently treated
   as final acceptance; see
   [Requirements Traceability](../requirements-traceability.md).

## Black-box, Grey-box, and White-box Perspectives

### Black-box

User-visible checks cover forms loading and submitting, lost/found reports,
keyword search and no-result handling, report-type/category filters, Item
Details, uploaded-photo display and fallback, valid claim submission, empty
claim rejection, and the dedicated Claim Request Submitted page. The later
lecturer-requested refinement additionally covers registration, login, logout,
session-aware navigation, My Reports isolation, authorization, and the read-only
administrator records view.

### Grey-box

Repository-recorded manual evidence inspects selected MySQL item/claim rows and
`image_path`/`pending` values while using the running Flask application. Source
and test evidence verifies parameterised persistence, commits, and cursor and
connection cleanup; `.gitignore` records the exclusion rule for new runtime
uploads. Current source/test evidence also checks normalized emails, password
hashing, authenticated ownership for every new row, logged-out route guards,
the public-entry static-asset allowlist, and legacy-record `LEFT JOIN`
behaviour. Nullable ownership is exercised only as historical migration data.
These checks are not an automated live-MySQL integration suite.

### White-box

The pytest suite exercises Flask routes and internal branches using fake or
mocked database connections. It covers valid and invalid paths, missing items,
empty claim input, invalid file extensions, SQL parameters, redirect/response
content, checks that submitted contact and verification details are absent from
the confirmation page, commit behaviour, and resource cleanup. The expanded
suite also covers generic login failure, hashed registration, safe local
redirects, session clearing, login guards across operational routes, required
item/claim ownership, My Reports isolation, administrator summaries and legacy
rows, and read-only administrator behaviour.

The reproducible automated command is:

```bash
.venv/bin/python -m pytest -v
```

## Final Automated Regression

**Current final result: 95 tests passed.**

The regression screenshot,
[`iteration-3-final-regression-21-passed.png`](images/iteration-3-final-regression-21-passed.png),
records **21 collected, 21 passed, and 0 failed** for the completed US01–US07
baseline. It remains valid historical evidence but is not evidence of the
expanded 95-test suite. The current command result comprises the unchanged
21-test baseline plus 74 collected cases for the later user/administrator
refinement. No replacement screenshot is claimed here. The older 15-, 16-,
18-, and 19-pass screenshots also remain historical milestones.

All automated database interactions are fakes or mocks. A green automated result
therefore does **not** prove MySQL connectivity, schema installation, filesystem
permissions, browser rendering, or deployment configuration.

## Test Coverage by User Story

| Story | Automated Tests | What They Prove | What They Do Not Prove |
|---|---|---|---|
| US01 Report Lost Item | `test_report_lost_item_page_loads`; `test_valid_lost_item_report_is_saved`; `test_lost_item_rejects_invalid_photo_type` | Page availability, parameterised item insertion, lost report type, invalid extension rejection | Live MySQL insert, valid lost-photo path, MIME/content validation, file cleanup after DB failure |
| US02 Report Found Item | `test_report_found_item_page_loads`; `test_valid_found_item_report_is_saved`; `test_found_item_report_saves_valid_photo` | Page availability, parameterised item insertion, found report type, supported photo filename handling | Live MySQL/filesystem integration, upload size, MIME, duplicate filenames |
| US03 Search Items | `test_browse_items_page_loads`; `test_search_uses_keyword_for_name_description_and_location`; `test_search_with_no_matching_result_is_handled` | Browse response, the keyword SQL pattern for name/description/location, graceful no-result response | Query performance, collation/case behaviour on the deployed database, browser interaction |
| US04 Filter Items | `test_filter_items_by_report_type`; `test_filter_items_by_category`; `test_combined_search_and_filters` | Expected report-type/category SQL and parameter construction, including combination with search, against a fake cursor | Actual MySQL query execution/results; original location/date/status filter criteria; formal scope acceptance |
| US05 View Item Details | `test_item_details_entry_route_redirects_to_items`; `test_existing_item_details_are_displayed`; `test_missing_item_returns_404` | Entry redirect, existing record rendering, GET 404 for a missing record | Authorization/privacy decisions, accessibility, missing-item claim POST beyond the separate claim test |
| US06 Upload Item Photo | `test_item_details_displays_uploaded_photo`; `test_item_details_without_photo_displays_placeholder`, plus the US01/US02 upload tests | Stored filename display, placeholder path, representative valid/invalid extension paths | Unavailable stored file, MIME spoofing, maximum size, name collision, orphan cleanup |
| US07 Submit Claim Request | `test_claim_request_stores_pending_claim_with_mock_database`; `test_claim_success_page_loads_with_confirmation`; `test_empty_claim_request_is_rejected`; `test_claim_request_for_missing_item_returns_404` | Existing-item lookup, complete/empty form paths, one parameterised insert, `pending`, commit, redirect, dedicated confirmation content, and GET missing-item 404 | Whitespace-only regression, missing-item POST, live MySQL transaction, concurrency/idempotency, CSRF, and claim-eligibility rules |
| User registration | Registration tests in `test_user_admin_system.py` | Page load, normalized email, password hash rather than raw password, fixed public `user` role, duplicate/missing/whitespace/format/length/mismatch validation | Email ownership, password strength beyond length, delivery or recovery workflows, live MySQL |
| Login/logout and authorization | Login, logout, safe-next, and protected-route tests in `test_user_admin_system.py` | Normal/admin sessions, generic invalid message, external redirect rejection, POST-only logout, session clearing, login/admin guards and 403 for normal users | Brute-force resistance, CSRF protection, cookie behaviour in a deployed browser, password recovery or MFA |
| Protected operations, ownership, and My Reports | Access, ownership, and account-isolation tests in `test_user_admin_system.py` | Logged-out operational-route redirects, authenticated item/claim inserts, missing-session helper rejection, parameterised own-user filtering, required report fields/navigation, and cross-account isolation including administrators | Retrospective ownership of legacy rows, report editing, live concurrent accounts |
| Read-only administrator dashboard | Administrator display/query tests in `test_user_admin_system.py` | Summary labels/counts, all item and claim rows, `LEFT JOIN users`, registered and legacy labels, no commits/state-changing SQL, rejected POST | Large-dataset performance, production privacy policy, administrator account lifecycle |

## TDD Evidence

Repository history and screenshots record a US07 TDD sequence:

- RED evidence: the claim persistence test initially failed; the repository
  records commit `33ce1e4` and
  [`us07-claim-storage-red.png`](images/us07-claim-storage-red.png).
- GREEN evidence: minimum claim persistence behaviour was implemented; the
  repository records commit `050f6f3` and
  [`us07-claim-storage-green.png`](images/us07-claim-storage-green.png).
- Both repository-recorded screenshots were added with the TDD evidence in commit
  `3210869` and merged through PR #58. The later `docs/evidence/iteration3-*`
  images show a broader two-test state and are not used as the minimum GREEN.
- Commit `876f0be` extracts claim persistence into `save_claim_request()` while
  preserving the earlier claim-storage behaviour.

This supports a selected red/green/refactor example. It does not prove that every
user story was developed test-first.

Bug #72 is a separate defect-driven RED/GREEN example. System testing exposed an
empty stored claim; a failing regression reproduced it; server-side validation
and the regression test landed together in commit `050da84`; and PR #76 merged
the correction. There is no separately committed RED test state for this bug,
so that boundary is stated rather than reconstructed.

## Claim Request Defect Evidence

The final claim workflow is:

1. Receive a request for an item ID and query that item.
2. Return 404 if the referenced item does not exist.
3. On POST, read and strip form keys `name`, `contact`, and `message`.
4. Reject empty or whitespace-only values.
5. Map those values to the claim columns and insert one row with lowercase
   database status `pending`.
6. Commit and redirect to `/claim-success/<item_id>`.
7. Render **Claim Request Submitted**, visible status **Pending**, and the
   **View Item Details** and **Browse More Items** actions.

Evidence includes:

- empty-claim before/fix screenshots in [`testing/images/`](images/);
- current server-side rejection test in
  [`test_claim_request_mock.py`](../../tests/test_claim_request_mock.py);
- a stored pending-claim screenshot,
  [`claim-database-verification.png`](../evidence/claim-database-verification.png)
  (**privacy-sensitive:** it exposes local paths and personal-looking test data;
  redact or omit it before public submission);
- a fixed-state manual retest screenshot,
  [`system-test-bug-empty-claim-fixed.png`](images/system-test-bug-empty-claim-fixed.png);
- local merge commits for PRs #76, #80, and #81 covering validation and the
  confirmation flow.

The current dedicated Claim Request Submitted page is recorded in
[`final-claim-success.png`](../evidence/final-claim-success.png). The current
final Iteration 3 Board is recorded in
[`final-iteration-3-board.png`](../evidence/final-iteration-3-board.png).

## Test Data Coverage

The suite contains representative values for:

- lost and found report types;
- item names, descriptions, locations, and categories;
- keyword and no-result searches;
- report-type/category filters and a combined query;
- supported `.jpg` upload and rejected `.exe` upload;
- stored photo and no-photo placeholder cases;
- existing and missing item IDs;
- complete and empty claim form values;
- pending claim status and success-page navigation;
- normalized/duplicate/invalid registration data and hashed passwords;
- normal-user and administrator roles, safe/unsafe redirects, and logout;
- required authenticated ownership, logged-out access attempts, and two-account
  My Reports isolation; and
- owned current rows plus pre-enhancement legacy item/claim rows on the
  read-only administrator view.

The fake result categories used in tests are sufficient for the tested response
paths but do not exactly mirror every category slug offered by the production
forms. This is a data-realism limitation, not a current regression failure.

## Remaining Testing Limitations

- No automated test connects to a real MySQL instance.
- No browser/UI automation, accessibility audit, responsive cross-browser test,
  or end-to-end filesystem/database test is present.
- No continuous-integration workflow is present.
- No performance, load, penetration, CSRF, browser-cookie, or deployed security
  testing is present. Authentication and authorization do have automated
  fake/mock coverage, but not an independent security assessment.
- Upload validation checks filename extension only; MIME type, size, collision,
  path lifecycle, and orphan-file behaviour are not tested.
- A valid lost-item photo upload is not explicitly tested.
- A database filename whose file is unavailable on disk is not explicitly
  tested.
- Lost/found report fields rely on HTML `required` attributes and direct
  `request.form[...]` access; the backend has no explicit empty-value validation
  and the suite has no missing/empty report-field regression. Browser
  requirements can be bypassed, and a missing key produces Flask's generic 400.
- Whitespace-only claim input is handled by the implementation but is not a
  dedicated regression test.
- The missing-item claim regression sends GET only; a missing-item POST is not a
  separate test.
- Direct authenticated navigation to the generic success route is possible and
  is not tied to a claim identifier.
- The backend does not enforce a rule restricting claims to a particular report
  type.
- Registration uses basic email syntax and minimum password length only. There
  is no email verification, password reset, MFA, login throttling, or account
  management UI.
- The role is loaded into the signed Flask session at login; a database role
  change is not reflected until a later login/session refresh.
- The read-only Admin Dashboard displays claimant contact and verification
  details to administrators; production retention and privacy policy remain
  outside this university-project scope.
- Login-protected Item Details displays report contact information to any
  authenticated account; privacy expectations require product-owner
  confirmation.
- Historical manual screenshots may contain names, email addresses, phone
  numbers, claim messages, database rows, or a local username. They require
  privacy review before public submission.

## Privacy and Evidence Check

The following tracked files visibly expose personal or browser-context data and
should be replaced, redacted, or omitted from public submission:

- `docs/evidence/final-home-page.png`, `final-report-lost-item1.png`,
  `final-report-lost-item2.png`, `final-report-found-item1.png`, and
  `final-report-found-item2.png` — browser profile/account and local-browser
  context;
- `docs/evidence/final-search-filter.png` — open tabs, bookmarks, browser
  profile/avatar context, and unrelated account/service labels;
- `docs/evidence/final-uploaded-photo-display.png` — phone number;
- `docs/evidence/final-claim-form.png` — name, phone number, claim text, browser
  tabs/bookmarks, and profile/avatar context;
- `docs/evidence/claim-database-verification.png` — local username/path,
  hostname, names, email, phone number, claim text, and database rows;
- `docs/testing/images/us07-real-database-claim-saved.png` and
  `system-test-us07-mysql-pending-pass.png` — local development context plus
  names/contact or verification data;
- `docs/testing/images/system-test-us07-claim-entry-pass.png`,
  `system-test-bug-empty-claim-stored.png` — phone/contact or local terminal
  context;
- `docs/evidence/iteration3-red-test.png` and `iteration3-green-test.png` —
  names or verification text, local username/hostname/path, and development-tool
  context;
- `docs/evidence/iteration3-final-regression-19-passed.png` and the tracked
  terminal/IDE regression screenshots under `docs/testing/images/`, including
  `iteration-3-final-regression-21-passed.png` — local username, device/host name,
  path, or development-tool context; and
- `docs/evidence/final-iteration-3-board.png` — GitHub account name, profile
  avatar, and contributor avatars.

No database password is visible in the inspected screenshots.

Historical baseline/final-iteration evidence is present at:

- [`final-claim-success.png`](../evidence/final-claim-success.png);
- [`final-iteration-3-board.png`](../evidence/final-iteration-3-board.png); and
- [`iteration-3-final-regression-21-passed.png`](images/iteration-3-final-regression-21-passed.png).

The 21-pass image is explicitly the pre-refinement baseline. The current
95-pass result is the command result recorded above; this document does not
claim that an image of that expanded run exists.

The following requested evidence also exists, but all three items need
privacy-safe replacements:

- `final-search-filter.png`;
- `final-uploaded-photo-display.png`;
- `claim-database-verification.png`.

The opaque file
`docs/testing/images/463415eb7059b718a9d9d24d6d486044.png` is visibly an
Iteration 3 Board screenshot, but it shows Issue #63 In Progress. It remains a
historical checkpoint and is not substituted for the final Board evidence linked
above.
