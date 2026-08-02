# Final Implemented UI Specification

## 1. Design goals

The delivered Campus Lost and Found Platform uses server-rendered Jinja pages, CSS, browser forms and limited JavaScript feedback. The interface is designed to make the delivered reporting, browsing and claiming tasks clear without requiring an account.

The implemented design priorities are:

- consistent page structure and navigation;
- clear form labels, feedback and actions;
- readable item information;
- layouts that adapt to desktop, tablet and mobile widths;
- visible keyboard focus and meaningful image alternatives.

## 2. Shared navigation

The header on the delivered pages contains four primary links:

| Link | Route | Purpose |
|---|---|---|
| Home | `/` | Open the landing page. |
| Browse Items | `/items` | Browse, search and filter item records. |
| Report Lost Item | `/report-lost-item` | Open the lost-item report form. |
| Report Found Item | `/report-found-item` | Open the found-item report form. |

The current section is visually identified where applicable. Search is part of **Browse Items**, rather than a separate navigation destination. **My Reports** is not part of the implemented navigation.

## 3. Home page

The home page presents the platform title, a short explanation and three prominent actions:

- **Report a Lost Item**;
- **Report a Found Item**;
- **Browse Items**.

The implemented home page does not contain a recent-items feed.

## 4. Report Lost Item page

The lost-item form contains:

- Item Name;
- one Category selection;
- Location Lost;
- Date Lost;
- Description;
- an optional Item Photo;
- Contact Information.

All fields except the photo use browser `required` attributes. **Submit Lost Item Report** sends a multipart `POST` request to `/report-lost-item`; **Cancel** returns to the home page. After processing, the Flask route flashes a success or error message and redirects back to the lost-item form.

## 5. Report Found Item page

The found-item form mirrors the lost-item form and contains:

- Item Name;
- one Category selection;
- Location Found;
- Date Found;
- Description;
- an optional Item Photo;
- Contact Information.

All fields except the photo use browser `required` attributes. **Submit Found Item Report** sends a multipart `POST` request to `/report-found-item`; **Cancel** returns to the home page. The outcome is displayed as a flashed message after redirecting back to the form.

## 6. Browse, Search and Filter page

The `/items` page combines browsing, keyword search and filtering in one `GET` form. It provides:

- one keyword field named `q`, which searches item name, description and location;
- one Report Type selector with All Types, Lost and Found choices;
- one Category selector with All Categories, Student Card, Keys, Wallet, Electronics, Books and Other;
- **Apply Filters** and **Clear Filters** actions.

When more than one input is supplied, keyword, report type and category conditions are combined with `AND`. The current values remain selected after the request.

Results are shown as item cards containing item name, status, report type, category, location, date and a **View Details** action. When nothing matches, the page displays **No Items Found** and a **View All Items** action.

The delivered page has no pagination, left-side desktop filter panel, collapsible mobile filter menu or multi-category selection.

## 7. Item Details page

`/items/<int:item_id>` displays the selected item with:

- the uploaded image or a no-photo placeholder;
- item name;
- report type;
- category;
- status;
- location;
- date;
- description;
- contact information.

The page includes **Return to Browse Items**. The template displays **Submit Claim Request** only when `report_type` is `found`. This is a UI eligibility decision: a direct request to `/claim-request/<int:item_id>` is not independently rejected by the backend when the item is not a found report.

The general `/item-details` route redirects to `/items` so that the user selects a specific record first. A missing item ID at `/items/<int:item_id>` returns a handled 404 response.

## 8. Photo upload and display

Photo upload is optional on both report forms. The file input advertises `png`, `jpg`, `jpeg` and `gif`; the Flask helper checks the filename extension, applies `secure_filename()` and stores an accepted file under `static/uploads`. The related `image_path` is stored as `uploads/<filename>`.

There is no implemented client-side preview or remove-image action. Validation does not inspect MIME type, file size, filename collisions or malware.

On Item Details, a stored `image_path` is rendered with the alternative text `Photo of <item name>`. When `image_path` is absent, the page shows **No photo available for this item.** An `onerror` handler hides an image that fails to load and reveals the same fallback. CSS keeps both the image and placeholder responsive.

## 9. Claim Request page

The Item Details action opens `/claim-request/<int:item_id>`. Flask first queries the selected item; an unknown ID returns 404. For an existing item, the page shows a short item summary and a claim form with:

- **Your Name** (`name`);
- **Contact Information** (`contact`);
- **Claim Message** (`message`), which is stored as the claim's verification details.

The three controls use browser `required` attributes. On `POST`, Flask also strips all three values and rejects empty or whitespace-only input. Rejected input displays **All claim fields are required.**, remains on the form, and performs no claim insert or commit.

The page provides **Submit Claim** and **Return to Item Details** actions. A valid submission is stored with status `pending` and redirects to `/claim-success/<int:item_id>`.

## 10. Claim Request Submitted page

The dedicated confirmation page displays:

- **Claim Request Submitted**;
- confirmation that the request was recorded;
- **Current status: Pending**;
- **View Item Details**;
- **Browse More Items**.

Submitted contact and verification values are not repeated on this page. The page confirms storage only; it does not claim that an administrator has reviewed or approved the request.

## 11. Responsive and accessibility considerations

The delivered templates include a viewport declaration and semantic labels, headings, navigation and form controls. Primary navigation has an accessible label, current navigation links use `aria-current`, claim feedback uses a polite live region, and the success card has a labelled heading. Required controls are marked with HTML `required` attributes.

CSS provides visible `focus-visible` outlines, responsive item-grid columns, stacked navigation and full-width actions on smaller screens. Item images scale within their container. A reduced-motion media query limits transitions and animation when the browser requests reduced motion. These implementation details support accessibility but are not a claim of formal accessibility certification.

The JavaScript adds visual button feedback only; it does not implement the report or claim validation rules.

## 12. Deferred UI

The following UI remains deferred:

- US08 Track Claim Status;
- US09 Review Claim Requests;
- US10 Update Item Status;
- US11 View My Reports.

There is no delivered authentication, user-account area, administrator dashboard, claim-approval interface, email notification flow, report-editing UI or claim-status tracking UI.

## 13. Historical prototypes

The following images are retained as planning artefacts. They may show proposed layouts or interactions that do not exactly match the final implementation; the implemented specification above is authoritative.

### Search Results Prototype

![Search Results Prototype](images/search-results-prototype.png)

### Filter Panel Prototype

![Filter Panel Prototype](images/filter-panel-prototype.png)

### Photo Upload Prototype

![Photo Upload Prototype](images/photo-upload-prototype.png)

### Claim Request Prototype

![Claim Request Prototype](images/claim-request-prototype.png)

The prototypes were prepared with Figma to explore page layouts, navigation and interactions before implementation. The [historical Figma design](https://www.figma.com/design/uW6BKB70chZFDM6twSy4H9/Untitled?node-id=0-1&t=JADnl2OYpQjxtCNL-1) is not evidence that every proposed element was delivered.
