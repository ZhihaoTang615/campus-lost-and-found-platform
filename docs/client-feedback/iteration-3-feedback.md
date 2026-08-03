# Iteration 3 Demonstration and Lecturer Feedback

## Demonstration Information

- **Demonstration date:** 3 August 2026
- **Feedback provider:** Dr Dasheng Liu
- **Feedback format:** Oral feedback after the in-class project demonstration
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

The demonstration covered the main lost-and-found workflow, including reporting
items, browsing records, searching and filtering, viewing item details,
displaying uploaded photos, and submitting a claim request.

## Lecturer Feedback

After the demonstration, Dr Dasheng Liu provided the following oral feedback:

> The final version should include a user system and an administrator system
> that can be used to view lost-and-found records.

The feedback identified two missing system-level capabilities:

1. Users should have accounts and authenticate before using the main platform
   functions.
2. An administrator should be able to view lost-and-found records through a
   protected administrator interface.

## Team Interpretation

The feedback was interpreted as a focused final scope refinement rather than a
rewrite of the original Iteration 3 plan.

The team retained the completed US01–US07 baseline and added:

- public user registration;
- secure user and administrator login;
- POST-only logout;
- authenticated-only access to reporting, browsing, item details, and claims;
- ownership links between authenticated accounts and all newly submitted item
  reports and claim requests;
- a protected **My Reports** page showing only the signed-in user's item
  reports; and
- a protected, read-only **Admin Dashboard** showing item and claim records.

The administrator system was intentionally implemented as read-only. It does
not approve, reject, delete, edit, or update claim and item records.

## Implementation Response

Zhihao Tang independently implemented the final user and administrator
refinement after the lecturer demonstration.

The implementation included:

- a new `users` database table;
- password hashing using Werkzeug;
- session-based authentication and role-based authorization;
- protected user and administrator routes;
- account ownership through `items.user_id` and `claims.user_id`;
- a non-destructive one-time migration for the existing database;
- a secure local administrator-creation script;
- role-aware navigation;
- the My Reports page;
- the read-only Admin Dashboard; and
- accessibility improvements to button, hover, visited, and focus states.

## Database Preservation

The database migration preserved the existing item and claim records.

The new ownership fields remain nullable only for records created before the
user system was introduced. Every new item report and claim request created by
the final application is linked to the authenticated account.

The administrator dashboard uses `LEFT JOIN` queries so that pre-enhancement
legacy records remain visible.

## Verification

The final refinement was verified through:

- automated registration and login tests;
- user and administrator authorization tests;
- protected-route tests;
- account ownership tests;
- My Reports account-isolation tests;
- administrator dashboard tests;
- legacy-record display tests;
- manual user and administrator workflow testing;
- template compilation;
- CSS validation; and
- full regression testing.

The final automated result was:

```text
95 passed
