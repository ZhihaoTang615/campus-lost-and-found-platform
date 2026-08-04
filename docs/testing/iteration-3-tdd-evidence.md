# Iteration 3 TDD and Defect Evidence

## Purpose and Scope

This document separates verified RED, GREEN, REFACTOR, defect, and regression
evidence for US07. It does not infer Issue states, Board states, customer
acceptance, estimates, or team responsibilities.

At the recorded pre-user/admin Iteration 3 milestone, the delivered stories were
US01–US07 and US08–US11 were deferred. A later lecturer-requested refinement
added registration, login, protected operations, ownership, My Reports, and a
read-only Admin Dashboard. In the current final scope, US08 and US10 remain
deferred; US09 remains deferred because claims cannot be approved or rejected;
and the view-only portion of US11 is delivered through My Reports. See the
[Iteration 3 Review](../iterations/iteration-3-review.md) and
[Delivered Solution](../delivered-solution.md) for current final status.

## Bug #72 – Empty Claim Submission

Bug #72 affected US07: an empty claim request could be stored. Repository
screenshots record the before and fixed states, and local Git history contains
the validation correction and PR #76 merge.

### RED

System testing exposed an empty stored claim. A regression test demonstrated
that the route did not reject an empty claim submission correctly.

Evidence:

- Issue #72 is visible in the recorded final Iteration 3 Board screenshot,
  [`final-iteration-3-board.png`](../evidence/final-iteration-3-board.png);
- [`system-test-bug-empty-claim-stored.png`](images/system-test-bug-empty-claim-stored.png)
  records the invalid stored row; and
- `test_empty_claim_request_is_rejected` is the current regression test.

The validation and regression test were committed together in `050da84`.
Consequently, local Git history does not preserve a separate commit containing
only the failing Bug #72 test. That missing isolated RED commit is not
reconstructed.

### GREEN

Server-side validation strips `name`, `contact`, and `message`, rejects any
empty or whitespace-only value, displays `All claim fields are required.`, and
returns without inserting or committing.

The focused regression verifies:

- HTTP 200 with the validation message;
- only the item lookup is executed;
- no claim INSERT occurs; and
- no commit occurs.

Evidence:

- validation and test: commit `050da84`;
- delivery: local merge commit for PR #76;
- manual fixed state:
  [`system-test-bug-empty-claim-fixed.png`](images/system-test-bug-empty-claim-fixed.png).

### REFACTOR

No repository evidence proves a refactor performed specifically after the Bug
#72 GREEN step. Ordinary validation changes are therefore not labelled as a
refactor.

An earlier US07 persistence TDD sequence does contain a supported refactor:
commit `876f0be` extracts `save_claim_request()` from the route while preserving
claim-storage behaviour.

## Earlier US07 Persistence TDD Example

### RED

Commit `33ce1e4` added a failing mock-object test for claim persistence before the
required storage behaviour existed.

### GREEN

Commit `050f6f3` added the minimum pending-claim storage behaviour. Subsequent
schema-alignment commits completed the tested field mapping.

### REFACTOR

Commit `876f0be` extracted the persistence helper and the claim-storage test
continued to protect the behaviour.

The repository-recorded RED and GREEN screenshots are:

- [`us07-claim-storage-red.png`](images/us07-claim-storage-red.png);
- [`us07-claim-storage-green.png`](images/us07-claim-storage-green.png).

Both screenshots were added later in commit `3210869` and merged through PR
#58. They support the recorded sequence but are not contemporaneous commits of
the underlying code states.

Local history also preserves the implementation merge for PR #52. The following
additional screenshot links from the original evidence record remain historical
checkpoints rather than the current final result:

- [`us07-full-regression-16-passed.png`](images/us07-full-regression-16-passed.png);
- [`us07-real-database-claim-saved.png`](images/us07-real-database-claim-saved.png),
  which records a manual Flask/MySQL pending-claim check;
- [`us06-full-regression-18-passed.png`](images/us06-full-regression-18-passed.png);
  and
- [`iteration-3-final-regression-19-passed.png`](images/iteration-3-final-regression-19-passed.png).

These links preserve authentic historical evidence without treating the older
test counts as the current final regression. The 21-test result below is the
pre-user/admin baseline.

## Verified Defect Chain

```text
System testing
→ Issue #72 records the US07 defect
→ a failing regression reproduces the missing validation
→ server-side validation is added
→ the focused regression passes
→ PR #76 merges
→ repository screenshot records the manual fixed-state retest
→ the pre-user/admin baseline suite passes 21 tests
```

Local evidence supports the merge, but live Issue/Board state was not queried in
this documentation pass.

## Current Claim Regression Coverage

[`tests/test_claim_request_mock.py`](../../tests/test_claim_request_mock.py)
contains:

- `test_claim_request_stores_pending_claim_with_mock_database`;
- `test_claim_success_page_loads_with_confirmation`;
- `test_empty_claim_request_is_rejected`; and
- `test_claim_request_for_missing_item_returns_404`.

Together they verify item lookup, one parameterised INSERT, correct `item_id`,
claim fields, lowercase database status `pending`, commit, cleanup, empty-input
rejection, missing-item handling, redirect to `/claim-success/<item_id>`, and
the dedicated confirmation page content. The valid-claim test also checks that
the submitted contact and verification details are not rendered on that page.

These tests use fake or mocked database connections. They do not connect to live
MySQL.

## Historical Pre-Refinement Regression

The reproducible command is:

```bash
.venv/bin/python -m pytest -v
```

Pre-user/admin baseline result:

- **21 collected**
- **21 passed**
- **0 failed**

The tracked 15-, 16-, 18-, and 19-pass screenshots remain historical milestones.
The historical 21-pass baseline screenshot,
[`iteration-3-final-regression-21-passed.png`](images/iteration-3-final-regression-21-passed.png),
records 21 collected, 21 passed, and 0 failed.

## Current Final Regression

After the later user/admin refinement, the complete automated result is
**95 passed**. The current screenshot is
[`final-regression-95-passed.png`](images/final-regression-95-passed.png). See
[Final Testing Evidence](final-testing-evidence.md) for the current suite scope
and the boundary between automated fake/mock database tests and manual MySQL
evidence.

## Manual Evidence Boundaries

Repository screenshots record selected running-Flask/MySQL states, including a
pending claim and the Bug #72 before/fixed states. They are not browser
automation, and several expose names, contact information, verification text,
local paths, or development context. Complete the privacy review before public
submission.

The current dedicated Claim Request Submitted page is recorded in
[`final-claim-success.png`](../evidence/final-claim-success.png). The final
Iteration 3 Board evidence is recorded in
[`final-iteration-3-board.png`](../evidence/final-iteration-3-board.png). The
Board screenshot exposes GitHub account/avatar context, and the final regression
screenshot exposes local terminal identity/device context, so both require
privacy review before public embedding.
