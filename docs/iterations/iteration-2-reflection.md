# Iteration 2 Reflection

## 1. Purpose

This document reflects on the planning, implementation, testing, and outcomes of Iteration 2 for the Campus Lost and Found Platform.

The purpose of this reflection is to identify what was completed, what remained unfinished, what problems affected the iteration, and what changes should be made for Iteration 3.

The reflection is also used together with the actual Iteration 2 velocity to reduce over-commitment and support a proper Test-Driven Development process in Iteration 3.

---

## 2. Iteration 2 Planned User Stories

Iteration 2 originally included the following user stories:

| User Story                  | Description                                   |  Original Estimate |
| --------------------------- | --------------------------------------------- | -----------------: |
| US03 - Search Items         | Search lost and found items using a keyword   |      2 person-days |
| US04 - Filter Items         | Filter items by category, location, and date  |      3 person-days |
| US06 - Upload Item Photo    | Upload a photo to help users identify an item |      5 person-days |
| US07 - Submit Claim Request | Submit a claim request for a found item       |      4 person-days |
| **Total**                   |                                               | **14 person-days** |

---

## 3. Final Completion Status

| User Story                  | Final Status | Main Reason                                              |
| --------------------------- | ------------ | -------------------------------------------------------- |
| US03 - Search Items         | Completed    | Keyword search was implemented and tested                |
| US04 - Filter Items         | Incomplete   | Location and date filters were not completed             |
| US06 - Upload Item Photo    | Incomplete   | Uploaded images were saved but not displayed correctly   |
| US07 - Submit Claim Request | Incomplete   | Submitted claim requests were not stored in the database |

The final actual velocity of Iteration 2 was:

```text
2 person-days
```

Only US03 fully delivered its intended user value.

---

## 4. What Went Well

### 4.1 Search Functionality Was Completed

The keyword-search feature was successfully implemented.

Users can search across:

- Item name
- Item description
- Item location

The automated tests also confirmed that:

- The Browse Items page loads correctly
- Matching keywords are added to the SQL query
- Search parameters are passed correctly
- Searches with no matching results do not crash the system

This made US03 the only fully completed Iteration 2 user story.

---

### 4.2 Automated Testing Was Introduced

The team added a pytest-based automated test suite.

The final Week 7 test suite contained:

```text
15 automated tests
15 passed
0 failed
```

The tests covered:

- Report Lost Item
- Report Found Item
- Search Items
- Filter Items
- View Item Details
- File upload validation
- Database query parameters
- HTTP redirects
- Missing-item handling

This provided a stable testing baseline before Iteration 3.

---

### 4.3 Real Defects Were Found Through Testing

Automated testing identified real defects in the application.

One defect was an incorrect Flask endpoint in the Item Details template. The template used an incorrect claim endpoint, which prevented the page from loading correctly.

Another defect was a Jinja template syntax regression on the Browse Items page. This caused several search and filter tests to fail.

The defects were corrected, and the complete test suite was run again successfully.

This demonstrated that automated tests can protect the system against regression errors.

---

### 4.4 Test Data Was Isolated from the Real System

The automated tests used:

- A Flask test client
- Fake database connections
- Fake database cursors
- Temporary upload directories
- Controlled sample data

This prevented tests from modifying the real MySQL database or storing test images in the real upload directory.

This approach supports safer and repeatable testing.

---

### 4.5 The User Interface Became More Consistent

The main pages were updated to use a more consistent layout and navigation structure.

The following pages shared a consistent visual style:

- Home
- Browse Items
- Report Lost Item
- Report Found Item
- Item Details
- Claim Request

The navigation and page structure became easier to understand and demonstrate.

---

## 5. Problems Encountered

### 5.1 The Iteration Scope Was Too Large

Iteration 2 planned 14 person-days of user-story work.

However, only 2 person-days of fully completed user-story value were delivered.

The team attempted to work on several large features at the same time:

- Search
- Filter
- Photo upload
- Photo display
- Claim Request UI
- Claim Request backend
- Automated testing
- UI improvements
- Documentation

This created too much work for one iteration and made it difficult to complete full end-to-end user stories.

---

### 5.2 Some Stories Were Closed Too Early

Several GitHub user-story issues were closed before all of their intended functionality was complete.

Closing an issue did not always mean that:

- All acceptance criteria were satisfied
- The complete workflow worked
- Automated tests existed
- Manual testing was complete
- The intended user value had been delivered

In Iteration 3, a user story should only move to `done` when its acceptance criteria, implementation, testing, and evidence are complete.

---

### 5.3 US04 Did Not Match Its Original Scope

US04 originally required filtering by:

- Category
- Location
- Date

The implemented system supported:

- Report type
- Category

The separate location and date filters were not completed.

The team implemented useful filter functionality, but the full original user story was not delivered.

This shows that the team needs to compare implementation work with the original user-story wording before marking a story as complete.

---

### 5.4 Uploaded Images Were Not Displayed

US06 successfully supported:

- Image selection
- File extension validation
- Filename sanitisation
- File saving
- Image-path storage

However, manual testing confirmed that the uploaded image was not displayed on the Item Details page.

The system stored the image information, but users could not see the image and use it to identify the item.

This meant that the main user value of US06 was incomplete.

---

### 5.5 Claim Requests Were Not Stored

US07 provided:

- A Claim Request page
- A form
- A POST route
- A success message
- A redirect

However, the submitted claim request was not inserted into the database.

The system did not yet provide:

- A persistent claim record
- An initial `Pending` status
- Retrieval of submitted claims
- Claim review
- Claim approval or rejection
- Claim-status tracking

The feature looked usable from the interface, but the complete backend workflow was missing.

---

### 5.6 Testing Was Added After Most Implementation

The Week 7 tests were mainly added after the related functionality had already been implemented.

This was automated testing, but it was not a complete Test-Driven Development process.

A proper TDD process should be:

```text
RED
Write and run a failing test.

GREEN
Write the simplest code required to make the test pass.

REFACTOR
Improve the code while keeping the tests passing.
```

Iteration 3 will use this sequence before implementing production functionality.

---

### 5.7 Daily Remaining Work Was Not Recorded Consistently

The team did not consistently record the remaining person-days at the end of every working day.

This makes it harder to create a completely accurate Iteration 2 burn-down graph.

The actual burn-down data will need to be reconstructed using:

- GitHub issue dates
- Commit dates
- Pull Request dates
- Task completion records
- Project Board status updates

Iteration 3 should record remaining work more consistently.

---

## 6. Testing Results

Before Iteration 3, the complete existing test suite was run again.

The result was:

```text
15 passed
0 failed
```

This creates a stable regression-testing baseline.

The Iteration 3 tests must not break the existing 15 tests.

New tests should be added for selected Iteration 3 work, including mock-object testing where database or user dependencies need to be isolated.

---

## 7. Technical Debt

The following technical debt remains after Iteration 2:

1. Add location filtering.
2. Add date filtering.
3. Display uploaded images on Browse Items.
4. Display uploaded images on Item Details.
5. Add a fallback state when no image is available.
6. Store claim requests in the database.
7. Set the initial claim status to `Pending`.
8. Retrieve submitted claim requests.
9. Add claim review functionality.
10. Add item-status update logic.
11. Test the complete claim workflow.
12. Improve separation between route logic and database access.
13. Add mock-object tests for database dependencies.

These items must be prioritised rather than hidden by marking incomplete stories as complete.

---

## 8. Lessons Learned

### 8.1 Complete User Value Matters More Than Partial Code

A feature should not be considered complete only because a page, route, or database field exists.

The complete user workflow must work.

For example:

- Uploading a photo is not enough when the photo cannot be viewed.
- Submitting a claim form is not enough when the claim is not stored.
- Adding some filter controls is not enough when the original required filters are missing.

---

### 8.2 Acceptance Criteria Must Be Checked Before Closing Issues

Before moving a user story to `done`, the team must confirm:

- All acceptance criteria are satisfied
- The UI works
- The backend works
- Data is stored correctly
- Tests pass
- Evidence is available
- GitHub Pages are updated

---

### 8.3 Smaller Tasks Are Easier to Finish

Large stories should be divided into smaller tasks.

For example, US07 can be divided into:

1. Create the claim database structure.
2. Write a failing test for claim storage.
3. Store a claim with `Pending` status.
4. Retrieve the stored claim.
5. Display the claim.
6. Add review functionality later.

This approach is more suitable for TDD and makes progress easier to measure.

---

### 8.4 Tests Should Be Written Before Production Code

Iteration 3 will use the Chapter 8 process:

```text
User Story and UI Design
→ Test Specification
→ Failing Test
→ Minimum Implementation
→ Passing Test
→ Refactor
```

The team will capture both RED and GREEN evidence.

---

### 8.5 External Dependencies Should Be Mocked

Database access makes tests slower and more difficult to control.

Iteration 3 should use Python `unittest.mock`, including:

```python
MagicMock
patch
```

Mock objects can simulate database results or a current user and verify whether methods are called with the correct parameters.

This supports isolated, repeatable, and faster tests.

---

## 9. Changes for Iteration 3

The team will make the following changes:

### 9.1 Reduce the Planned Scope

The Iteration 2 actual velocity was only 2 person-days.

Therefore, Iteration 3 should not automatically include all remaining and new user stories.

The team will select a small amount of high-priority work and divide it into testable tasks.

---

### 9.2 Prioritise Carry-over Work

Incomplete Iteration 2 work will be reviewed before adding new stories.

Priority areas include:

1. Claim request database storage
2. Uploaded-image display
3. Missing filter functionality

The final selection must be based on value, dependencies, and revised estimates.

---

### 9.3 Use UI Designs and User Stories as Test Specifications

Before writing code, the team will define:

- User Story
- Acceptance Criteria
- UI elements
- Inputs
- Expected behaviour
- Automated test name

The UI and User Story will become the specification for each Iteration 3 test.

---

### 9.4 Follow Red-Green-Refactor

Every selected development task will follow:

```text
RED
Create a failing automated test.

GREEN
Write the simplest production code that makes the test pass.

REFACTOR
Clean up the implementation without adding new functionality.
```

Chapter 8 describes this cycle as the core TDD workflow. :contentReference[oaicite:0]{index=0}

---

### 9.5 Use Mock Objects

The team will research and use Python `unittest.mock`.

The project will attempt to mock one or more of these dependencies:

- Database connection
- Database cursor
- Claim repository
- Current user
- Admin user

The mock tests must verify method calls, arguments, return values, and database commit behaviour.

---

### 9.6 Improve Task Monitoring

Every Iteration 3 task will have:

- One owner
- One Issue
- One branch
- An estimate
- Acceptance criteria
- A status label
- Required evidence

The required labels are:

```text
todo
in-progress
done
```

The team may also use a `testing` workflow stage before moving a task to `done`.

---

### 9.7 Update GitHub Pages Only After Completion

GitHub Pages will only show a story as completed when:

- The feature is implemented
- Acceptance criteria are satisfied
- Tests pass
- Evidence is available
- The Pull Request has been merged

---

## 10. Conclusion

Iteration 2 produced useful technical progress, including keyword search, image-upload handling, claim-request UI, interface improvements, and an automated pytest suite.

However, only US03 fully delivered its intended user value.

The main problems were:

- Excessive iteration scope
- Partial completion of multiple stories
- Issues being closed too early
- Missing image display
- Missing claim storage
- Testing being added after implementation
- Inconsistent daily progress recording

Iteration 3 will respond by:

- Reducing scope
- Prioritising unfinished value
- Using velocity for backlog planning
- Writing test specifications from UI designs and user stories
- Following Red-Green-Refactor
- Using mock objects
- Requiring complete evidence before marking work as done
