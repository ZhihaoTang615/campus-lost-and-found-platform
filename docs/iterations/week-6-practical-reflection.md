# Week 6 Practical Reflection

## Context

Our team is currently working on Iteration 2 of the Campus Lost and Found Platform. Practical 6 focuses on reflecting on Iteration 1 and using the result to adjust the Iteration 2 backlog and task tracking.

This practical also connects with the Week 6 topic of version control. Our team uses GitHub commits, branches, issues, and the project board to track changes and manage development work.

---

## 1. Actual Velocity of Iteration 1

Iteration 1 included the following completed user stories:

| User Story | Description | Estimate | Status |
|---|---|---:|---|
| US01 - Report Lost Item | Users can submit a lost item report | 3 person-days | Completed |
| US02 - Report Found Item | Users can submit a found item report | 3 person-days | Completed |
| US05 - View Item Details | Users can view item details | 2 person-days | Completed |

Actual Velocity = 3 + 3 + 2

Actual Velocity = 8 person-days

Therefore, the actual velocity of Iteration 1 was **8 person-days**.

---

## 2. SRP and DRY Review

The team reviewed the main classes using the Single Responsibility Principle and the DRY principle.

| Class | Responsibility | SRP / DRY Finding |
|---|---|---|
| User | Stores user information and submits reports or claims | Should focus only on user-related actions |
| Item | Stores common lost and found item information | Should store shared item fields to avoid duplication |
| LostItemReport | Records lost item report details | Should only contain lost-report-specific information |
| FoundItemReport | Records found item report details | Should only contain found-report-specific information |
| Photo | Handles uploaded item photo information | Keeps photo logic separate from item/report classes |
| ClaimRequest | Handles claim request information and status | Should focus only on claim workflow |
| Admin | Reviews claims and updates item status | Should focus on administrative actions |

### Findings

The design mostly satisfies SRP because each class has a clear responsibility.

The design also supports DRY because common fields such as item name, category, description, location, date, photo, status, and contact information are stored in the Item class instead of being repeated separately in LostItemReport and FoundItemReport.

---

## 3. Updating Iteration 2 Backlog Using Iteration 1 Velocity

Since the actual velocity of Iteration 1 was 8 person-days, our Iteration 2 backlog should stay close to 8 person-days. This helps the team avoid overcommitting.

The adjusted Iteration 2 backlog is:

| User Story | Description | Estimate | Priority |
|---|---|---:|---|
| US03 - Search Items | Users can search for lost and found items | 2 person-days | High |
| US04 - Filter Items | Users can filter items by report type and category | 2 person-days | High |
| US06 - Upload Item Photo | Users can upload an item photo when submitting a report | 2 person-days | High |
| US07 - Submit Claim Request | Users can submit a claim request for a found item | 2 person-days | High |

Total planned Iteration 2 workload = 8 person-days.

This matches the actual velocity from Iteration 1.

---

## 4. Iteration 2 Task and User Story Tracking

The team monitors Iteration 2 work using GitHub Issues and the GitHub Project Board.

The board uses the following status labels:

| Status | Meaning |
|---|---|
| Todo | The task has not been started |
| In Progress | The task is currently being worked on |
| Done | The task has been completed |

Examples of Iteration 2 tasks include:

| Task | Related User Story | Status |
|---|---|---|
| Create search results page prototype | US03 | Done |
| Implement search item logic | US03 | Done / In Progress |
| Improve search and filter UI | US03 / US04 | Done / In Progress |
| Add photo upload field to report forms | US06 | Done |
| Add uploaded photo preview display | US06 | Todo / In Progress |
| Improve item details page | US05 / US07 | In Progress |
| Improve claim request form UI | US07 | In Progress |
| Test core Iteration 2 workflow | US03 / US04 / US06 / US07 | Todo |

---

## 5. Completed vs Unfinished User Stories

### Completed / Partially Completed User Stories

| User Story | Status | Evidence |
|---|---|---|
| US03 - Search Items | Completed / In Progress | Browse Items page includes search input and item results |
| US04 - Filter Items | Completed / In Progress | Browse Items page includes report type and category filters |
| US06 - Upload Item Photo | Partially Completed | Report Lost Item and Report Found Item pages include photo upload fields |
| US07 - Submit Claim Request | In Progress | Claim request form UI is being improved |

### Unfinished Work

The following work still needs to be completed or improved:

| Unfinished Work | Reason | Next Action |
|---|---|---|
| Photo preview display | Upload field exists, but preview display still needs improvement | Continue in Iteration 2 |
| Claim request workflow | UI exists / planned, but full workflow needs testing | Continue implementation and testing |
| Full admin review dashboard | Advanced feature beyond current core scope | Move to Next if not completed |
| Automatic notification | Advanced feature | Move to Next if not completed |

---

## 6. GitHub Pages / Runnable Prototype Update

The runnable prototype has been updated for completed or partially completed Iteration 2 user stories.

| User Story | Prototype Page | Status |
|---|---|---|
| US03 - Search Items | Browse Items page | Updated |
| US04 - Filter Items | Browse Items page | Updated |
| US06 - Upload Item Photo | Report Lost Item and Report Found Item pages | Updated |
| US07 - Submit Claim Request | Claim Request page / form | In Progress |

The current dynamic version runs through Flask. The updated prototype pages are documented with screenshots in the repository.

---

## 7. Version Control and Build Notes

The team used GitHub for version control. Feature work was committed with meaningful commit messages and merged into the main branch after review.

Examples of version control practice:

- Use feature branches for separate work.
- Commit changes with clear messages.
- Merge completed work back into main.
- Use GitHub Issues and Project Board to track progress.
- Keep documentation and screenshots in the repository.

The project can be run locally using Flask. The basic setup is documented in the repository through files such as README.md and requirements.txt.

---

## Summary

In Practical 6, our team used the actual velocity from Iteration 1 to adjust the Iteration 2 backlog. Since Iteration 1 velocity was 8 person-days, Iteration 2 was planned around 8 person-days of work.

The team also reviewed SRP and DRY, monitored Iteration 2 tasks through GitHub Issues and Project Board labels, documented completed and unfinished user stories, and updated the runnable prototype for completed user stories.
