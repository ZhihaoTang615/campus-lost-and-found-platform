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

## Summary

Overall, Week 5 helped our team improve both the technical design and the project management process. The design is now clearer, responsibilities are better separated, repeated fields are reduced, and the GitHub board gives a better view of current progress and unfinished work.
