# Iteration 1 Plan

## 1. Iteration Objective

The objective of Iteration 1 is to build a runnable front-end prototype for the Campus Lost and Found Platform.

This iteration focuses on the most important basic services. Students should be able to report lost items, report found items, and view the details of an item.

The prototype will be used to collect initial client feedback before backend and database development begins.

---

## 2. Planned User Stories

| ID   | User Story Title  | Description                                                                                                                                                            | Priority | Estimated Effort |
| ---- | ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------: | ---------------: |
| US01 | Report Lost Item  | As a student, I want to report a lost item with its name, category, location, date, description, and contact information so that other users can help me find it.      |       10 |    3 person-days |
| US02 | Report Found Item | As a student, I want to report a found item with its name, category, location, date, description, and contact information so that the owner can identify and claim it. |       10 |    3 person-days |
| US05 | View Item Details | As a student, I want to view item details so that I can check whether an item matches the item I lost or found.                                                        |       10 |    2 person-days |

### Total Estimated Effort

```text
3 + 3 + 2 = 8 person-days
```

---

## 3. Priority Justification

US01, US02, and US05 are assigned the highest priority because they provide the basic services required for a lost-and-found platform.

* **US01 - Report Lost Item** is required so that students can submit information about missing items.
* **US02 - Report Found Item** is required so that students can share information about items they have found.
* **US05 - View Item Details** is required so that users can review the information and decide whether an item is relevant.

Search, filtering, image uploads, claim requests, and database storage will be implemented in later iterations.

---

## 4. Planned Deliverables

The planned deliverables for Iteration 1 are:

* A homepage with navigation links
* A lost-item report form
* A found-item report form
* An item-details page
* Client-side form validation
* Submission confirmation messages
* A GitHub Project Board with `Todo`, `In Progress`, and `Done` columns
* Progress screenshots
* An Iteration 1 burn-down graph
* Initial client feedback

---

## 5. Technical Scope

The Iteration 1 prototype will use:

| Technology           | Purpose                                          |
| -------------------- | ------------------------------------------------ |
| HTML                 | Build the webpage structure                      |
| JavaScript           | Handle form submission and confirmation messages |
| VS Code              | Edit source code                                 |
| Live Server          | Run and test the website locally                 |
| GitHub               | Store the repository and record version history  |
| GitHub Desktop       | Commit, pull, and push project updates           |
| GitHub Project Board | Track user-story progress                        |

The Iteration 1 prototype will not yet include a backend server or database connection.

---

## 6. Team Responsibilities

| Team Member  | Role                                                                                      | Iteration 1 Responsibilities                                                                                                              |
| ------------ | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Zhihao Tang  | Technical Lead / Full-Stack Developer / Integration Manager                               | Implement the runnable front-end prototype, test navigation, commit source code, and manage technical integration                         |
| Jingyang Cai | UI/UX Designer / Design Documentation Lead                                                | Collect UI inspiration, prepare interface design ideas, and document the planned user experience                                          |
| Sihan Zhong  | Requirements Analyst / Client Feedback Coordinator / Agile and Testing Documentation Lead | Organize user stories, document priorities and estimates, prepare acceptance tests, collect client feedback, and update iteration records |

---

## 7. Planned Workflow

The team will follow this workflow:

```text
Create user stories
→ Add stories to the GitHub Project Board
→ Move selected stories to In Progress
→ Implement and test the prototype
→ Move completed stories to Done
→ Collect client feedback
→ Record the Iteration 1 review
```

---

## 8. Acceptance Criteria

Iteration 1 will be considered complete when:

* Users can open the homepage.
* Users can navigate between the homepage, lost-item form, found-item form, and item-details page.
* Users can fill in the lost-item form.
* Users can fill in the found-item form.
* Empty required fields are blocked by browser validation.
* A success message appears after a valid form submission.
* The item-details page displays sample item information.
* All three planned user stories are moved to `Done` on the GitHub Project Board.
* Screenshots and the iteration review are added to the repository.

---

## 9. Known Limitations

The Iteration 1 version is a front-end prototype.

The following features are not included yet:

* Database storage
* Backend server
* User login
* Item search
* Item filtering
* Image upload
* Claim requests
* Admin review functions

These features will be developed in later iterations.
