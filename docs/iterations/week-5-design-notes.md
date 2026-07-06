# Week 5 Design Notes

## Focus of the Week

In Week 5, our team focused on improving the design quality and task tracking of the Campus Lost and Found Platform. Instead of trying to build a perfect system, we followed a good-enough design approach. This means we improved the current design so it is clear, maintainable, and suitable for Iteration 2 delivery.

## Good-Enough Design

Our team did not try to over-design the system. We focused on the features that are most important for Iteration 2, including search, filter, photo upload, item details, and claim request. More advanced features, such as user authentication, automatic notifications, claim history, and admin dashboard improvements, can be moved to the Next column if they cannot be completed in this iteration.

## Single Responsibility Principle

We reviewed our class diagram using the Single Responsibility Principle. Each class should have one clear responsibility. For example, the Item class stores item information, the Photo class manages uploaded image information, the ClaimRequest class manages claim submissions, and the Admin class handles claim review actions. This makes the design easier to understand and easier to update later.

## DRY Principle

We also applied the DRY principle by avoiding repeated fields in different parts of the design. Lost item reports and found item reports share common information, such as title, category, description, location, date, photo, and status. These shared fields can be stored in the Item class instead of being repeated across multiple classes.

## Refactoring

The team improved the structure of the design through refactoring. The goal of refactoring was not to add new features, but to make the existing design cleaner and easier to maintain. For example, separating item information, photo information, and claim request information helps reduce confusion and makes future changes safer.

## GitHub Issues and Project Board Tracking

We used GitHub Issues and the Project Board to track Week 5 work. Each task should have a clear title, description, assignee, label, estimate, and status. The Project Board helps the team see which tasks are in Todo, In Progress, Done, or Next.

## Unfinished Work

If a task cannot be completed during Iteration 2, it should not be ignored. Instead, the task should be moved to the Next column. This makes unfinished work visible and helps the team plan the next iteration more honestly and clearly.


## Practical 5: SRP and DRY Review

For Practical 5, our team reviewed the main classes in the Campus Lost and Found Platform to check whether they satisfy the Single Responsibility Principle and the DRY principle.

### SRP Review

The Single Responsibility Principle means that each class should have one clear responsibility. We reviewed the main classes in our project and checked whether each class had a focused purpose.

| Class | Main Responsibility | SRP Finding |
|---|---|---|
| User | Stores user information and allows users to submit lost item reports, found item reports, and claim requests | Mostly satisfies SRP because it focuses on user-related actions |
| Item | Stores common lost and found item information such as title, category, location, date, description, photo, and status | Satisfies SRP if it only manages item details and item status |
| LostItemReport | Records details of a lost item report submitted by a user | Satisfies SRP because it focuses only on the lost item reporting process |
| FoundItemReport | Records details of a found item report submitted by a user | Satisfies SRP because it focuses only on the found item reporting process |
| Photo | Manages uploaded item photo information | Satisfies SRP because it only handles photo-related information |
| ClaimRequest | Manages claim request information and claim status | Satisfies SRP because it focuses on claim submission and claim status |
| Admin | Reviews claim requests and updates item status | Satisfies SRP because it focuses on administrative review actions |

### SRP Findings

Our review found that the design mostly follows SRP, but some responsibilities need to stay clearly separated.

The Item class should only store item information. It should not be responsible for photo upload, claim review, or user account management.

The Photo class should handle uploaded image information separately.

The ClaimRequest class should manage claim request data and claim status. It should not directly manage the full item record.

The Admin class should handle review actions, such as approving or rejecting claim requests and updating item status.

### DRY Review

The DRY principle means that repeated information and repeated logic should be avoided.

In our project, lost item reports and found item reports share many common fields, including:

- item title
- category
- description
- location
- date
- photo
- status
- contact information

Instead of repeating all of these fields separately in LostItemReport and FoundItemReport, the shared fields should be stored in the Item class. LostItemReport and FoundItemReport should only store report-specific details.

### DRY Findings

Our team found three main DRY issues:

1. Lost item reports and found item reports share common item fields.
2. Search and filter should use the same item data source instead of duplicated item lists.
3. Photo upload should not be repeated separately in multiple report classes.

### Design Decision

To improve the design, we decided to keep common item information in the Item class. LostItemReport and FoundItemReport only keep report-specific details. Photo upload is handled separately by the Photo class, and claim request logic is handled by the ClaimRequest class.

This design is good enough for the current iteration because it is clear, maintainable, and supports the main features required for the prototype.
## Summary

Overall, Week 5 helped our team improve both the technical design and the project management process. The design is now clearer, responsibilities are better separated, repeated fields are reduced, and the GitHub board gives a better view of current progress and unfinished work.
