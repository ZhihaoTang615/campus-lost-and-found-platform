# Iteration 3 Demonstration and Lecturer Feedback

## Demonstration Information

- **Demonstration date:** 3 August 2026
- **Feedback provider:** Dr Dasheng Liu
- **Feedback format:** Oral feedback following the in-class project demonstration
- **Project:** Campus Lost and Found Platform
- **Demonstrated solution:** Runnable Flask and MySQL web application

## Version Demonstrated

The version demonstrated in class included the completed US01–US07 baseline:

- **US01 – Report Lost Item**
- **US02 – Report Found Item**
- **US03 – Search Items**
- **US04 – Filter Items**
- **US05 – View Item Details**
- **US06 – Upload Item Photo**
- **US07 – Submit Claim Request**

The demonstration covered the main lost-and-found workflow, including:

- reporting lost and found items;
- browsing item records;
- searching and filtering records;
- viewing item details;
- displaying uploaded photos; and
- submitting claim requests.

## Lecturer Feedback

After the demonstration, Dr Dasheng Liu provided the following oral feedback:

> The final version should include a user system and an administrator system
> that can be used to view lost-and-found records.

The feedback identified two missing system-level capabilities:

1. Users should have accounts and authenticate before using the main platform functions.
2. An administrator should be able to view lost-and-found records through a protected administrator interface.

## Interpretation of the Feedback

The feedback was treated as a focused final scope refinement rather than a rewrite of the original Iteration 3 plan.

The completed US01–US07 baseline was retained, while the following capabilities were added:

- public user registration;
- secure user and administrator login;
- POST-only logout;
- authenticated-only access to reporting, browsing, item details, and claim functions;
- ownership links between authenticated accounts and all newly submitted item reports;
- ownership links between authenticated accounts and all newly submitted claim requests;
- a protected **My Reports** page showing only the signed-in account's item reports; and
- a protected, read-only **Admin Dashboard** showing item and claim records.

The administrator system was intentionally implemented as read-only. It does not approve, reject, delete, edit, or update item or claim records.

## Implementation Response

Zhihao Tang independently implemented the final user and administrator refinement after the lecturer demonstration.

The implementation included:

- a new `users` database table;
- password hashing using Werkzeug;
- session-based authentication;
- role-based authorization;
- protected user and administrator routes;
- account ownership through `items.user_id` and `claims.user_id`;
- a non-destructive one-time database migration;
- a secure local administrator-creation script;
- session-aware navigation;
- the **My Reports** page;
- the read-only **Admin Dashboard**; and
- accessibility improvements to button default, hover, visited, active, and keyboard-focus states.

## Database Preservation

The database migration preserved all existing item and claim records.

The new ownership fields remain nullable only for records created before the user system was introduced. Every new item report and claim request created through the final application is linked to the authenticated account.

The Admin Dashboard uses `LEFT JOIN` queries so that pre-enhancement legacy records remain visible to administrators.

## Verification

The final refinement was verified through:

- registration validation tests;
- login and logout tests;
- password-hashing tests;
- user and administrator authorization tests;
- protected-route tests;
- item and claim ownership tests;
- My Reports account-isolation tests;
- Admin Dashboard tests;
- legacy-record display tests;
- manual user workflow testing;
- manual administrator workflow testing;
- Jinja template compilation;
- CSS validation; and
- full automated regression testing.

The final automated regression result was:

```text
95 passed
```

## GitHub Evidence

The final refinement was developed on the following feature branch:

```text
feature/final-user-admin-system
```

It was reviewed and merged through:

- **Pull Request #87 – Add final user and administrator systems**

Pull Request #87 records the implemented user system, administrator system, database migration, access-control changes, interface improvements, and final validation results.

## Resulting Final Scope

The final delivered system consists of:

- the completed US01–US07 baseline;
- user registration;
- user and administrator login;
- POST-only logout;
- authenticated ownership of all new item reports and claims;
- the protected **My Reports** page;
- the protected, read-only **Admin Dashboard**; and
- preservation of pre-enhancement legacy database records.

The following scope remains deferred:

- **US08 – Track Claim Status**
- **US10 – Update Item Status**

**US09 – Review Claim Requests** also remains deferred because the administrator can view claim records but cannot approve, reject, delete, or update them.

The view-only part of **US11 – View My Reports** was delivered through the final lecturer-requested refinement. Report editing and management remain outside the delivered scope.

## Main Lesson Learned

The demonstration showed that completing the individual functional user stories was not sufficient by itself. The final system also required clear user identity, record ownership, and administrator visibility.

The lecturer feedback therefore resulted in a focused final refinement that improved:

- accountability;
- access control;
- database traceability;
- separation between normal users and administrators; and
- the completeness of the delivered platform.
