# Iteration 2 Actual Velocity

## 1. Purpose

This document reviews the actual completion status of the Iteration 2 user stories and calculates the actual velocity of Iteration 2 for the Campus Lost and Found Platform.

The result will be used to adjust the scope and backlog for Iteration 3.

A user story contributes to actual velocity only when its intended functionality has been fully completed and verified. Closing a GitHub issue alone does not prove that the complete user story has been delivered.

Partially completed or incomplete user stories contribute zero to the actual velocity and their remaining work must be reconsidered for Iteration 3.

---

## 2. Iteration 2 Planned User Stories

| User Story                  | Description                                   |  Original Estimate |
| --------------------------- | --------------------------------------------- | -----------------: |
| US03 - Search Items         | Search lost and found items using a keyword   |      2 person-days |
| US04 - Filter Items         | Filter items by category, location, and date  |      3 person-days |
| US06 - Upload Item Photo    | Upload a photo to help users identify an item |      5 person-days |
| US07 - Submit Claim Request | Submit a claim request for a found item       |      4 person-days |
| **Total Planned Work**      |                                               | **14 person-days** |

---

## 3. Assessment Method

The completion status was reviewed using the following evidence:

- Original user story descriptions and estimates
- Current Flask application behaviour
- Automated pytest results
- Database and route implementation
- Manual browser testing
- Uploaded-image display testing
- GitHub issues and project tasks
- Remaining unfinished workflow tasks

The existing automated test suite was also executed before the review.

```text
15 automated tests passed
0 failed
```

The existing tests provide evidence for reporting items, searching, filtering, uploading image files, and viewing item details. However, passing tests do not automatically mean that every original Iteration 2 user story has been fully completed because some original acceptance expectations are not covered by the current tests.

---

## 4. Completion Audit

### 4.1 US03 - Search Items

**User Story**

> As a student, I want to search items by keyword so that I can quickly find relevant listings.

**Original estimate:** 2 person-days  
**Final status:** Completed

The current implementation allows users to enter a search keyword on the Browse Items page.

The backend applies the keyword to:

- Item name
- Item description
- Item location

The automated tests verify:

- The Browse Items page loads successfully
- A matching keyword is added to the database query
- Item name, description, and location are searched
- Correct search parameters are used
- A search with no matching result is handled without a server error

The required keyword-search functionality has been implemented and verified.

**Velocity contribution:** 2 person-days

---

### 4.2 US04 - Filter Items

**User Story**

> As a student, I want to filter items by category, location, and date so that I can narrow down the search results.

**Original estimate:** 3 person-days  
**Final status:** Incomplete

The current implementation supports:

- Filtering by report type
- Filtering by category
- Combining a keyword search with the available filters

The existing automated tests verify:

- Report-type filtering
- Category filtering
- Combined search and filtering

However, the original user story also requires:

- A separate location filter
- A date filter

These two filtering options have not been fully implemented.

Because the complete user story has not been delivered, US04 does not contribute to the actual Iteration 2 velocity.

**Velocity contribution:** 0 person-days

**Carry-over work:**

- Add a location filter
- Add a date filter
- Update the Browse Items UI
- Add automated tests for the new filters
- Complete manual workflow testing

The remaining work should be re-estimated before it is added to the Iteration 3 backlog.

---

### 4.3 US06 - Upload Item Photo

**User Story**

> As a student, I want to upload an item photo so that other users can identify the item more easily.

**Original estimate:** 5 person-days  
**Final status:** Incomplete

The current implementation supports:

- Selecting an image in the report form
- Uploading a JPG, JPEG, PNG, or GIF file
- Rejecting an unsupported file extension
- Sanitising the uploaded filename
- Saving the uploaded file
- Storing the uploaded image path with the item report

The automated tests verify:

- A valid image file is saved
- The filename is sanitised
- The image path is stored correctly
- An unsupported file type is rejected

However, manual browser testing confirmed that the uploaded image is not displayed on the Item Details page. The user can see the item information, but there is no visible uploaded photo.

This means that the main user value of the story has not been completely delivered because other users cannot use the uploaded photo to identify the item.

Because the uploaded image is not displayed correctly, US06 does not contribute to the actual Iteration 2 velocity.

**Velocity contribution:** 0 person-days

**Carry-over work:**

- Display uploaded images on the Browse Items page
- Display uploaded images on the Item Details page
- Correct the stored image URL where necessary
- Provide a fallback image or empty state
- Test records with and without uploaded images
- Add automated tests for image display

The remaining work should be re-estimated before it is added to the Iteration 3 backlog.

---

### 4.4 US07 - Submit Claim Request

**User Story**

> As a student, I want to submit a claim request so that I can recover my lost property.

**Original estimate:** 4 person-days  
**Final status:** Incomplete

The current implementation provides:

- A Claim Request page
- A claim form for found items
- Claim form fields
- A form submission route
- A success message and redirect after submission

However, the submitted claim request is not permanently stored in the database.

The current workflow does not yet fully provide:

- A stored claim request record
- A relationship between the claim and the selected item
- An initial claim status such as `Pending`
- A way to retrieve the submitted request
- A way to review the request later
- A complete claim-management workflow

Because the submitted claim data cannot be retrieved after submission, the complete user story has not been delivered.

US07 therefore does not contribute to the actual Iteration 2 velocity.

**Velocity contribution:** 0 person-days

**Carry-over work:**

- Create or confirm the claim request database table
- Store the related item ID
- Store claimant information
- Store the reason or proof of ownership
- Set the initial status to `Pending`
- Retrieve submitted claim requests
- Add automated tests using mock database objects
- Complete end-to-end claim workflow testing

The remaining work should be re-estimated before it is added to the Iteration 3 backlog.

---

## 5. Final Velocity Calculation

| User Story                  |  Original Estimate | Final Status | Velocity Contribution |
| --------------------------- | -----------------: | ------------ | --------------------: |
| US03 - Search Items         |      2 person-days | Completed    |         2 person-days |
| US04 - Filter Items         |      3 person-days | Incomplete   |         0 person-days |
| US06 - Upload Item Photo    |      5 person-days | Incomplete   |         0 person-days |
| US07 - Submit Claim Request |      4 person-days | Incomplete   |         0 person-days |
| **Total**                   | **14 person-days** |              |     **2 person-days** |

---

## 6. Actual Velocity

```text
Iteration 2 Actual Velocity = 2 person-days
```

The team planned 14 person-days of user-story work for Iteration 2.

Only US03 fully delivered its intended functionality and satisfied the available implementation and testing evidence. Therefore, only its original estimate contributes to the actual velocity.

The completion rate based on the original estimates is:

```text
2 / 14 × 100 = 14.3%
```

Therefore:

```text
Iteration 2 completion by estimated work = approximately 14.3%
```

---

## 7. Interpretation

The low actual velocity does not mean that the team completed only two person-days of technical activity.

Significant work was completed on:

- Search and filter implementation
- Photo upload handling
- Claim Request UI
- Item Details UI
- Automated testing
- Template improvements
- Database-related code
- Bug fixing
- Testing documentation

However, velocity measures fully completed user stories rather than the total amount of technical activity.

Several stories were partially implemented but did not fully deliver their original intended user value. These stories must therefore contribute zero to the final velocity.

---

## 8. Impact on Iteration 3

The Iteration 2 actual velocity should be used as evidence when planning Iteration 3.

The team should not automatically add all new Iteration 3 user stories without considering unfinished Iteration 2 work.

The following work must be considered first:

1. Complete the location and date filters from US04.
2. Display uploaded images correctly for US06.
3. Store submitted claim requests for US07.
4. Test the complete claim workflow.
5. Use Test-Driven Development for new or remaining functionality.
6. Use mock objects to isolate database dependencies.

Because the actual velocity is only 2 person-days, the original Iteration 3 scope should be reduced or divided into smaller, independently testable tasks.

The team should prioritise the smallest high-value task that supports the claim workflow and can be completed using the Chapter 8 Red-Green-Refactor process.

---

## 9. Planning Decision

The Iteration 3 backlog should be updated using these rules:

- Unfinished Iteration 2 work receives priority.
- Work must be divided into smaller testable tasks.
- Each new feature starts with a failing automated test.
- The simplest implementation should be added to make the test pass.
- Refactoring should occur only after the tests return to green.
- Mock objects should be used where database or user dependencies make testing difficult.
- A user story is moved to `done` only when its acceptance criteria and tests are complete.

The final selected Iteration 3 workload should be based on the actual velocity and the revised estimates of the carry-over work.

---

## 10. Conclusion

Iteration 2 planned four user stories with a total estimate of 14 person-days.

After reviewing the current implementation, automated tests, browser behaviour, database workflow, and unfinished tasks:

- US03 was completed.
- US04 was incomplete.
- US06 was incomplete.
- US07 was incomplete.

The final Iteration 2 actual velocity is:

```text
2 person-days
```

This result will be used to adjust the Iteration 3 plan, reduce over-commitment, prioritise unfinished user value, and apply a proper Test-Driven Development process.
