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
| MySQL | Persistent `items` and `claims` model | Local application database and manual system evidence | A relational schema suits item-to-claim relationships and parameterised queries. | [`database.sql`](../database.sql), SQL in [`app.py`](../app.py), manual database screenshots |
| `mysql-connector-python` | Python/MySQL connection | Database connection and cursor operations | It provides a direct Python DB API for the selected MySQL database. | [`requirements.txt`](../requirements.txt), [`app.py`](../app.py) |
| `python-dotenv` | Loads local database and secret settings | Application startup | It separates local configuration from tracked source for development. | [`requirements.txt`](../requirements.txt), [`app.py`](../app.py), ignored `.env` pattern |
| Werkzeug `secure_filename` | Sanitises an uploaded filename | Shared item-report upload path | It reduces unsafe filename characters using the Flask stack's existing utility. | [`app.py`](../app.py); it does not validate MIME, size, or collisions |
| pytest | Automated regression runner | All four test modules | Its fixtures and concise assertions suit Flask route regression tests. | [`tests/`](../tests/), [`requirements.txt`](../requirements.txt); 21 tests in the final run |
| `unittest.mock`, `MagicMock`, `patch` | Isolates database dependencies | Claim persistence and success-flow tests | Mocks make SQL/commit behaviour deterministic without requiring live MySQL. | [`test_claim_request_mock.py`](../tests/test_claim_request_mock.py), [`mock-object-research.md`](testing/mock-object-research.md) |
| Python virtual environment | Dependency isolation | Local `.venv` test/run commands | It avoids relying on globally installed Python packages. | `.venv/` is used by the final command; `venv/pyvenv.cfg` is also tracked, creating a hygiene risk |
| Git | Distributed version history | Branches, commits, and merges | It provides local traceability and supports team branching. | Local `.git` history |
| GitHub repository | Shared remote source | Team code/document collaboration | It centralises the project and exposes repository history. | Repository remote and links in project records |
| GitHub Issues | Backlog/defect tracking | Story and bug references | Issue records can connect work to an owned task. | Planning/testing documents reference issues; several live states need confirmation |
| GitHub Projects | Iteration board | Todo/In Progress/Done tracking | A board makes iteration work state visible. | Board screenshots and iteration documents |
| GitHub Pull Requests | Integration and review workflow | Feature/fix branch merges | PRs provide an integration point and possible review record. | 25 PR-style merge commits and referenced PRs; substantive review evidence is limited |
| GitHub Pages | Repository-recorded assessment-document hosting | `docs/` entry point and recorded Pages URL | It provides a simple static assessor navigation page from the repository. | [`index.html`](index.html) and the URL recorded there; live publication was not independently verified, and it is **not** Flask/MySQL deployment |
| Figma | UI design/prototyping | UI design record and exported assets | It supports shareable UI mock-ups before template implementation. | [`ui-design.md`](design/ui-design.md) records the Figma URL and exports; the live file was not independently inspected |
| VS Code | Local editing | Development workflow described in project records | It supports Python, HTML/CSS, Git, and repository editing in one environment. | Named in planning/reflection records; not independently verifiable from source |
| GitHub Desktop | Local Git workflow | Commit/branch workflow described in project records | It provides a graphical Git workflow for the team. | Named in planning/reflection records; not independently verifiable from source |

`requirements.txt` also contains packages that may be transitive dependencies.
They should not all be presented as tools directly selected or used by the team.

## Reproducible Local Setup

The reproducible steps below are consolidated from the application,
[`requirements.txt`](../requirements.txt), [`database.sql`](../database.sql),
and environment-variable names read by [`app.py`](../app.py):

1. Create and activate a Python virtual environment.
2. Install `requirements.txt`.
3. create a local `.env` containing the documented database variable names;
4. create the schema using `database.sql`;
5. ensure `static/uploads/` is writable;
6. run `python app.py`;
7. run `.venv/bin/python -m pytest -v` for the assessed regression suite.

No public Flask application deployment is evidenced. The GitHub Pages address
serves documentation only.

## Reproducibility and Hygiene Gaps

- No `.env.example` is present. Variable names are documented, but a
  copy-safe template would improve onboarding.
- No CI workflow reproduces the test command on a clean runner.
- A large legacy `venv/` directory is tracked. Adding `venv/` to `.gitignore`
  prevents new files from being added but does not remove the existing tracked
  content.
- `static/uploads/MacBook_Charger.jpg` is tracked even though runtime upload
  contents are intended to be excluded. Existing tracked files are unaffected by
  ignore rules.
- `.venv` and the tracked `venv` report different Python generations, while the
  project does not declare a supported Python version.
- The application assumes the upload directory already exists and is writable.
- The ignore rule permits `static/uploads/.gitkeep`, but that placeholder is not
  present, so Git does not guarantee the empty directory in a clean clone.
- `database.sql` makes database creation idempotent, but its two table statements
  omit `IF NOT EXISTS`; it also contains no demonstration seed data.
- No Docker, container, deployment manifest, or production WSGI configuration is
  present.
- Root-level prototype HTML/JavaScript and the `.save` template backup can be
  confused with the active Flask implementation. The active system is
  `app.py`, `templates/`, and `static/`.

These gaps do not invalidate the local 21-test run, but they should be disclosed
instead of overstating clean-install or production readiness.
