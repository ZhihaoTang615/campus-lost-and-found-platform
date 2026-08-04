# Iteration 3 Deferred Backlog

## 1. Purpose

This document is a historical record of the user stories that were originally
considered for Iteration 3 but were deferred after reviewing the team's
Iteration 2 delivery performance. Its deferral statements describe the
pre-user/admin milestone, not the current final scope.

The purpose of this adjustment was to keep Iteration 3 achievable and to prioritise completion quality, testing, TDD, regression testing, and final evidence.

---

## 2. Iteration 2 Capacity and Velocity

The Iteration 2 planning figures used for the final review are:

- Team capacity: **45 person-days**
- Estimated completed story work: **14 person-days**

The velocity ratio is:

```text
14 / 45 = 0.31
```
Therefore, the recorded Iteration 2 velocity is:

0.31

This value is used consistently in the final project documentation.

## 3. Deferred User Stories

The following user stories were originally included in the Iteration 3 backlog but were deferred:

US08
US09
US10
US11

At this pre-refinement milestone, these stories were not part of the completed
system scope. A later lecturer-requested refinement changed the current status
of the view-only portion of US11 without rewriting this historical decision.

## 4. Reason for Deferral

After the Iteration 2 velocity review, the team reduced the Iteration 3 scope.

The reduced scope allowed the team to focus on work that was already partially implemented or directly required for the final quality review.

The main priorities became:

completing US06 photo display functionality;
completing US07 claim persistence;
applying TDD to selected Iteration 3 work;
adding automated acceptance and regression tests;
researching and implementing mock-object testing;
running final regression testing;
collecting GitHub evidence;
preparing the Week 10 system test and demonstration.

This decision reduced the risk of starting additional user stories that could not be fully implemented, tested, reviewed, and evidenced before final submission.

## 5. Recorded Original Iteration 3 Scope

The implemented and verified scope at this pre-refinement milestone focused on:

US01 – Report Lost Item
US02 – Report Found Item
US03 – Search Items
US04 – Filter Items
US05 – View Item Details
US06 – Upload/Display Item Photo
US07 – Submit Claim Request

At this milestone, US08-US11 remained deferred backlog items.

## 6. Quality-Focused Iteration 3 Work

Instead of expanding the number of features, Iteration 3 prioritised software-engineering quality.

This included:

US06 photo display completion;
US06 regression testing;
US07 database persistence;
US07 initial pending claim status;
US07 mock-object testing;
RED and GREEN TDD evidence;
final pytest regression testing;
system testing preparation;
GitHub Board and evidence consistency;
GitHub Pages evidence;
final documentation review.

This approach ensured that completed functionality could be demonstrated with implementation, automated tests, Pull Requests, and repository evidence.

## 7. Recorded Deferred Story Status
User Story	Iteration 3 Status	Status at this pre-refinement milestone
US08	Deferred	Not completed
US09	Deferred	Not completed
US10	Deferred	Not completed
US11	Deferred	Not completed

The deferred stories may remain in the product backlog for future development.

They must not be moved into the completed scope unless implementation, testing, Pull Request, and evidence requirements are fully satisfied.

## 8. Documentation Consistency Rule

The confirmed final capacity basis is 15 working days for each of three members,
giving 45 person-days. The original iteration record used the following
planning values:

Capacity: 45 person-days
Completed story work: 14 person-days
Velocity: 0.31

Old or inconsistent velocity values should not be used in the final Week 10 documentation.

At this historical milestone, the documentation rule also stated:

US08-US11 were marked as deferred;
they did not appear in the milestone's completed user-story list;
evidence focused only on work verified at that time.

This historical rule is superseded for the current final system by the later
lecturer-requested refinement.

## 9. Current Final Status

| User Story | Current final status |
|---|---|
| US08 Track Claim Status | Deferred. |
| US09 Review Claim Requests | Deferred; the administrator can view claims but cannot approve or reject them. |
| US10 Update Item Status | Deferred. |
| US11 View My Reports | Historical deferral retained; the view-only portion is delivered through My Reports. Editing and management remain outside scope. |

The current final system also includes registration, login, protected
operations, ownership, and a read-only Admin Dashboard. See the
[Iteration 3 Review](iteration-3-review.md),
[Requirements Traceability](../requirements-traceability.md), and
[Delivered Solution](../delivered-solution.md).

## 10. Historical Conclusion

The Iteration 3 backlog was deliberately reduced after the Iteration 2 review.

The team prioritised completion quality over adding more partially completed features.

This allowed the pre-refinement milestone to focus on US06, US07, TDD,
mock-object testing, regression testing, system testing, and evidence while
keeping US08-US11 documented as deferred at that time.


