# Project Requirements and User Stories

## Priority and Effort Guide

Priority values are used to show the relative importance of each feature. In this document, a **lower priority number means the feature is more important**. For example, Priority 1 is treated as a core feature that should be completed before Priority 5.

> Note: The instruction “Priority 10 means highest priority” conflicts with “lower priority values mean the feature is more important.” This document follows the second rule because it is internally consistent. If the lecturer confirms that Priority 10 should be the highest, reverse the priority numbers before submission.

Estimated effort is recorded in **person-days**. One person-day means the amount of work that one team member is expected to complete in one working day.

Iteration 1 contains the basic services needed for a runnable prototype. Later iterations add search, claim-management, tracking, and administration features.

## User Stories

| ID | Title | User Story | Priority | Estimated Effort | Iteration | Justification |
|---|---|---|---:|---:|---:|---|
| US01 | Report Lost Item | As a student, I want to report a lost item so that other users can help identify and return it. | 1 | 3 person-days | 1 | This is one of the main services of the platform and is required for the first runnable prototype. |
| US02 | Report Found Item | As a student, I want to report an item that I found so that its owner can locate it. | 1 | 3 person-days | 1 | This is a core service that complements lost-item reporting and supports the main purpose of the website. |
| US05 | View Item Details | As a student, I want to view the details of an item so that I can decide whether it matches the item I lost or found. | 2 | 2 person-days | 1 | Users need item details to understand reports. This completes the basic prototype flow. |
| US03 | Search Items | As a student, I want to search item reports using keywords so that I can find relevant items quickly. | 2 | 3 person-days | 2 | Search improves usability after the basic report and details pages are working. |
| US04 | Filter Items | As a student, I want to filter items by category, location, date, or status so that I can narrow the results. | 3 | 2 person-days | 2 | Filtering helps users manage a larger number of reports and supports the search feature. |
| US06 | Upload Item Photo | As a student, I want to upload a photo when reporting an item so that other users can identify it more accurately. | 3 | 2 person-days | 2 | Photos reduce confusion between similar items and were identified as a useful enhancement. |
| US07 | Submit Claim Request | As a student, I want to submit a claim request for an item so that I can start the return process. | 2 | 3 person-days | 2 | Claim requests are needed to move from browsing reports to recovering an item. |
| US08 | Track Claim Status | As a student, I want to track the status of my claim request so that I know whether it is pending, approved, or completed. | 4 | 2 person-days | 3 | Status tracking is important once the claim process has been introduced. |
| US09 | Review Claim Requests | As an authorised reviewer, I want to review claim requests so that false or incorrect claims can be reduced. | 4 | 3 person-days | 3 | Review improves trust and supports a safer item-return process. |
| US10 | Update Item Status | As an authorised user, I want to update an item status so that users can see whether an item is available, claimed, or returned. | 4 | 2 person-days | 3 | Accurate status information prevents users from following up on items that are no longer available. |
| US11 | View My Submitted Reports | As a student, I want to view the reports that I submitted so that I can monitor and manage them. | 5 | 2 person-days | 3 | This improves user convenience after the core features and claim workflow are complete. |

## Iteration Allocation Summary

| Iteration | Main Goal | User Stories | Total Estimated Effort |
|---|---|---|---:|
| Iteration 1 | Build a runnable prototype with the core reporting and details pages. | US01, US02, US05 | 8 person-days |
| Iteration 2 | Improve usability and introduce the first claim workflow. | US03, US04, US06, US07 | 10 person-days |
| Iteration 3 | Add tracking, review, and report-management features. | US08, US09, US10, US11 | 9 person-days |
