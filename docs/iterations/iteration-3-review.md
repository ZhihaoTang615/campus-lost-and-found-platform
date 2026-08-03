# Iteration 3 Review

## Iteration Purpose

Iteration 3 focused on completing and verifying the remaining photo-display and
claim-submission work carried forward from Iteration 2.

The original Iteration 3 work included:

- completing uploaded-photo display for US06;
- completing claim-request persistence for US07;
- applying Test-Driven Development to selected functionality;
- using mock objects to isolate database behaviour;
- conducting regression and system testing;
- correcting defects discovered during testing; and
- collecting final implementation and testing evidence.

The original Iteration 3 plan recorded US08–US11 as deferred. A later
lecturer-requested refinement was completed after the in-class demonstration and
is recorded separately in this review so that the historical plan is not
rewritten.

## Planned Work

The tracked Iteration 3 plan selected:

- **US06 – Upload Item Photo:** display an uploaded photo on Item Details and
  provide a safe no-photo fallback;
- **US07 – Submit Claim Request:** store a valid claim for an existing item with
  initial status `pending`;
- focused RED–GREEN–REFACTOR evidence;
- mock-object testing;
- regression testing;
- system testing;
- defect correction; and
- final evidence documentation.

The following broader user stories were deferred during the original Iteration 3
planning:

- **US08 – Track Claim Status**
- **US09 – Review Claim Requests**
- **US10 – Update Item Status**
- **US11 – View My Reports**

## Original Iteration 3 Delivery

Current source code, tests, Git history, and repository evidence support the
following original Iteration 3 outcomes:

- uploaded-photo display on the Item Details page;
- a responsive no-photo fallback;
- claim-request persistence linked to an existing item;
- initial claim status `pending`;
- server-side rejection of empty or whitespace-only claim fields;
- a dedicated **Claim Request Submitted** page;
- visible **Pending** status after a successful submission;
- **View Item Details** and **Browse More Items** actions;
- mock-object database testing;
- regression testing; and
- selected manual Flask/MySQL workflow verification.

The completed US01–US07 baseline reached a historical regression result of:

```text
21 passed
```

This 21-test result remains valid historical evidence for the system before the
later user and administrator refinement.

## Test-Driven Development Evidence

US07 claim persistence provides the main preserved RED–GREEN–REFACTOR example.

The evidenced sequence was:

1. a failing mock-object test showed that the application did not store a claim;
2. the minimum claim-storage behaviour was implemented;
3. the focused test passed;
4. the complete regression suite remained green; and
5. claim persistence was refactored into `save_claim_request()`.

The repository records the related implementation, screenshots, commits, and
Pull Request #52.

This evidence demonstrates selected TDD practice. It does not claim that every
project feature was developed test-first.

## Bug #72 – Empty Claim Request Validation

System testing found that an empty claim request could be accepted and stored.

The evidenced defect workflow was:

1. system testing exposed the invalid behaviour;
2. the defect was recorded as Issue #72;
3. a regression test reproduced the problem;
4. server-side validation was added;
5. empty and whitespace-only fields were rejected;
6. invalid requests no longer produced an insert or commit;
7. the focused regression passed;
8. the manual workflow was retested; and
9. Pull Request #76 merged the correction.

Commit `050da84` contains both the validation change and its regression test.
Therefore, the Git history does not preserve this bug as a separate committed
RED state. The before-and-after system-test evidence is retained without
overstating the commit history.

## Iteration Demonstration and Lecturer Feedback

The completed US01–US07 system was demonstrated in class on **3 August 2026**.

After the demonstration, Dr Dasheng Liu provided the following oral feedback:

> The final version should include a user system and an administrator system
> that can be used to view lost-and-found records.

The complete feedback record is available in:

- [Iteration 3 Demonstration and Lecturer Feedback](../client-feedback/iteration-3-feedback.md)

This feedback was treated as a focused final scope refinement rather than being
retroactively added to the original Iteration 3 plan.

## Lecturer-Requested Final Refinement

Following the demonstration, the completed US01–US07 baseline was retained and
the final system was extended with:

- public user registration;
- password hashing;
- user and administrator login;
- POST-only logout;
- authenticated-only lost-and-found operations;
- role-based authorization;
- authenticated ownership for every new item report;
- authenticated ownership for every new claim request;
- a protected **My Reports** page;
- a protected, read-only **Admin Dashboard**;
- a non-destructive database migration;
- secure local administrator creation;
- legacy-record preservation; and
- improved button and keyboard-focus accessibility.

Zhihao Tang independently implemented this final refinement after the lecturer
demonstration.

The work was developed on:

```text
feature/final-user-admin-system
```

and merged through:

- **Pull Request #87 – Add final user and administrator systems**

## Final Testing Outcome

The final automated regression result after the user and administrator
refinement is:

```text
95 passed
```

The final suite includes the unchanged 21-test US01–US07 baseline plus additional
tests covering:

- registration validation;
- password hashing;
- normalized and duplicate emails;
- user and administrator login;
- generic login-failure messages;
- safe local redirects;
- POST-only logout;
- session clearing;
- protected operational routes;
- item and claim ownership;
- My Reports account isolation;
- normal-user denial from administrator routes;
- administrator summary counts;
- registered and legacy item records;
- registered and legacy claim records; and
- read-only administrator behaviour.

Automated database behaviour uses fake or mocked connections. Manual testing was
also performed using the running Flask application and local MySQL database.
These forms of testing provide different evidence and are not presented as
interchangeable.

## Database Preservation

The final database refinement added:

- a `users` table;
- nullable `items.user_id`;
- nullable `claims.user_id`; and
- ownership foreign keys.

The migration preserved all existing item and claim rows. Nullable ownership is
retained only for records created before authentication was added.

Every new item and claim created through the final application uses the
authenticated session account ID.

The Admin Dashboard uses `LEFT JOIN` queries so that legacy records remain
visible rather than being removed or incorrectly assigned to a new user.

## Final Scope Status

The final delivered baseline includes:

- **US01 – Report Lost Item**
- **US02 – Report Found Item**
- **US03 – Search Items**
- **US04 – Filter Items**
- **US05 – View Item Details**
- **US06 – Upload Item Photo**
- **US07 – Submit Claim Request**

The lecturer-requested final refinement additionally delivers:

- user registration and authentication;
- administrator authentication;
- protected operations;
- account ownership;
- a view-only **My Reports** feature; and
- a read-only **Admin Dashboard**.

The remaining deferred scope is:

- **US08 – Track Claim Status**
- **US10 – Update Item Status**

**US09 – Review Claim Requests** remains deferred because the administrator can
view claims but cannot approve, reject, delete, or update them.

The view-only portion of **US11 – View My Reports** was delivered through the
later lecturer-requested refinement. Editing and managing reports remain
outside the final scope.

US04 is implemented using report-type and category filters combined with keyword
search. The original planning wording also included location, date, and status
filters. Final treatment of that scope difference remains subject to lecturer
confirmation and is not silently rewritten in this review.

## Final Evidence

Current final evidence includes:

- [Iteration 3 lecturer feedback](../client-feedback/iteration-3-feedback.md)
- [Final 95-test regression result](../testing/images/final-regression-95-passed.png)
- [Login page](../evidence/final-login-page.png)
- [Registration page](../evidence/final-register-page.png)
- [My Reports page](../evidence/final-my-reports-page.png)
- [Admin Dashboard](../evidence/final-admin-dashboard.png)
- [Claim Request Submitted page](../evidence/final-claim-success.png)
- [Final Iteration 3 Board](../evidence/final-iteration-3-board.png)

The older 21-test screenshot remains historical baseline evidence and must not
be presented as the final complete regression result.

## Lessons Learned

- HTML `required` attributes are not a substitute for server-side validation.
- Tests should verify both visible outcomes and the absence of invalid database
  operations.
- Mock testing and live system testing answer different questions.
- Historical planning records should not be rewritten after an unplanned final
  refinement.
- Functional user stories alone do not provide user identity, data ownership, or
  administrator accountability.
- Demonstration feedback can reveal important system-level requirements that are
  not obvious from isolated feature testing.
- Evidence must clearly distinguish historical milestones from the current final
  state.

## Process Improvements

Verified project improvements include:

- server-side claim validation;
- a focused defect regression;
- preserved US07 TDD evidence;
- a dedicated claim-success page;
- user and administrator authentication;
- role-based access control;
- account-owned reports and claims;
- My Reports isolation;
- read-only administrator visibility;
- non-destructive legacy-data migration;
- expanded automated testing from 21 to 95 passing tests;
- clearer accessibility states;
- documented lecturer feedback; and
- clearer separation between original iteration delivery and later scope
  refinement.
