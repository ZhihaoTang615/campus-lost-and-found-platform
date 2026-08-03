# Delivered Solution

## Completed baseline

The completed and retained baseline delivers:

- US01 Report Lost Item;
- US02 Report Found Item;
- US03 Search Items;
- US04 Filter Items at the implemented report-type/category scope;
- US05 View Item Details;
- US06 Upload Item Photo; and
- US07 Submit Claim Request.

At the time of the pre-enhancement baseline, these flows did not require an
account; the iteration and testing records preserve that historical state. In
the final refined system, the same US01-US07 functionality is retained behind
login so records and claims have an authenticated owner.

## Lecturer-requested final refinement

The final version adds a focused user system and an administrator system for
viewing lost-and-found records:

- `GET/POST /register` validates and creates normal user accounts with Werkzeug
  password hashes;
- `GET/POST /login` verifies a password hash, clears prior session state, and
  stores only `user_id`, `user_name`, and `user_role`;
- `POST /logout` clears the session;
- reporting, browsing, item details, claim submission, and claim confirmation
  require login;
- every new report and claim stores the authenticated session account ID;
- `GET /my-reports` requires login and lists only the current account's item
  reports; and
- `GET /admin` requires the administrator role and shows five summary counts,
  every item report, and every claim request in a read-only dashboard.

The administrator queries use `LEFT JOIN`, so records created before the
account system remain visible under the legacy fallback labels. My Reports
deliberately does not infer ownership for those historical rows. Nullable
ownership is a migration-compatibility measure only; the current application
does not create unowned reports or claims.

## Database and administrator setup

Fresh installations use the three-table schema in [`database.sql`](../database.sql).
Existing installations run
[`migrations/001_add_user_admin_system.sql`](../migrations/001_add_user_admin_system.sql)
once after taking a backup. The migration creates `users` and adds nullable
`items.user_id` and `claims.user_id` foreign keys without removing existing
records.

Administrators are not created through public registration. After installing
the schema or migration, an operator runs:

```bash
python scripts/create_admin.py
```

The script loads the existing `.env` database configuration, hides password
input with `getpass`, validates and normalizes the account values, stores a
password hash, and inserts `role='admin'`. It contains no account credentials.

## Security boundaries

SQL values are parameterized, Jinja automatic escaping remains active, unsafe
external login return URLs are rejected, logout is POST-only, and authorization
uses the signed session role rather than form or URL data. `APP_SECRET_KEY` and
all database credentials remain environment settings; the application refuses
requests without the session secret. Operational lost-and-found routes require
login, and item/claim inserts require the authenticated session `user_id`.

## Verification and remaining scope

The complete automated regression result is **95 passed**: the unchanged
21-test US01-US07 baseline plus 74 collected refinement cases. Database behavior
is tested with fake or mocked connections and does not require live MySQL.

US08 Track Claim Status and US10 Update Item Status remain deferred. US09 also
remains deferred because the administrator can view claim records but cannot
approve, reject, delete, or update them. Historical Iteration 3 evidence that
US11 was deferred remains intact; the later refinement now delivers only its
viewing slice through My Reports, not report editing or management.

- [Requirements traceability](requirements-traceability.md)
- [Database design](design/database-design.md)
- [Historical US01-US07 testing evidence](testing/final-testing-evidence.md)
- [Iteration 3 review](iterations/iteration-3-review.md)
- [Known limitations](known-limitations.md)
- [Definition of Done](definition-of-done.md)
