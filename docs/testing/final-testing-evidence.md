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
   Conflicts between those records and later retrospectives are called out in the
   [Final Rubric Audit](../final-rubric-audit.md).

The reproducible automated command is:

```bash
.venv/bin/python -m pytest -v
```

## Final Automated Regression

**Final result: 21 tests passed.**

The final command output is retained in the audit hand-off response rather than
represented by a fabricated screenshot. The repository contains older 15-, 16-,
18-, and 19-test screenshots; those remain historical milestones and are not
evidence of the current 21-test suite.

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
| US07 Submit Claim Request | `test_claim_request_stores_pending_claim_with_mock_database`; `test_claim_success_page_loads_with_confirmation`; `test_empty_claim_request_is_rejected`; `test_claim_request_for_missing_item_returns_404` | Existing-item lookup, complete/empty form paths, one parameterised insert, `pending`, commit, redirect, dedicated confirmation content, and GET missing-item 404 | Whitespace-only regression, missing-item POST, live MySQL transaction, concurrency/idempotency, CSRF, authentication, claim eligibility/business ownership rules |

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
- Later refactoring/validation work is visible in commit `876f0be` and merged
  claim-related PRs.

This supports a selected red/green/refactor example. It does not prove that every
user story was developed test-first.

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
- merged PRs #76, #80, and #81 for validation and confirmation-flow work.

The file
[`final-claim-success.png`](../evidence/final-claim-success.png) shows the older
in-page feedback implementation and must not be presented as the current
dedicated confirmation page. A current confirmation-page screenshot remains
missing.

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
- pending claim status and success-page navigation.

The fake result categories used in tests are sufficient for the tested response
paths but do not exactly mirror every category slug offered by the production
forms. This is a data-realism limitation, not a current regression failure.

## Remaining Testing Limitations

- No automated test connects to a real MySQL instance.
- No browser/UI automation, accessibility audit, responsive cross-browser test,
  or end-to-end filesystem/database test is present.
- No continuous-integration workflow is present.
- No performance, load, security, penetration, CSRF, authentication, or
  authorization testing is present.
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
- Direct navigation to the generic success route is possible and is not tied to
  a claim identifier.
- The backend does not enforce a rule restricting claims to a particular report
  type.
- Item Details displays report contact information; privacy expectations require
  product-owner confirmation.
- Historical manual screenshots may contain names, email addresses, phone
  numbers, claim messages, database rows, or a local username. They require
  privacy review before public submission.
