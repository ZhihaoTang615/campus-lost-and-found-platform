# Development Tools and Reproducibility

## Verified Toolchain

| Tool or Technology | Purpose | Where Used | Why It Was Suitable | Repository Evidence |
|---|---|---|---|---|
| Python | Application and test runtime | Backend routes/helpers and pytest suite | One language supports the small server application and tests. | [`app.py`](../app.py), [`tests/`](../tests/), [`requirements.txt`](../requirements.txt) |
| Flask | HTTP routing, requests, redirects, templates, and test client | Application backend and route tests | Its small framework surface fits a local course prototype and provides an integrated test client. | [`app.py`](../app.py), [`tests/conftest.py`](../tests/conftest.py) |
| Jinja2 | Server-rendered HTML | Active Flask templates | It integrates with Flask and escapes displayed values by default. | [`templates/`](../templates/) |
| HTML | Page structure and forms | Active templates and documentation entry point | Native browser markup supports the required forms and navigation without a frontend build step. | [`templates/`](../templates/), [`index.html`](index.html) |
| CSS | Visual layout and responsive presentation | Active application stylesheet and documentation page | Standard CSS keeps the interface portable and build-tool free. | [`static/css/style.css`](../static/css/style.css), [`index.html`](index.html) |
| JavaScript | Small client-side UI interactions | Button ripple/confirmation interaction | Lightweight browser scripts are sufficient for the limited client-side behaviour. | [`static/js/ui-feedback.js`](../static/js/ui-feedback.js); `static/script.js` is an empty legacy file, and this is not a Node.js application |
| MySQL | Persistent `users`, `items`, and `claims` model | Local application database and manual system evidence | A relational schema enforces account and item-to-claim relationships; nullable ownership preserves only pre-enhancement legacy rows, while every current application insert is owned. | [`database.sql`](../database.sql), [`001_add_user_admin_system.sql`](../migrations/001_add_user_admin_system.sql), SQL in [`app.py`](../app.py), manual database screenshots |
| `mysql-connector-python` | Python/MySQL connection | Database connection and cursor operations | It provides a direct Python DB API for the selected MySQL database. | [`requirements.txt`](../requirements.txt), [`app.py`](../app.py) |
| `python-dotenv` | Loads local database and secret settings | Application startup | It separates local configuration from tracked source for development. | [`requirements.txt`](../requirements.txt), [`app.py`](../app.py), ignored `.env` pattern |
| Werkzeug security and upload utilities | Password hashing/checking and uploaded-filename sanitisation | Registration, login, administrator creation, and shared item-report upload path | Existing Flask-stack utilities avoid plaintext passwords and unsafe filename characters without another authentication framework. | [`app.py`](../app.py), [`create_admin.py`](../scripts/create_admin.py); upload checks still do not validate MIME, size, or collisions |
| `getpass` | Hidden administrator password input | Interactive administrator-account creation | It prevents raw password echo and avoids hard-coded administrator credentials. | [`create_admin.py`](../scripts/create_admin.py) |
| pytest | Automated regression runner | Five test modules | Its fixtures, parametrization, and Flask test-client support suit route, security, ownership, and regression checks. | [`tests/`](../tests/), [`requirements.txt`](../requirements.txt); 95 tests in the current final run |
| `unittest.mock`, `MagicMock`, `patch` | Isolates database dependencies | Item, claim, authentication, ownership, and administrator tests | Fakes and mocks make SQL/commit behaviour deterministic without requiring live MySQL. | [`test_claim_request_mock.py`](../tests/test_claim_request_mock.py), [`test_user_admin_system.py`](../tests/test_user_admin_system.py), [`mock-object-research.md`](testing/mock-object-research.md) |
| Python virtual environment | Dependency isolation | Local `.venv` test/run commands | It avoids relying on globally installed Python packages. | `.venv/` is used by the final command; `venv/pyvenv.cfg` is also tracked, creating a hygiene risk |
| Git | Distributed version history | Branches, commits, and merges | It provides local traceability and supports team branching. | Local `.git` history |
| GitHub repository | Shared remote source | Team code/document collaboration | It centralises the project and exposes repository history. | Repository remote and links in project records |
| GitHub Issues | Backlog/defect tracking | Story and bug references | Issue records can connect work to an owned task. | Planning/testing documents reference issues; several live states need confirmation |
| GitHub Projects | Iteration board | Todo/In Progress/Done tracking | A board makes iteration work state visible. | Board screenshots and iteration documents |
| GitHub Pull Requests | Integration and review workflow | Feature/fix branch merges | PRs provide an integration point and possible review record. | 26 PR-style merge commits and referenced PRs; substantive review evidence is limited |
| GitHub Pages | Intended static assessment-document hosting | `docs/` entry point and repository-recorded Pages URL | It can provide a simple static assessor navigation page. | [`index.html`](index.html) and its recorded URL; live publication is not verified here, and it is **not** Flask/MySQL deployment |
| Figma | UI design/prototyping | UI design record and exported assets | It supports shareable UI mock-ups before template implementation. | [`ui-design.md`](design/ui-design.md) records the Figma URL and exports; the live file was not independently inspected |
| VS Code | Local editing | Development workflow described in project records | It supports Python, HTML/CSS, Git, and repository editing in one environment. | Named in planning/reflection records; not independently verifiable from source |
| GitHub Desktop | Local Git workflow | Commit/branch workflow described in project records | It provides a graphical Git workflow for the team. | Named in planning/reflection records; not independently verifiable from source |

`requirements.txt` also contains packages that may be transitive dependencies.
They should not all be presented as tools directly selected or used by the team.

## Reproducible Local Setup

The reproducible steps below are consolidated from the application,
[`requirements.txt`](../requirements.txt), [`database.sql`](../database.sql),
and environment-variable names read by [`app.py`](../app.py):

1. Create a virtual environment with `python -m venv .venv`.
2. Activate it with `source .venv/bin/activate` on macOS/Linux, or the
   platform-equivalent activation command.
3. Install dependencies with `python -m pip install -r requirements.txt`.
4. Create an untracked local `.env` containing values for `APP_SECRET_KEY`,
   `DB_HOST`, `DB_USER`, `DB_PASSWORD`, and `DB_NAME`.
5. For a fresh installation, create the database and all three tables from the tracked schema, for example with
   `mysql -u <local-user> -p < database.sql`.
   For an existing US01–US07 database, back it up and run
   `migrations/001_add_user_admin_system.sql` once instead; it adds nullable
   ownership fields without deleting existing records.
6. Create an administrator when needed with `python scripts/create_admin.py`.
   The script reads `.env`, hides password input, and stores a hash.
7. Ensure `static/uploads/` exists and is writable.
8. Run `flask --app app run --debug`.
9. Run `python -m pytest -v` for the regression suite.

No public Flask application deployment is evidenced. The GitHub Pages address
serves documentation only.

Registration and login are the public application entry points. Reporting,
browsing, details, claims, My Reports, and diagnostics are authenticated routes;
the current application does not create anonymous item or claim rows.

## Reproducibility and Hygiene Gaps

- `.env.example` now provides placeholder variable names only. A real `.env`
  and a strong `APP_SECRET_KEY` must still be created locally and remain
  untracked; the application refuses requests without that secret.
- No CI workflow reproduces the test command on a clean runner.
- A large legacy `venv/` directory is tracked. Adding `venv/` to `.gitignore`
  prevents new files from being added but does not remove the existing tracked
  content.
- `static/uploads/MacBook_Charger.jpg` is tracked even though runtime upload
  contents are intended to be excluded. Existing tracked files are unaffected by
  ignore rules.
- `.venv` and the tracked `venv` report different Python generations, while the
  project does not declare a supported Python version. Current pinned package
  metadata requires Python 3.10 or newer, and the verified local environment
  uses Python 3.13.2.
- The application assumes the upload directory already exists and is writable.
- The ignore rule permits `static/uploads/.gitkeep`, but that placeholder is not
  present, so Git does not guarantee the empty directory in a clean clone.
- `database.sql` creates the database if needed, but its three table statements
  omit `IF NOT EXISTS`; it also contains no demonstration seed data. Existing
  installations must use the documented one-time migration rather than rerun
  the fresh schema over their tables.
- No Docker, container, deployment manifest, or production WSGI configuration is
  present.
- Root-level prototype HTML/JavaScript and the `.save` template backup can be
  confused with the active Flask implementation. The active system is
  `app.py`, `templates/`, and `static/`.

These gaps do not invalidate the current local 95-test run. The earlier
21-test result remains valid historical evidence for the completed US01–US07
baseline, but it is no longer the current full-suite count. Neither result
should be used to overstate clean-install or production readiness.
