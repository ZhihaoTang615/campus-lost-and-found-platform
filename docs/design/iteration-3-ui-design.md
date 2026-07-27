# Iteration 3 UI Design

## Overview

This document describes the user interface design for the selected Iteration 3 user stories.

The Iteration 3 UI focuses on improving the uploaded photo display and claim request workflow while maintaining consistency with the existing Lost and Found Platform.

---

# Uploaded Photo Workflow

## Related User Story

US06 (Carry-over) – Display Uploaded Photo

## Page Purpose

The Item Details page displays the uploaded photo of a lost or found item to help users identify the item more accurately before submitting a claim request.

## Acceptance Criteria

1. An uploaded image is displayed on the Item Details page.
2. The image uses the stored `image_path`.
3. The image has useful alt text based on the item name.
4. An item without an image displays a clear placeholder.
5. The layout remains usable on mobile screens.

### Image Position

The uploaded photo is displayed near the top of the Item Details page, above the item information such as category, report type, location, and description.

### Image Size

- Maximum width: 400px
- Responsive width: 100%
- Height adjusts automatically to maintain the original aspect ratio.
- Images use `object-fit: contain` to prevent distortion.

### Image Behaviour

| Situation | Expected Behaviour |
|------------|-------------------|
| image_path exists | Display the uploaded item photo. |
| image_path is empty | Display a placeholder with the message "No photo available for this item." |
| Image fails to load | Display a broken-image placeholder and alternative text. |

### Accessibility

The image uses meaningful alternative text:

`Photo of {{ item.item_name }}`

to improve accessibility for screen readers.

### Mobile Layout

On smaller screens, the image scales automatically to fit the available width while maintaining the aspect ratio.

---

# Claim Request Workflow

## Related User Story

US07 – Submit Claim Request

## Page Purpose

The Claim Request page allows a student to submit a request to claim a found item. The page collects the required information and submits it to the existing backend without changing the current data structure.

## Acceptance Criteria

1. Users can enter their name.
2. Users can enter their contact information.
3. Users can provide verification details for ownership verification.
4. Users can submit the claim successfully.
5. A success message is displayed after submission.
6. Invalid or incomplete input is handled safely.

## Form Fields

| Field | Type | Required |
|--------|------|----------|
| Your Name | Text | Yes |
| Contact Information | Text | Yes |
| Verification Details | Text Area | Yes |

Users can enter verification details to prove ownership of the found item.

## Buttons

- Submit Claim
- Back to Item Details

## Status

After a successful submission, the system displays a confirmation message to inform the user that the claim request has been received.

## Normal State

The page displays the selected item information together with the claim request form.

## Empty State

If the selected item cannot be found, a message is displayed indicating that the item is unavailable.

## Error State

If required fields are missing or invalid, validation messages are displayed and the form is not submitted.

## Expected User Actions

1. Open the Item Details page.
2. Click **Submit Claim Request**.
3. Enter the required information.
4. Click **Submit Claim**.
5. Receive a confirmation message.

---

## Design Summary

The Iteration 3 UI design improves the uploaded photo display and claim request workflow while remaining compatible with the existing backend implementation. The design also considers accessibility, responsive layouts, and clear feedback for normal, empty, and error states.