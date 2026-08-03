# Campus Lost and Found Platform

## Project Overview

The Campus Lost and Found Platform is a web-based application developed for CP3407 Advanced Software Engineering.

The system helps university students report lost items, report found items,
browse item records, search and filter listings, view item details, upload item
photos, and submit claim requests for found property. The final version also
supports user accounts, account-owned report lists, and a read-only
administrator view of lost-and-found records.

The project was developed using an iterative Agile process with GitHub Issues, GitHub Projects, branches, Pull Requests, automated testing, Test-Driven Development, mock objects, regression testing, and system testing.

---

## Delivered Baseline

The final verified system includes the following user stories:

- **US01 – Report Lost Item**
- **US02 – Report Found Item**
- **US03 – Search Items**
- **US04 – Filter Items**
- **US05 – View Item Details**
- **US06 – Upload Item Photo**
- **US07 – Submit Claim Request**

These user stories are implemented and supported by repository, testing, and system-test evidence.

## Lecturer-Requested Final Scope Refinement

After the US01-US07 baseline was completed and tested, the lecturer confirmed:

> "The final version should include a user system and an administrator system
> that can be used to view lost-and-found records."

The final implementation therefore also includes:

- public user registration with password hashing;
- user and administrator login;
- POST-only logout;
- authenticated-only access to reporting, browsing, item details, and claiming;
- required ownership links from every new item report and claim to the signed-in
  account;
- a protected **My Reports** page showing only the signed-in account's item
  reports; and
- a protected, read-only **Admin Dashboard** showing summary counts, all item
  reports, and all claim requests.

The final application requires login before any lost-and-found functionality is
used. Every new item report and claim is owned by the authenticated account.
The database ownership columns remain nullable only so records created before
the enhancement are preserved as legacy rows and remain visible to
administrators.

---

## Historical Deferral and Remaining Backlog

The Iteration 3 records correctly preserve the earlier decision to defer
US08-US11 at that point in the project. The later lecturer-requested refinement
does not rewrite that history.

- **US08 – Track Claim Status**
- **US09 – Review Claim Requests**
- **US10 – Update Item Status**

US08 and US10 remain deferred. US09 also remains deferred: the Admin Dashboard
can view claims but cannot approve, reject, delete, or update them. The
view-only portion of US11 is now delivered as **My Reports** through the later
scope refinement; report editing and management are not included.

Historical planning files contain conflicting capacity, completed-effort, and
velocity values. Those records have been preserved and require team
confirmation; they are not repeated here as settled final metrics.

---

## Main Features

Registration and login are public entry points. The final operational routes
for reporting, browsing/searching/filtering, item details, photo workflows,
claims, and My Reports require authentication; database diagnostics and the
Admin Dashboard additionally require the administrator role.

### Report Lost Items

Students can submit lost-item reports including:

- Item name
- Category
- Location
- Date
- Description
- Contact information
- Optional item photo

### Report Found Items

Students can create found-item reports using the same structured information and optionally upload a photo.

### Browse Items

Users can browse existing lost-and-found records.

### Search Items

Users can search records using keywords matched against:

- Item name
- Description
- Location

### Filter Items

Users can filter records by report type and category.

The original US04 wording also mentions location, date, and status filters.
Confirm whether US04 was formally refined to the implemented report-type and
category scope before submission.

### View Item Details

Users can open an individual item record to view detailed information.

### Upload and Display Photos

Valid image files can be uploaded with item reports and displayed on the item-details page.

Supported image extensions include:

- PNG
- JPG
- JPEG
- GIF

If no photo is available, the interface displays an appropriate fallback message.

### Submit Claim Requests

Users can submit a claim request for a found item.

Claim information includes:

- Claimant name
- Contact information
- Verification details

New claims are stored in MySQL with the initial status:

`pending`

Server-side validation prevents empty or whitespace-only claim requests from being stored.

After a valid claim is stored, the application redirects to the dedicated
**Claim Request Submitted** page. The page displays **Pending** status and
provides **View Item Details** and **Browse More Items** links.

### Registration, Login, and Logout

Public registration creates only normal user accounts. Names and email
addresses are validated, emails are normalized to lowercase, and passwords are
stored only as Werkzeug password hashes. Login uses a generic invalid-
credentials message and accepts only safe local return destinations. Logout is
available only through `POST /logout`.

### My Reports

`GET /my-reports` requires login and queries `items.user_id` using the signed-in
session's `user_id`. It lists only that account's reports, newest first, with
links to the authenticated item-details, reporting, and browsing pages.

### Read-Only Admin Dashboard

`GET /admin` requires an authenticated session whose stored role is `admin`.
It displays total item, lost-report, found-report, claim, and pending-claim
counts, followed by all item and claim records. `LEFT JOIN` queries keep
pre-enhancement rows with a nullable `user_id` visible under the legacy fallback
labels. The dashboard has no state-changing controls.

---

## Technology Stack

### Backend

- Python
- Flask

### Database

- MySQL
- `mysql-connector-python`

### Frontend

- HTML
- CSS
- Jinja templates

### Testing

- pytest
- `unittest.mock`
- `MagicMock`
- `patch`

### Development and Project Management

- Git
- GitHub
- GitHub Issues
- GitHub Projects
- GitHub Pull Requests
- GitHub Pages
- Visual Studio Code

---

## Application Architecture

The application uses a Flask-based web architecture.

Main responsibilities include:

- Flask routes handle HTTP requests and responses.
- Jinja templates render the user interface.
- MySQL stores users, item reports, and claim requests.
- Helper functions manage database persistence and image validation.
- Flask session helpers enforce login and administrator authorization.
- pytest provides automated testing.
- mock objects isolate database behaviour in selected tests.

Important implementation files include:

```text
app.py
database.sql
migrations/
scripts/create_admin.py
templates/
static/
tests/
docs/
```

## Local Setup

The application is designed to run locally with Python, Flask, and MySQL.

1. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install the pinned dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

3. Copy `.env.example` to `.env` and replace every placeholder with local
   values for `APP_SECRET_KEY`, `DB_HOST`, `DB_USER`, `DB_PASSWORD`, and
   `DB_NAME`. Do not commit credentials. `APP_SECRET_KEY` is required before
   the application will serve requests.

4. For a fresh installation, create the local database and all three tables
   from the tracked schema:

   ```bash
   mysql -u <local-user> -p < database.sql
   ```

   For a database that already contains the original `items` and `claims`
   tables, do not re-import the fresh schema. Back up the database and run the
   one-time additive migration instead:

   ```bash
   mysql -u <local-user> -p <database-name> \
     < migrations/001_add_user_admin_system.sql
   ```

   The migration creates `users`, adds nullable `user_id` columns, and adds the
   ownership foreign keys without removing existing rows.

5. After the schema or migration is installed, create an administrator account
   through the secure interactive script:

   ```bash
   python scripts/create_admin.py
   ```

   The script loads the same database environment variables, hides both
   password prompts with `getpass`, hashes the password, and inserts
   `role='admin'`. No administrator credentials are hard-coded.

6. Start the application:

   ```bash
   flask --app app run --debug
   ```

7. Run the automated regression suite:

   ```bash
   python -m pytest -v
   ```

The repository does not evidence a public deployment of the Flask/MySQL
application. The documentation page, if published, is separate from the local
application.

## Final Verification

The final regression command is:

```bash
.venv/bin/python -m pytest -v
```

The current result is **95 passed**. The original 21 tests remain green, and the
added account, authorization, ownership, and administrator tests also use fake
or mocked database connections rather than a live MySQL service.

## Security Decisions

- Passwords are hashed and are never stored in session or printed by the admin
  creation script.
- Session authentication state is limited to `user_id`, `user_name`, and
  `user_role`.
- Public registration always stores `role='user'`; administrators are created
  only through the local script.
- Reporting, browsing, item-details, claim, and personal-report routes require
  login; every new item and claim insert uses the authenticated `user_id`.
- Logged-out static access is limited to the stylesheet and UI-feedback script
  used by the Home, Login, and Register pages; uploaded item photos require
  authentication.
- Nullable ownership exists only for records that predate the account
  enhancement; the current application does not create anonymous records.
- SQL values use parameter placeholders.
- The administrator decorator trusts only the signed session role, never a
  form or URL role value.
- Login return destinations must be local paths, preventing external open
  redirects.
- Jinja automatic escaping remains enabled.
- Application and database secrets remain environment-based and untracked.

- [Assessment entry point](docs/index.html)
- [Requirements](docs/requirements.md)
- [Requirements traceability](docs/requirements-traceability.md)
- [Delivered solution](docs/delivered-solution.md)
- [Final testing evidence](docs/testing/final-testing-evidence.md)
- [TDD evidence](docs/testing/iteration-3-tdd-evidence.md)
- [System testing plan](docs/testing/system-testing-plan.md)
- [Development tools](docs/development-tools.md)
- [Iteration 3 review](docs/iterations/iteration-3-review.md)
- [Known limitations](docs/known-limitations.md)
- [Definition of Done](docs/definition-of-done.md)
