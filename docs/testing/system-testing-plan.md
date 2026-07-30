# System Testing Plan

## 1. Purpose

This system testing plan defines how the Campus Lost and Found Platform will be tested before and during the Week 10 demonstration.

The purpose is to verify that the final delivered system works correctly as a complete Flask and MySQL application, rather than testing individual functions in isolation.

The plan focuses on the final implemented scope:

- US01 – Report Lost Item
- US02 – Report Found Item
- US03 – Search Items
- US04 – Filter Items
- US05 – View Item Details
- US06 – Upload and Display Item Photo
- US07 – Submit Claim Request

US08–US11 are deferred and are not part of the final system testing scope.

---

## 2. Test Environment

The system will be tested using the following environment:

- Backend: Python Flask
- Database: MySQL
- Frontend: HTML, CSS and Jinja templates
- Browser: Google Chrome
- Operating System: macOS
- Testing framework: pytest
- Version control: GitHub
- Application URL: `http://127.0.0.1:5000`

The tests will be performed using the latest version of the `main` branch.

---

## 3. Preconditions

Before system testing begins:

1. The latest `main` branch must be pulled from GitHub.
2. The Python virtual environment must be activated.
3. Required Python packages must be installed.
4. MySQL must be running.
5. The application database must contain the required tables.
6. Flask must start successfully.
7. The application must be accessible through the browser.
8. The final automated regression suite must pass.

Flask can be started using:

```bash
flask --app app run --debug
```

This file records the system-test plan. It is not an execution record. See
[Final Testing Evidence](final-testing-evidence.md) for the verified automated
result and the distinction between mocked regression tests and manual MySQL
system evidence.
