# Iteration 3 Review

## Iteration Purpose

Iteration 3 concentrated on completing and verifying the photo-display and
claim-submission workflow, then strengthening regression, system-test, defect,
and final documentation evidence. This review does not restate disputed
capacity or velocity figures.

## Planned Work

The tracked Iteration 3 plan selected:

- US06: display an uploaded photo on Item Details and handle a missing photo;
- US07: store a claim for an existing item with initial `pending` status;
- focused TDD and mock-object testing;
- regression and system-test preparation; and
- final evidence documentation.

The plan also recorded US08–US11 as deferred. Its wider planning and
responsibility assertions remain historical records and are not re-certified by
this review.

## Delivered Work

Current source, tests, and Git history support:

- uploaded-photo display and a no-photo placeholder for US06;
- a persisted US07 claim linked by `item_id` with status `pending`;
- server-side rejection of empty or whitespace-only claim fields;
- a dedicated Claim Request Submitted page with Pending status, View Item
  Details, and Browse More Items actions;
- fake/mock database regression tests; and
- repository-recorded manual Flask/MySQL evidence for selected workflows.

## Unplanned Work

The repository does not establish that Bug #72 was formally classified as
unplanned work. It is therefore recorded as defect work discovered during
system testing, without assigning an estimate, severity, owner, or Board state
beyond the evidence that exists.

## Bug #72 – Empty Claim Request Validation

Bug #72 affected US07 because an empty claim could be stored. The evidenced
chain is:

1. system testing exposed the empty-claim behaviour;
2. the defect was recorded as Issue #72;
3. a failing regression test reproduced the missing validation;
4. server-side required-field validation was added;
5. the focused test passed;
6. PR #76 was merged;
7. a repository screenshot records the manual fixed-state retest; and
8. the current complete regression suite passes 21 tests.

Commit `050da84` contains the validation and regression test in the same commit,
so the repository does not preserve a separate commit for the Bug #72 RED
state. The before/fixed screenshots remain supporting historical evidence.

## Testing Outcome

The current automated result is **21 passed**. The suite covers US01–US07,
including claim validation, pending persistence, confirmation-page content and
navigation, checks that submitted contact and verification details are absent
from that page, missing-item behaviour, redirects, commits, and resource
cleanup.

Automated database behaviour uses fake or mocked connections. It does not
replace manual testing of the running Flask application with MySQL.

## Deferred Scope

US08 Track Claim Status, US09 Review Claim Requests, US10 Update Item Status,
and US11 View My Reports remain deferred.

US04 is delivered with report-type and category filters. The repository does not
prove formal approval of the change from the broader historical
location/date/status wording, so that scope decision still requires human
confirmation.

## Demonstration Evidence

The repository contains current final evidence alongside historical UI,
database, TDD, defect, and Board screenshots:

- [dedicated Claim Request Submitted page](../evidence/final-claim-success.png);
- [complete automated regression](../testing/images/iteration-3-final-regression-21-passed.png),
  recording 21 collected, 21 passed, and 0 failed; and
- [final Iteration 3 Board](../evidence/final-iteration-3-board.png).

The Board and regression images contain account or development-environment
context and require privacy review before public embedding.

`docs/client-feedback/iteration-3-feedback.md` is empty, so no Iteration 3
customer demonstration or feedback is claimed.

## Lessons Learned

- HTML required fields are not a substitute for server-side validation.
- A regression must verify both the visible response and the absence of an
  invalid database insert or commit.
- Automated fake/mock tests and manual MySQL evidence answer different testing
  questions and must be labelled separately.
- Historical screenshots must not be relabelled as the current final state.

## Process Improvements

Verified improvements include:

- server-side claim validation;
- a focused Bug #72 regression test;
- a complete 21-test regression run;
- a dedicated claim-success page;
- runtime upload patterns excluded from new Git tracking; and
- clearer final traceability, limitations, system-test, and delivery evidence.
