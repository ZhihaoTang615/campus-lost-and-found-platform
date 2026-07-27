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
- **US06 – Upload and Display Item Photo**
- **US07 – Submit Claim Request**

These user stories are implemented and supported by repository, testing, and system-test evidence.

---

## Deferred Backlog

The following user stories were originally considered for Iteration 3 but were deferred after reviewing Iteration 2 delivery performance:

- **US08 – Track Claim Status**
- **US09 – Review Claim Requests**
- **US10 – Update Item Status**
- **US11 – View My Submitted Reports**

These stories are not part of the completed final system.

The team deliberately reduced the Iteration 3 scope so that completed functionality could receive stronger testing, TDD, regression testing, system testing, and final evidence.

Iteration 2 planning figures:

- Team capacity: **45 person-days**
- Completed estimated story work: **14 person-days**
- Velocity ratio: **0.31**

See:

`docs/iterations/iteration-3-deferred-backlog.md`

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
