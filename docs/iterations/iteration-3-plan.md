# Iteration 3 Plan and Adjusted Backlog

## 1. Purpose

This document records the original Iteration 3 plan and the adjusted plan based on the results of Iteration 2.

The Iteration 3 backlog was revised using the actual Iteration 2 velocity, incomplete acceptance expectations, implementation evidence, testing results, and available team capacity.

## 2. Iteration 2 Findings

Iteration 2 originally planned the following user stories:

| User Story | Description | Original Estimate | Final Assessment |
|---|---|---:|---|
| US03 | Search Items | 2 person-days | Completed |
| US04 | Filter Items | 3 person-days | Partially completed |
| US06 | Upload Item Photo | 5 person-days | Partially completed |
| US07 | Submit Claim Request | 4 person-days | Partially completed |
| **Total** |  | **14 person-days** |  |

The accepted Iteration 2 actual velocity was:

**2 person-days**

Only fully completed user-story value was counted as completed velocity.

The remaining incomplete value was:

**12 person-days**

## 3. Incomplete Work from Iteration 2

The following acceptance expectations were not fully satisfied.

### US04 – Filter Items

The original user story required filtering by:

- Category
- Location
- Date

Category filtering was available, but the following features remained incomplete:

- Location filter
- Date filter

### US06 – Upload Item Photo

Users could select or upload an image file, but the uploaded image was not displayed in the item interface.

The remaining outcome is to retrieve and display the uploaded photo on the relevant item page.

### US07 – Submit Claim Request

A claim request interface was available, but submitted claim-request data was not stored.

The remaining outcome is to save a basic claim request with an initial Pending status.

## 4. Carry-over Work

The incomplete Iteration 2 work cannot be copied directly into Iteration 3 using the original estimates.

The remaining work must be divided into smaller, testable tasks and re-estimated.

| Carry-over Source | Remaining Task | Revised Estimate |
|---|---|---:|
| US04 | Add location filtering to the item list | 1 person-day |
| US04 | Add date filtering to the item list | 1 person-day |
| US06 | Display uploaded photos on the item details page | 1 person-day |
| US07 | Store a basic claim request with Pending status | 1 person-day |
| **Total revised carry-over work** |  | **4 person-days** |

These revised estimates describe only the remaining work. They do not repeat the full original user-story estimates.

## 5. Original Iteration 3 Plan

Before reviewing Iteration 2 performance, the original Iteration 3 plan was expected to include:

| User Story | Description |
|---|---|
| US08 | Track Claim Status |
| US09 | Review Claim Requests |
| US10 | Update Item Status |
| US11 | View My Submitted Reports |

This original plan assumed that the main Iteration 2 search, filter, photo-upload, and claim-submission features would already be complete.

That assumption was not supported by the final Iteration 2 review.

## 6. Reason for Adjusting the Plan

The original Iteration 3 plan was too large compared with the accepted Iteration 2 velocity of 2 person-days.

Starting several new claim-management features before completing the basic photo and claim-storage workflow would create additional incomplete work and technical dependencies.

The adjusted plan therefore:

- Uses the actual velocity as a realistic planning guide.
- Prioritises incomplete core workflow tasks.
- Splits carry-over work into smaller tasks.
- Selects work that can be tested independently.
- Defers lower-priority work rather than marking it as completed.
- Avoids planning more work than the team has recently demonstrated it can complete.

## 7. Adjusted Iteration 3 Goal

The goal of Iteration 3 is:

> Complete and verify two small carry-over improvements that make the item and claim workflow functional and testable.

The selected work focuses on:

1. Displaying an uploaded item photo.
2. Storing a basic claim request with Pending status.

## 8. Selected User Stories

### Selected Carry-over: US06 – Upload Item Photo

#### Task

Display uploaded photos on the item details page.

#### Estimate

**1 person-day**

#### Acceptance Criteria

- An uploaded image path or filename is available to the item details page.
- The item details page displays the uploaded image.
- A missing image does not cause the page to crash.
- The feature is verified using an automated test or documented manual evidence.

#### Primary Assignee

**Zhihao Tang**

#### Dependencies

- Existing item report and photo-upload implementation
- Item details route
- Cai's item details UI design or template update

#### Evidence Required

- Item details screenshot showing an uploaded photo
- Relevant commit
- Automated test result
- Pull Request link

---

### Selected Carry-over: US07 – Submit Claim Request

#### Task

Store a basic claim request with Pending status.

#### Estimate

**1 person-day**

#### Acceptance Criteria

- A valid claim request can be submitted.
- The submitted claim request is stored.
- A new claim request receives the status `Pending`.
- Invalid or incomplete input is handled safely.
- The behaviour is verified using an automated test.

#### Primary Assignee

**Zhihao Tang**

#### Dependencies

- Existing claim request form
- Database connection or test data layer
- Item details page
- Cai's claim form UI design

#### Evidence Required

- RED failing-test screenshot
- GREEN passing-test screenshot
- Stored claim-request evidence
- Relevant commit
- Pull Request link

## 9. Adjusted Iteration 3 Backlog

| Priority | User Story | Task | Estimate | Primary Assignee | Planned Status |
|---:|---|---|---:|---|---|
| 1 | US06 | Display uploaded photos on item details | 1 person-day | Zhihao Tang | Todo |
| 2 | US07 | Store a basic claim request with Pending status | 1 person-day | Zhihao Tang | Todo |
| 3 | US04 | Add location filtering | 1 person-day | Deferred | Deferred |
| 4 | US04 | Add date filtering | 1 person-day | Deferred | Deferred |
| 5 | US08 | Track Claim Status | Not re-estimated | Deferred | Deferred |
| 6 | US09 | Review Claim Requests | Not re-estimated | Deferred | Deferred |
| 7 | US10 | Update Item Status | Not re-estimated | Deferred | Deferred |
| 8 | US11 | View My Submitted Reports | Not re-estimated | Deferred | Deferred |

The selected implementation workload is:

**2 person-days**

This matches the accepted Iteration 2 velocity.

Documentation, UI design, testing specifications, mock-object research, project-board management, and final evidence collection support the selected work but are tracked separately from completed user-story velocity.

## 10. Deferred User Stories

The following work is deferred:

### US04 Remaining Filters

- Add location filtering
- Add date filtering

These tasks remain useful, but they are lower priority than completing the photo-display and claim-storage workflow.

### US08 – Track Claim Status

This feature depends on claim requests being stored successfully.

It cannot be completed reliably before the basic US07 storage task is finished.

### US09 – Review Claim Requests

This feature depends on stored claim requests and a working review workflow.

It is deferred until the basic claim data model is stable.

### US10 – Update Item Status

This feature depends on the claim workflow and item ownership rules.

It is deferred to avoid adding more incomplete backend logic.

### US11 – View My Submitted Reports

This feature requires a reliable current-user mechanism and report ownership data.

It is deferred until user-specific data handling is ready.

## 11. Team Responsibilities

| Team Member | Iteration 3 Responsibility |
|---|---|
| Zhihao Tang | TDD, Python tests, backend implementation, mock implementation, regression testing, and final merge |
| Jingyang Cai | Iteration 3 UI design, templates, CSS, and GitHub Pages evidence for completed UI work |
| Sihan Zhong | Iteration 3 plan, backlog, Board, test specifications, mock-object research, burn-down documentation, and final evidence |

Each GitHub Issue must have only one primary assignee.

Team members may support one another, but responsibility for each task must remain clear.

## 12. Testing Approach

The selected tasks will follow a Test-Driven Development workflow where appropriate:

1. **RED:** Create a test that fails because the required behaviour is missing.
2. **GREEN:** Implement the minimum code required to pass the test.
3. **REFACTOR:** Improve the implementation without changing the expected behaviour.

The test specifications must be based on:

- The selected User Story
- Its Acceptance Criteria
- Cai's completed UI design

Test cases must not invent fields, buttons, or behaviour that are not supported by the User Story or UI design.

## 13. Mock Object Work

Mock objects will be used where tests should not depend on a live database or real logged-in user.

Sihan Zhong will document:

- Mock-object concepts
- Fake, Stub, and Mock differences
- `unittest.mock`
- `MagicMock`
- `patch`
- Mock database examples
- Mock current-user examples
- Benefits and limitations

Zhihao Tang will implement the actual Python mock test.

## 14. Board Requirements

The Iteration 3 Board must include at least:

- Todo
- In Progress
- Done

An additional Testing column may be included.

Required labels include:

- `todo`
- `in-progress`
- `done`
- `iteration-3`
- `documentation`
- `testing`
- `backend`
- `frontend`
- `mock-object`
- `github-pages`

Each Issue must include:

- User Story
- Task description
- Acceptance criteria
- Estimate
- Assignee
- Dependencies
- Evidence required

## 15. Iteration 3 Completion Rule

A selected task may only be marked as Done when:

- Its acceptance criteria are satisfied.
- Required implementation exists.
- Relevant tests pass.
- Evidence is available.
- The GitHub Issue and Board status are updated.

Partially completed work must remain in Todo, In Progress, or Testing.

It must not be counted as completed velocity.

## 16. Expected Iteration 3 Outcome

At the end of Iteration 3, the team aims to demonstrate:

- Uploaded item photos displayed on item details.
- Basic claim requests stored with Pending status.
- Automated tests for the selected behaviour.
- TDD RED and GREEN evidence.
- At least one mock-object test.
- Updated Issues, labels, and Board.
- Final pytest regression results.
- GitHub Pull Request and GitHub Pages evidence.

## 17. Conclusion

The Iteration 3 plan was reduced and adjusted because the accepted Iteration 2 velocity was only 2 person-days.

Instead of starting all four original Iteration 3 user stories, the team will first complete two small carry-over tasks from US06 and US07.

This plan is more realistic, protects the team from creating additional unfinished work, and creates a stronger foundation for later claim-management features.
