# Iteration 3 US06–US07 UI Design — Historical Pre-Refinement Record

## Overview

At the recorded pre-user/admin Iteration 3 milestone, the project completed the
US06 uploaded-photo display and US07 claim-request workflow. It also added the
Bug #72 empty-claim safeguard and the dedicated claim-confirmation page. This
document describes that implemented historical milestone rather than a proposed
interface; it is not the current final UI specification.

## US06 uploaded-photo display

The Item Details template reads the selected item's `image_path`.

| State | Delivered presentation |
|---|---|
| `image_path` is present and the file loads | Display the item image with `alt="Photo of <item name>"`. |
| `image_path` is absent | Display **No photo available for this item.** |
| The image fails to load | The `onerror` handler hides the failed image and reveals the no-photo placeholder. |

CSS presents the image in a responsive container and allows it to scale to the available width on smaller screens. The same responsive layout is used for lost and found item records.

The reporting forms accept an optional photo. The allowed filename extensions are `png`, `jpg`, `jpeg` and `gif`; `secure_filename()` is applied before storage in `static/uploads`, and the item row stores `uploads/<filename>` in `image_path`. The delivered interface has no client-side image preview or remove-image action.

## US07 Claim Request page

The Item Details template displays **Submit Claim Request** only for an item whose `report_type` is `found`. The link opens `/claim-request/<int:item_id>`.

Flask queries the item before rendering the form. An unknown item ID returns **Item not found.** with HTTP 404. When the item exists, the page displays an item summary and these required inputs:

| Visible purpose | HTML field | Stored claim field |
|---|---|---|
| Your Name | `name` | `claimant_name` |
| Contact Information | `contact` | `claimant_contact` |
| Claim Message | `message` | `verification_details` |

The actions are **Submit Claim** and **Return to Item Details**.

## Bug #72: empty-claim validation

On `POST`, `claim_request()` strips `name`, `contact` and `message`. If any value is empty or whitespace-only, the route:

- flashes **All claim fields are required.**;
- re-renders the Claim Request form with status 200;
- does not execute the claim `INSERT`;
- does not commit a transaction.

This is server-side validation and remains effective when a direct request bypasses the browser's `required` attributes.

## Valid claim persistence

For a valid submission, `save_claim_request()` performs a parameterised insert into `claims`, records status `pending`, and commits the transaction. The route then redirects to `/claim-success/<int:item_id>`.

## Dedicated Claim Request Submitted page

The delivered workflow does not end with only a generic in-page success message. `/claim-success/<int:item_id>` is a separate page that displays:

- **Claim Request Submitted**;
- confirmation that the request was successfully recorded;
- **Current status: Pending**;
- **View Item Details**;
- **Browse More Items**.

The submitted name, contact information and verification details are not repeated on the confirmation page.

## Responsive and accessibility behaviour

The Item Details image and placeholder resize within the available layout. Navigation and actions stack on smaller screens, and buttons become full width. Images use meaningful alternative text, forms have associated labels, the claim error area uses a polite live region, and CSS supplies visible keyboard-focus styling and reduced-motion handling.

## Pre-refinement implementation limitations

- There is no authentication or user-account UI.
- There is no administrator review interface.
- Claim approval is not implemented.
- Claim-status tracking is not implemented.
- The Item Details UI exposes the claim action only for found items, but the backend claim route does not independently enforce found-only eligibility.
- The success route uses `item_id`, not a claim identifier; it confirms the pending state passed by the application rather than loading a particular claim record.
- Contact information remains visible on Item Details and requires product-owner privacy confirmation.

At this pre-refinement milestone, US08 Track Claim Status, US09 Review Claim
Requests, US10 Update Item Status, and US11 View My Reports were deferred. No
customer acceptance or approval is asserted by this historical design record.

## Current final status

The later lecturer-requested refinement added registration, login, protected
operations, ownership, My Reports, and a read-only Admin Dashboard. US08 and
US10 remain deferred. US09 remains deferred because the administrator cannot
approve or reject claims. The view-only portion of US11 is delivered through My
Reports; report editing and management remain outside scope.

See the authoritative [Final Implemented UI Specification](ui-design.md),
[Implemented System Architecture](architecture.md), and
[Delivered Solution](../delivered-solution.md).
