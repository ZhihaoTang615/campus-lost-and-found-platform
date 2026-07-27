# Iteration 3 Test Specifications

## 1. Purpose

This document defines the Iteration 3 test specifications for the Campus Lost and Found Platform.

The Iteration 3 testing scope focuses on:

- **US06 – Upload Item Photo**
- **US07 – Submit Claim Request**

The tests are based on the current Flask implementation, repository acceptance criteria, implemented UI fields, and existing automated testing structure.

No unsupported functionality is assumed.

---

## 2. Test Scope

### US06 – Upload Item Photo

US06 allows a student to upload an item photo when reporting an item and allows the uploaded image to be displayed on the related Item Details page.

The implemented photo field is:

- **Item Photo**
- HTML field name: `item-photo`
- Accepted formats: `.png`, `.jpg`, `.jpeg`, `.gif`

The photo field is optional.

If no photo is uploaded, or an image is unavailable, the Item Details page must continue to work without crashing.

### US07 – Submit Claim Request

US07 allows a student to submit a claim request for a found item.

The currently implemented claim form contains:

- **Your Name** – `name`
- **Contact Information** – `contact`
- **Claim Message** – `message`

All three fields are required by the current HTML form.

A successfully stored claim contains:

- `item_id`
- `claimant_name`
- `claimant_contact`
- `verification_details`
- initial status `pending`

The claim must remain linked to the selected item.

---

## 3. Test Specifications

| Test ID | User Story | Acceptance Criterion | UI Element | Input | Expected Behaviour | Automated Test |
|---|---|---|---|---|---|---|
| I3-T01 | US06 | An uploaded image filename or path is available to the Item Details page. | Item Photo (`item-photo`) | Valid JPG file such as `test_photo.jpg` | The image is accepted, saved in the uploads folder, and the relative image path is stored with the item record. | Yes |
| I3-T02 | US06 | The uploaded image is displayed on the relevant Item Details page. | Item image area | Item record containing a valid `image_path` | The uploaded image is rendered on the correct Item Details page. | Yes |
| I3-T03 | US06 | A missing image does not cause the page to crash. | Item image area | Item record with no image path | The page loads normally and displays `No photo available for this item.` | Yes |
| I3-T04 | US06 | An unavailable image does not cause the page to crash. | Item image area | Stored image path points to an unavailable file | The page remains usable and the no-photo placeholder is displayed. | Manual/UI candidate |
| I3-T05 | US06 | Invalid image input is handled safely. | Item Photo (`item-photo`) | Unsupported file such as `malicious-file.exe` | The upload is rejected and an invalid-image message is displayed. The report is not treated as a successful image submission. | Yes |
| I3-T06 | US06 | Existing item details continue to display correctly. | Item Details page | Existing item without a photo | Item name, category, report type, status, location, date, description, and contact information continue to display correctly. | Yes |
| I3-T07 | US07 | A valid claim request can be submitted from the claim form. | Your Name, Contact Information, Claim Message | Valid values in all required fields | The form is submitted successfully for the selected found item. | Yes |
| I3-T08 | US07 | The submitted claim request is stored successfully. | Claim form | Valid claim data | A new claim record is inserted and the database transaction is committed. | Yes |
| I3-T09 | US07 | A newly created claim request receives the initial Pending status. | Stored claim data | Valid claim submission | The newly created claim is stored with the implemented initial status value `pending`. | Yes |
| I3-T10 | US07 | The stored request is linked to the relevant item. | Submit Claim Request workflow | Submit a valid claim from a selected found item | The stored claim contains the correct selected `item_id`. | Yes |
| I3-T11 | US07 | Invalid or incomplete input is handled safely. | Your Name (`name`) | Leave the name field empty in the browser | Browser required-field validation prevents normal submission until a name is entered. | Manual |
| I3-T12 | US07 | Invalid or incomplete input is handled safely. | Contact Information (`contact`) | Leave the contact field empty in the browser | Browser required-field validation prevents normal submission until contact information is entered. | Manual |
| I3-T13 | US07 | Invalid or incomplete input is handled safely. | Claim Message (`message`) | Leave the claim message empty in the browser | Browser required-field validation prevents normal submission until a claim message is entered. | Manual |
| I3-T14 | US07 | Existing item and claim pages continue to work. | Submit Claim Request link | Open the claim page from a found item's Item Details page | The Claim Item page loads and displays the selected item's information and claim form. | Yes |
| I3-T15 | US07 | Invalid item requests are handled safely. | Claim request route | Request a claim page for an item ID that does not exist | The application returns `Item not found.` with HTTP 404. | Yes |
| I3-T16 | US07 | A valid claim request completes successfully. | Submit Claim button | Valid values in all required fields | The claim is stored, a success message is flashed, and the user is redirected to the related Item Details page. | Yes |

---

## 4. Automated Test Candidates

The main automated test candidates for Iteration 3 are:

1. Verify a valid image upload stores the expected image path.
2. Verify unsupported image extensions are rejected.
3. Verify an item without a photo still loads successfully.
4. Verify a stored image path is available to the Item Details page.
5. Verify a valid claim request is stored.
6. Verify a new claim receives the initial `pending` status.
7. Verify the claim stores the correct `item_id`.
8. Verify successful claim submission redirects to the correct Item Details page.
9. Verify a nonexistent item returns HTTP 404.
10. Verify existing US01–US05 automated tests continue to pass.

Where database behaviour is being tested, pytest fixtures or mock objects should be used where appropriate so that tests remain repeatable and independent from production data.

---

## 5. Manual UI Test Checks

### US06 Photo Workflow

1. Open a lost-item or found-item report form.
2. Select a supported image file.
3. Submit the item report.
4. Open the related Item Details page.
5. Confirm the uploaded image is displayed.
6. Repeat the workflow without uploading a photo.
7. Confirm the Item Details page still loads and displays the no-photo placeholder.
8. Attempt to upload an unsupported file extension.
9. Confirm the application rejects the invalid file.

### US07 Claim Workflow

1. Open the Item Details page for a found item.
2. Select **Submit Claim Request**.
3. Confirm the correct selected item is displayed.
4. Enter Your Name.
5. Enter Contact Information.
6. Enter a Claim Message.
7. Select **Submit Claim**.
8. Confirm the claim submission succeeds.
9. Confirm the user returns to the related Item Details page.
10. Repeat the form with each required field missing and confirm normal browser validation prevents submission.

---

## 6. Regression Requirement

After the Iteration 3 work is completed, the full pytest test suite must be executed.

The US06 and US07 changes must not break previously completed functionality:

- US01 – Report Lost Item
- US02 – Report Found Item
- US03 – Search Items
- US04 – Filter Items
- US05 – View Item Details

Any regression failure should be recorded through the GitHub Issue and Project Board bug-tracking workflow before final Iteration 3 evidence is collected.

---

## 7. Traceability

These test specifications support:

- **Issue #53 – Display uploaded photos on item details**
- **Issue #54 – Store basic claim request with Pending status**
- **Issue #57 – Write Iteration 3 test specifications**

The final evidence for these tests will be collected as part of the Iteration 3 testing and final evidence process.
