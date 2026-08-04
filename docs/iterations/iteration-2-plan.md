# Iteration 2 Plan

## Overview

Iteration 2 focuses on improving the usability of the Campus Lost and Found Platform and introducing the first stage of the claim-request workflow.

Iteration 1 delivered a runnable front-end prototype with the basic lost-item report form, found-item report form, and Item Details page. Iteration 2 will extend the platform by adding search, filters, item-photo uploads, claim requests, database integration, and backend functionality.

## Iteration 2 Goals

The main goals of Iteration 2 are:

* Allow users to search for lost and found items.
* Allow users to filter item reports by category, location, and date.
* Allow users to upload an item photo.
* Allow users to submit a claim request.
* Store submitted report data in a MySQL database.
* Connect the front-end pages to a Flask backend.
* Improve the user interface based on Iteration 1 client feedback.
* Prepare testing records and collect new client feedback.

## Planned User Stories

Priority values are used to show the importance of each feature. A lower priority value means that the feature is more important. In this iteration, Priority 10 is the highest priority.

| ID   | Title                | User Story                                                                                                    | Priority | Estimated Effort | Iteration | Justification                                                    |
| ---- | -------------------- | ------------------------------------------------------------------------------------------------------------- | -------: | ---------------: | --------: | ---------------------------------------------------------------- |
| US03 | Search Items         | As a student, I want to search item reports using keywords so that I can find relevant items quickly.         |       10 |    2 person-days |         2 | Search helps users locate relevant reports more efficiently.     |
| US04 | Filter Items         | As a student, I want to filter items by category, location, and date so that I can narrow the search results. |       20 |    3 person-days |         2 | Filters improve usability when the number of reports increases.  |
| US06 | Upload Item Photo    | As a student, I want to upload an item photo so that other users can identify the item more accurately.       |       30 |    5 person-days |         2 | Photos reduce confusion between similar lost and found items.    |
| US07 | Submit Claim Request | As a student, I want to submit a claim request so that I can start the process of recovering an item.         |       10 |    4 person-days |         2 | A claim request connects item discovery with the return process. |

## User Story Effort Summary

| User Story                  |   Estimated Effort |
| --------------------------- | -----------------: |
| US03 – Search Items         |      2 person-days |
| US04 – Filter Items         |      3 person-days |
| US06 – Upload Item Photo    |      5 person-days |
| US07 – Submit Claim Request |      4 person-days |
| **Total**                   | **14 person-days** |

## Technical Tasks

The following technical tasks are required to support the Iteration 2 user stories.

| ID     | Technical Task                          | Estimated Effort | Responsible Member | Description                                                                       |
| ------ | --------------------------------------- | ---------------: | ------------------ | --------------------------------------------------------------------------------- |
| TASK01 | Design MySQL Database Schema            |     1 person-day | Zhihao Tang        | Design database tables for items, claims, and related data.                       |
| TASK02 | Set Up Flask Backend                    |    2 person-days | Zhihao Tang        | Create the Flask project structure, routes, and development environment.          |
| TASK03 | Connect Report Forms to Database        |    3 person-days | Zhihao Tang        | Store submitted lost-item and found-item reports in MySQL.                        |
| TASK04 | Create Dynamic Item List                |    2 person-days | Zhihao Tang        | Retrieve item reports from the database and display them dynamically.             |
| TASK05 | Connect Dynamic Item Details Page       |    2 person-days | Zhihao Tang        | Display the correct item details when a user selects an item.                     |
| TASK06 | Add Input Validation and Error Handling |     1 person-day | Zhihao Tang        | Prevent invalid submissions and provide clear error messages.                     |
| TASK07 | Perform Integration Testing             |    2 person-days | Zhihao Tang        | Test the connection between the front end, backend, database, and claim workflow. |

## UI/UX and Design Tasks

| ID       | Design Task                      | Estimated Effort | Responsible Member | Output                                     |
| -------- | -------------------------------- | ---------------: | ------------------ | ------------------------------------------ |
| DESIGN01 | Search Results Page Prototype    |     1 person-day | Jingyang Cai       | `docs/design/ui-design.md` and screenshots |
| DESIGN02 | Filter Panel Prototype           |   0.5 person-day | Jingyang Cai       | `docs/design/images/`                      |
| DESIGN03 | Photo Upload Interface Prototype |   0.5 person-day | Jingyang Cai       | `docs/design/images/`                      |
| DESIGN04 | Claim Request Page Prototype     |     1 person-day | Jingyang Cai       | `docs/design/images/`                      |
| DESIGN05 | Database ER Diagram              |     1 person-day | Jingyang Cai       | `docs/design/database-design.md`           |
| DESIGN06 | Update UI Design Documentation   |     1 person-day | Jingyang Cai       | `docs/design/ui-design.md`                 |

## Requirements, Feedback, and Testing Tasks

| ID    | Documentation Task                   | Estimated Effort | Responsible Member | Output                                            |
| ----- | ------------------------------------ | ---------------: | ------------------ | ------------------------------------------------- |
| DOC01 | Write Iteration 2 Plan               |   0.5 person-day | Sihan Zhong        | `docs/iterations/iteration-2-plan.md`             |
| DOC02 | Update Acceptance Test Cases         |     1 person-day | Sihan Zhong        | `docs/testing/acceptance-tests.md`                |
| DOC03 | Prepare Iteration 2 Burn Down Graph  |   0.5 person-day | Sihan Zhong        | `docs/iterations/images/iteration-2-burndown.png` |
| DOC04 | Collect Feedback from Three Students |     1 person-day | Sihan Zhong        | `docs/client-feedback/iteration-2-feedback.md`    |
| DOC05 | Summarize Client Feedback            |   0.5 person-day | Sihan Zhong        | `docs/client-feedback/iteration-2-feedback.md`    |
| DOC06 | Write Iteration 2 Review             |     1 person-day | Sihan Zhong        | `docs/iterations/iteration-2-review.md`           |

## Team Responsibilities

### Zhihao Tang

**Role:** Technical Lead / Full-Stack Developer

Main responsibilities:

* Design the MySQL database schema.
* Develop the Flask backend.
* Connect the report forms to the database.
* Implement search and filter functionality.
* Implement photo-upload functionality.
* Implement the claim-request workflow.
* Perform integration testing.

### Jingyang Cai

**Role:** UI/UX Designer / Design Documentation Lead

Main responsibilities:

* Create the Search Results page prototype.
* Create the filter-panel prototype.
* Create the photo-upload interface prototype.
* Create the claim-request page prototype.
* Prepare a database ER diagram based on the database schema.
* Update the UI design documentation.

### Sihan Zhong

**Role:** Requirements Analyst / Client Feedback Coordinator / Testing Lead

Main responsibilities:

* Prepare the Iteration 2 plan.
* Prepare Iteration 2 acceptance test cases.
* Prepare the Iteration 2 burn-down graph.
* Collect feedback from three students.
* Maintain Project Board evidence.
* Prepare the Iteration 2 review.

## Estimated Team Workload

| Team Member  | Main Role                                              |            Estimated Workload |
| ------------ | ------------------------------------------------------ | ----------------------------: |
| Zhihao Tang  | Technical Lead / Full-Stack Developer                  |  Approximately 13 person-days |
| Jingyang Cai | UI/UX Designer / Design Documentation Lead             |   Approximately 5 person-days |
| Sihan Zhong  | Requirements, Feedback, and Testing Documentation Lead | Approximately 4.5 person-days |

The user-story workload is estimated at **14 person-days**. The internal technical, design, and documentation tasks are estimated separately because they describe the work needed to implement and document the user-facing services.

## Iteration 2 Capacity

The final confirmed capacity basis is 15 working days for each of three team
members:

```text
3 team members × 15 working days = 45 person-days
```

The original planning draft used the following superseded calculation:

```text
3 team members × 20 working days × 0.7 velocity = 42 person-days
```

The 20-working-day duration and 0.7 factor are retained only as historical
planning evidence. They are not used in the final report or final capacity
calculation.

The planned workload is within the estimated team capacity. A small buffer has been retained for debugging, testing, and unexpected issues.

## Planned Development Order

### Stage 1 – Database and Backend Setup

1. Design the MySQL database schema.
2. Set up the Flask backend.
3. Connect the lost-item and found-item report forms to the database.

### Stage 2 – Search and Item Details

1. Create a dynamic item list.
2. Implement keyword search.
3. Implement filters.
4. Connect the dynamic Item Details page.

### Stage 3 – Photo Upload and Claim Request

1. Implement item-photo uploads.
2. Implement the claim-request workflow.
3. Add validation and error handling.
4. Perform integration testing.

## Expected Outcome

By the end of Iteration 2, users should be able to submit item reports, upload photos, search and filter items, view dynamic item details, and submit claim requests. The platform should also store report data in a MySQL database through the Flask backend.
