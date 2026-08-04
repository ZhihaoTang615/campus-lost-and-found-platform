# Project Requirements and User Stories

## Priority and Effort Guide

The historical GitHub user-story issues use a **10/20/30 priority scale**. A
smaller recorded priority number represents greater importance: **Priority 10
is highest, Priority 20 is medium, and Priority 30 is lower**. These are the
original recorded values, not a conversion to a 1–5 scale. Priorities for
US08–US11 are not confirmed by reliable GitHub-issue evidence in this
repository and are marked for human confirmation.

Estimated effort is recorded in **person-days**. One person-day means the amount of work that one team member is expected to complete in one working day.

The table below preserves the confirmed original GitHub Issue priorities and
estimates for US01–US07. Later iteration records changed what was selected and
deferred; the final scope is stated separately below.

## User Stories

| ID | Title | User Story | Priority | Estimated Effort | Iteration | Justification |
|---|---|---|---|---:|---:|---|
| US01 | Report Lost Item | As a student, I want to report a lost item so that other users can help identify and return it. | 10 | 3 person-days | 1 | This is one of the main services of the platform and is required for the first runnable prototype. |
| US02 | Report Found Item | As a student, I want to report an item that I found so that its owner can locate it. | 10 | 3 person-days | 1 | This is a core service that complements lost-item reporting and supports the main purpose of the website. |
| US05 | View Item Details | As a student, I want to view the details of an item so that I can decide whether it matches the item I lost or found. | 10 | 2 person-days | 1 | Users need item details to understand reports. This completes the basic prototype flow. |
| US03 | Search Items | As a student, I want to search item reports using keywords so that I can find relevant items quickly. | 10 | 2 person-days | 2 | Search improves usability after the basic report and details pages are working. |
| US04 | Filter Items | As a student, I want to filter items by category, location, date, or status so that I can narrow the results. | 20 | 3 person-days | 2 | Filtering helps users manage a larger number of reports and supports the search feature. |
| US06 | Upload Item Photo | As a student, I want to upload a photo when reporting an item so that other users can identify it more accurately. | 30 | 5 person-days | 2 | Photos reduce confusion between similar items and were identified as a useful enhancement. |
| US07 | Submit Claim Request | As a student, I want to submit a claim request for an item so that I can start the return process. | 10 | 4 person-days | 2 | Claim requests are needed to move from browsing reports to recovering an item. |
| US08 | Track Claim Status | As a student, I want to track the status of my claim request so that I know whether it is pending, approved, or completed. | Confirmation required | 2 person-days | 3 | Status tracking is important once the claim process has been introduced. |
| US09 | Review Claim Requests | As an authorised reviewer, I want to review claim requests so that false or incorrect claims can be reduced. | Confirmation required | 3 person-days | 3 | Review improves trust and supports a safer item-return process. |
| US10 | Update Item Status | As an authorised user, I want to update an item status so that users can see whether an item is available, claimed, or returned. | Confirmation required | 2 person-days | 3 | Accurate status information prevents users from following up on items that are no longer available. |
| US11 | View My Reports | As a student, I want to view the reports that I submitted so that I can monitor and manage them. | Confirmation required | 2 person-days | 3 | This improves user convenience after the core features and claim workflow are complete. |

## Iteration Allocation Summary

| Iteration | Main Goal | User Stories | Total Estimated Effort |
|---|---|---|---:|
| Iteration 1 | Build a runnable prototype with the core reporting and details pages. | US01, US02, US05 | 8 person-days |
| Iteration 2 | Improve usability and introduce the first claim workflow. | US03, US04, US06, US07 | 14 person-days |
| Iteration 3 | Add tracking, review, and report-management features. | US08, US09, US10, US11 | 9 person-days |

## Lecturer-Requested Final Scope Refinement

The tables above preserve the original story and iteration records. After the
tested US01-US07 baseline, the lecturer confirmed:

> "The final version should include a user system and an administrator system
> that can be used to view lost-and-found records."

This later refinement adds the following requirements without rewriting the
historical Iteration 3 decision:

| Refinement | Acceptance requirement | Delivered behavior |
|---|---|---|
| User registration | Validate name, normalized email, an eight-character minimum password, confirmation, and duplicate email; never permit public admin registration | `GET/POST /register` creates only `role='user'` and stores a Werkzeug password hash. |
| Login and logout | Use generic invalid credentials, trusted session state, safe local return paths, and a state-changing logout method | `GET/POST /login` stores only `user_id`, `user_name`, and `user_role`; `POST /logout` clears the session. |
| Authenticated operations and ownership | Require login for reporting, browsing, details, claims, and personal records; every new report and claim must have an account owner | Protected routes redirect logged-out visitors to Login. Every application insert stores the authenticated session ID. Nullable schema fields preserve only pre-enhancement legacy rows. |
| My Reports | Require login and prevent one account from seeing another account's private report list | `GET /my-reports` filters `items` by the signed-in `user_id` and orders newest first. |
| Administrator viewing | Require the administrator role and retain legacy records | `GET /admin` is a read-only dashboard with five summary counts and all item/claim records loaded through `LEFT JOIN`. |
| Administrator creation | Avoid hard-coded credentials and public role selection | `python scripts/create_admin.py` securely prompts with `getpass`, hashes the password, and inserts `role='admin'`. |
| Existing database upgrade | Preserve all existing item and claim rows | The one-time migration creates `users` and adds nullable ownership foreign keys without removing records. |

## Final Scope Status

- **Delivered baseline:** US01 Report Lost Item, US02 Report Found Item, US03 Search
  Items, US04 Filter Items, US05 View Item Details, US06 Upload Item Photo, and
  US07 Submit Claim Request.
- **Delivered final refinement:** registration, login, POST-only logout,
  authenticated-only lost-and-found operations, required ownership for all new
  item/claim rows, the protected view-only My Reports page, and the protected
  read-only Admin Dashboard. Nullable database ownership remains only for
  pre-enhancement legacy compatibility.
- **Still deferred:** US08 Track Claim Status and US10 Update Item Status.
- **US09 boundary:** viewing claims in the Admin Dashboard is delivered, but
  reviewing, approving, rejecting, or changing claims is not. US09 remains
  deferred.
- **US11 history and refinement:** US11 was deferred during the recorded
  Iteration 3. Its view-only report-list slice was subsequently delivered by
  the lecturer-requested refinement; editing or managing reports is not
  included.
- **Implemented US04 behaviour:** report-type and category filters, including
  combination with keyword search.
- **Confirmed US04 team decision:** retain the delivered report-type/category
  filters combined with keyword search. Location, date, and status filters from
  the historical planning wording are deferred to avoid late-stage scope
  expansion and regression risk; they are not claimed as implemented.
- **Automated verification:** 95 tests pass using fake or mocked database
  connections. The 21-test result remains the historical US01-US07 baseline.

See [Requirements Traceability](requirements-traceability.md) for the final
evidence mapping and remaining evidence boundaries.
