# Week 5 Practical Reflection

## Context

Our team is currently working on Iteration 2. However, Practical 5 focuses on reflecting on Iteration 1 and applying Week 5 concepts such as good-enough design, SRP, DRY, task tracking, completed work, unfinished work, and actual velocity.

Iteration 1 was completed earlier in the project. This Week 5 reflection records what we found after reviewing the Iteration 1 work and checking the current project management process.

---

## 1. SRP and DRY Review

For Practical 5, we reviewed our project classes to check whether they satisfy the Single Responsibility Principle and the DRY principle.

### SRP Review

| Class | Main Responsibility | SRP Finding |
|---|---|---|
| User | Stores user information and allows users to submit reports or claim requests | Mostly satisfies SRP because it focuses on user-related actions |
| Item | Stores common lost and found item information | Satisfies SRP if it only manages item details and item status |
| LostItemReport | Records lost item report details | Satisfies SRP because it focuses on lost item reporting |
| FoundItemReport | Records found item report details | Satisfies SRP because it focuses on found item reporting |
| Photo | Manages uploaded item photos | Satisfies SRP because it only handles photo-related information |
| ClaimRequest | Manages claim request information and claim status | Satisfies SRP because it focuses on the claim workflow |
| Admin | Reviews claim requests and updates item status | Satisfies SRP because it focuses on administrative actions |

### SRP Findings

The design mostly follows SRP, but some responsibilities need to stay clearly separated.

The Item class should only store common item information, such as item name, report type, category, location, date, description, photo, contact information, and status.

The Item class should not be responsible for photo upload, claim review, or user account management.

The Photo class should manage uploaded photo information separately.

The ClaimRequest class should manage claim request data and claim status.

The Admin class should handle review actions, such as approving or rejecting claim requests.

---

### DRY Review

Lost item reports and found item reports share many common fields, including:

- item name
- category
- description
- location
- date
- photo
- status
- contact information

To avoid repeated design, the common fields should be stored in the Item class. LostItemReport and FoundItemReport should only store report-specific details.

### DRY Findings

Our team found three main DRY points:

1. Lost item reports and found item reports share common item fields.
2. Search and filter should use the same item data source instead of duplicated item lists.
3. Photo upload logic should not be repeated separately in multiple report classes.

### Design Decision

We decided to keep common item information in the Item class. LostItemReport and FoundItemReport keep only report-specific details. Photo upload is handled separately, and claim request logic is handled by the ClaimRequest class.

This design is good enough for the current prototype because it is clear, maintainable, and supports the main features needed for the project.

---

## 2. Task and User Story Tracking

The team used GitHub Issues and the GitHub Project Board to monitor tasks and user stories.

The board uses status columns such as:

| Status | Meaning |
|---|---|
| Todo | The task has not been started |
| In Progress | The task is currently being worked on |
| Done | The task has been completed |

Current Iteration 2 tasks are also tracked on the board with assignees and status updates. This helps the team manage ongoing work clearly.

Examples of tracked Week 5 / Iteration 2 tasks include:

- Refactor class diagram using Single Responsibility Principle
- Apply DRY principle to lost and found item design
- Create sequence diagram for claim request workflow
- Improve search and filter UI
- Add photo upload preview
- Improve claim request form UI
- Test core Iteration 2 workflow

---

## 3. Completed vs Unfinished User Stories from Iteration 1

Iteration 1 was completed earlier in the project. The planned Iteration 1 user stories were:

| User Story | Description | Status |
|---|---|---|
| US01 - Report Lost Item | Users can submit a lost item report | Completed |
| US02 - Report Found Item | Users can submit a found item report | Completed |
| US05 - View Item Details | Users can view item details | Completed |

There were no unfinished user stories from the planned Iteration 1 scope.

The following user stories were not part of Iteration 1 and were planned for Iteration 2:

| User Story | Description | Planned Iteration |
|---|---|---|
| US03 - Search Items | Users can search for lost and found items | Iteration 2 |
| US04 - Filter Items | Users can filter items by type and category | Iteration 2 |
| US06 - Upload Item Photo | Users can upload an item photo | Iteration 2 |
| US07 - Submit Claim Request | Users can submit a claim request for a found item | Iteration 2 |

---

## 4. GitHub Pages / Runnable Prototype Update

The runnable prototype was updated for each completed Iteration 1 user story.

| Completed User Story | Prototype Page | Status |
|---|---|---|
| US01 - Report Lost Item | Report Lost Item page | Updated |
| US02 - Report Found Item | Report Found Item page | Updated |
| US05 - View Item Details | Item Details page | Updated |

The prototype allows users to navigate from the homepage to the report lost item page, report found item page, browse items page, and item details page.

At the time of this Week 5 reflection, the project has already moved into Iteration 2, where search, filter, photo upload, and claim request features are being developed.

---

## 5. Actual Velocity of Iteration 1

Actual velocity is calculated by adding the estimates of all completed user stories in the iteration.

| User Story | Estimate | Status |
|---|---:|---|
| US01 - Report Lost Item | 3 person-days | Completed |
| US02 - Report Found Item | 3 person-days | Completed |
| US05 - View Item Details | 2 person-days | Completed |

### Velocity Calculation

Actual Velocity = 3 + 3 + 2

Actual Velocity = 8 person-days

### Result

The actual velocity for Iteration 1 was **8 person-days**.

Only completed Iteration 1 user stories were included in this calculation. Iteration 2 user stories were not included in the Iteration 1 velocity.

---

## Summary

Practical 5 helped the team reflect on the completed Iteration 1 work and improve the way we manage the current Iteration 2 tasks.

The main findings were:

1. The core classes mostly follow SRP.
2. Common item fields should stay in the Item class to avoid repetition.
3. Completed Iteration 1 user stories were clearly documented.
4. Current tasks are tracked using GitHub Issues and Project Board statuses.
5. The actual velocity for Iteration 1 was 8 person-days.
