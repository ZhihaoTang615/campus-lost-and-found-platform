# Requirements Traceability

This matrix consolidates the final assessment scope against repository evidence.
It does not silently reconcile conflicting planning values.
Repository screenshots are treated as supporting artefacts, not as proof that a
complete final manual test cycle or customer acceptance occurred.

Evidence labels used below:

- **Confirmed repository evidence**: directly visible in tracked source, tests,
  documents, assets, or Git history.
- **Human confirmation required**: a value or claim conflicts across project
  records, or the repository does not contain enough evidence to verify it.
- **Missing evidence**: the expected record is not present in the repository.

## Final Delivered Scope

For US01–US07, the Priority column preserves the original GitHub Issue values on
the 10/20/30 scale: 10 is highest, 20 is medium, and 30 is lower.

| User Story | User Goal | Priority | Estimate | Iteration | Acceptance Criteria | Implementation Evidence | Automated Test Evidence | System or Manual Test Evidence | GitHub Issue or PR Evidence | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| US01 Report Lost Item | Submit a lost-item report so others can identify it. | 10 (highest) | 3 person-days, recorded consistently | 1 | Page loads; required report data is accepted; a lost record is inserted; invalid photo extensions are rejected. | [`report_lost_item()` and shared upload handling](../app.py); [`report-lost-item.html`](../templates/report-lost-item.html); [`items` schema](../database.sql) | [`test_report_lost_item_page_loads`, `test_valid_lost_item_report_is_saved`, `test_lost_item_rejects_invalid_photo_type`](../tests/test_report_items.py) | Final lost-item UI screenshots exist in [`evidence/`](evidence/). The Iteration 1 acceptance template still says Not Tested, so no final manual pass is inferred. | No explicit issue/PR-to-story mapping was found. **Human confirmation required.** | **Delivered** |
| US02 Report Found Item | Submit a found-item report so its owner can locate it. | 10 (highest) | 3 person-days, recorded consistently | 1 | Page loads; required report data is accepted; a found record is inserted; a supported photo can be saved. | [`report_found_item()` and shared upload handling](../app.py); [`report-found-item.html`](../templates/report-found-item.html); [`items` schema](../database.sql) | [`test_report_found_item_page_loads`, `test_valid_found_item_report_is_saved`, `test_found_item_report_saves_valid_photo`](../tests/test_report_items.py) | Final found-item UI screenshots exist in [`evidence/`](evidence/). The Iteration 1 acceptance template still says Not Tested, and the images require privacy review. | No explicit issue/PR-to-story mapping was found. **Human confirmation required.** | **Delivered** |
| US03 Search Items | Search item reports by keyword. | 10 (highest) | Original GitHub Issue: 2 person-days | 2 | Keyword matches item name, description, or location; no-result searches are handled. | [`items()` query construction](../app.py); [`items.html`](../templates/items.html) | [`test_browse_items_page_loads`, `test_search_uses_keyword_for_name_description_and_location`, `test_search_with_no_matching_result_is_handled`](../tests/test_search_filter.py) | Search/filter screenshots in [`evidence/`](evidence/) and historical Iteration 2 system evidence. | No explicit issue/PR-to-story mapping was found. **Human confirmation required.** | **Delivered** |
| US04 Filter Items | Narrow the browse list using supported filters. | 20 (medium) | Original GitHub Issue: 3 person-days; Week 6 revised estimate: 2 person-days; Iteration 3 remaining-task estimates: 1 person-day each for location and date | 2, with proposed carry-over in 3 | **Implemented scope:** filter by report type and category, and combine filters with search. **Original criteria not fully implemented:** location, date, and status filters. | [`items()` filters](../app.py); [`items.html`](../templates/items.html) | [`test_filter_items_by_report_type`, `test_filter_items_by_category`, `test_combined_search_and_filters`](../tests/test_search_filter.py) | Search/filter screenshot in [`evidence/final-search-filter.png`](evidence/final-search-filter.png). It proves the implemented controls, not the original criteria, and exposes browser-profile context that should be replaced before publication. | No explicit issue/PR-to-story mapping was found. **Human confirmation required.** | **Delivered at the implemented report-type/category scope; formal refinement of the broader criteria requires confirmation.** |
| US05 View Item Details | Open one report and inspect enough detail to assess a match. | 10 (highest) | 2 person-days, recorded consistently | 1 | The browse entry route redirects correctly; an existing item is displayed; a missing item returns 404. | [`item_details()` entry redirect and `item_detail()` renderer](../app.py); [`item-details.html`](../templates/item-details.html) | [`test_item_details_entry_route_redirects_to_items`, `test_existing_item_details_are_displayed`, `test_missing_item_returns_404`](../tests/test_item_details.py) | Item-details screenshots in [`evidence/`](evidence/). The page exposes report contact data, so public screenshots require privacy review. | Git history contains merged PR [#47](https://github.com/ZhihaoTang615/campus-lost-and-found-platform/pull/47); the repository does not contain a complete issue-to-acceptance mapping. | **Delivered** |
| US06 Upload Item Photo | Attach a photo to an item report and display it for identification. | 30 (lower) | Original GitHub Issue: 5 person-days; Week 6 revised estimate: 2 person-days; Iteration 3 remaining-task estimate: 1 person-day | Began in 2; carried over and verified in 3 | Supported filename extensions are accepted and saved; unsupported extensions are rejected; stored photos display on details; missing photos use a placeholder. | Upload helpers and report routes in [`app.py`](../app.py); [`item-details.html`](../templates/item-details.html); runtime directory [`static/uploads/`](../static/uploads/) | [`test_lost_item_rejects_invalid_photo_type`, `test_found_item_report_saves_valid_photo`](../tests/test_report_items.py); [`test_item_details_displays_uploaded_photo`, `test_item_details_without_photo_displays_placeholder`](../tests/test_item_details.py) | [`final-uploaded-photo-display.png`](evidence/final-uploaded-photo-display.png) and Iteration 3 US06 screenshots prove a representative path. The final-named image displays a phone number and should be replaced or redacted before publication. | Git history contains merged PRs [#15](https://github.com/ZhihaoTang615/campus-lost-and-found-platform/pull/15), [#34](https://github.com/ZhihaoTang615/campus-lost-and-found-platform/pull/34), [#65](https://github.com/ZhihaoTang615/campus-lost-and-found-platform/pull/65), and [#68](https://github.com/ZhihaoTang615/campus-lost-and-found-platform/pull/68). Planning records reference Issue 53; final issue closure/acceptance requires confirmation. | **Delivered**, with upload-hardening limitations recorded in the final testing evidence |
| US07 Submit Claim Request | Submit an ownership claim for an existing item. | 10 (highest) | Original GitHub Issue: 4 person-days; Week 6 revised estimate: 2 person-days; Iteration 3 remaining-task estimate: 1 person-day | Began in 2; carried over and verified in 3 | Required fields are validated; the target item must exist; one claim is inserted with `pending`; the user is redirected to a dedicated confirmation page showing `Pending`, **View Item Details**, and **Browse More Items**. | [`claim_request()`, `save_claim_request()`, and `claim_success()`](../app.py); [`claim-request.html`](../templates/claim-request.html); [`claim-success.html`](../templates/claim-success.html); [`claims` schema](../database.sql) | [`test_claim_request_stores_pending_claim_with_mock_database`, `test_claim_success_page_loads_with_confirmation`, `test_empty_claim_request_is_rejected`, `test_claim_request_for_missing_item_returns_404`](../tests/test_claim_request_mock.py) | Claim form and database screenshots in [`evidence/`](evidence/). The only success-named screenshot is obsolete and shows the earlier in-page feedback flow; there is **no current dedicated-success-page screenshot**. | Git history contains merged PRs [#52](https://github.com/ZhihaoTang615/campus-lost-and-found-platform/pull/52), [#76](https://github.com/ZhihaoTang615/campus-lost-and-found-platform/pull/76), [#80](https://github.com/ZhihaoTang615/campus-lost-and-found-platform/pull/80), and [#81](https://github.com/ZhihaoTang615/campus-lost-and-found-platform/pull/81). Planning records reference Issue 54 and Bug 72; final issue metadata/acceptance requires confirmation. | **Delivered; report-type eligibility is not enforced by the backend.** |

## Iteration 2 Metrics

Iteration 2 selected 14 person-days of story effort. Retrospective records
identify 2 person-days of end-to-end completed story value and 12 person-days
remaining. Repository records disagree on whether the iteration contained 15 or
20 working days, so no single actual velocity is asserted. The historical 0.31
figure represents planned utilisation only under the 15-working-day scenario,
not actual velocity.

Only US03 Search Items met the end-to-end completion criteria by the end of
Iteration 2. US04, US06, and US07 were not fully complete. US06 photo-display
and US07 claim-persistence completion work occurred later in Iteration 3.

| Duration scenario | Raw capacity | Actual velocity | Planned utilisation |
|---|---:|---:|---:|
| 15 working days | 3 × 15 = 45 person-days | 2 / 45 = 0.0444 (4.44%) | 14 / 45 = 0.3111 (31.11%) |
| 20 working days | 3 × 20 = 60 person-days | 2 / 60 = 0.0333 (3.33%) | 14 / 60 = 0.2333 (23.33%) |

## Deferred Scope

The following stories are explicitly outside the delivered system and must not be
presented as implemented:

| User Story | Final Status | Repository Evidence |
|---|---|---|
| US08 Track Claim Status | Deferred, not delivered | Final title/status: [`requirements.md`](requirements.md); deferral record: [`iteration-3-deferred-backlog.md`](iterations/iteration-3-deferred-backlog.md) |
| US09 Review Claim Requests | Deferred, not delivered | Final title/status: [`requirements.md`](requirements.md); deferral record: [`iteration-3-deferred-backlog.md`](iterations/iteration-3-deferred-backlog.md) |
| US10 Update Item Status | Deferred, not delivered | Final title/status: [`requirements.md`](requirements.md); deferral record: [`iteration-3-deferred-backlog.md`](iterations/iteration-3-deferred-backlog.md) |
| US11 View My Reports | Deferred, not delivered | Final title/status: [`requirements.md`](requirements.md); deferral record: [`iteration-3-deferred-backlog.md`](iterations/iteration-3-deferred-backlog.md) |

## Traceability Conclusions

1. US05–US07 additionally have explicit PR mappings in the repository history.
2. US01–US03 have working implementation and tests, but explicit GitHub
   issue/PR acceptance mappings are missing.
3. US04 is the principal scope risk. The automated suite proves report-type and
   category filtering, not the original location/date/status acceptance criteria.
4. Original GitHub Issue priorities and estimates for US01–US07 are recorded
   above. Later re-estimates are separately labelled and do not replace the
   original values.
5. Manual evidence is useful demonstration support, but it is not a substitute
   for live-database or browser automation and may contain personal data.
