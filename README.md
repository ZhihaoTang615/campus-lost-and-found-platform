# Campus Lost and Found Platform

## Project Overview

The Campus Lost and Found Platform is a web-based application developed for CP3407 Advanced Software Engineering.

The system helps university students report lost items, report found items, browse item records, search and filter listings, view item details, upload item photos, and submit claim requests for found property.

The project was developed using an iterative Agile process with GitHub Issues, GitHub Projects, branches, Pull Requests, automated testing, Test-Driven Development, mock objects, regression testing, and system testing.

---

## Final Delivered Scope

The final verified system includes the following user stories:

- **US01 – Report Lost Item**
- **US02 – Report Found Item**
- **US03 – Search Items**
- **US04 – Filter Items**
- **US05 – View Item Details**
- **US06 – Upload Item Photo**
- **US07 – Submit Claim Request**

These user stories are implemented and supported by repository, testing, and system-test evidence.

---

## Deferred Backlog

The following user stories are deferred and are not part of the delivered system:

- **US08 – Track Claim Status**
- **US09 – Review Claim Requests**
- **US10 – Update Item Status**
- **US11 – View My Reports**

These stories are not part of the completed final system.

Historical planning files contain conflicting capacity, completed-effort, and
velocity values. Those records have been preserved and require team
confirmation; they are not repeated here as settled final metrics.

---

## Main Features

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
- MySQL stores item and claim data.
- Helper functions manage database persistence and image validation.
- pytest provides automated testing.
- mock objects isolate database behaviour in selected tests.

Important implementation files include:

```text
app.py
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

3. Create a local `.env` file with values for `APP_SECRET_KEY`, `DB_HOST`,
   `DB_USER`, `DB_PASSWORD`, and `DB_NAME`. Do not commit credentials.

4. Create the local database and tables from the tracked schema:

   ```bash
   mysql -u <local-user> -p < database.sql
   ```

5. Start the application:

   ```bash
   flask --app app run --debug
   ```

6. Run the automated regression suite:

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

The current result is **21 passed**. Automated database interactions use fake or
mocked connections; repository-recorded manual system evidence uses the running
Flask application and MySQL.

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
