# Project Sequence Diagrams

These implementation-aligned sequences show how the delivered function-based Flask application reports an item and submits a claim request. They use the real routes, helpers, database operations, and response behaviour from `app.py`; conceptual Event and Date elements are not presented as runtime participants.

## Combined final PNG export

[![Final project sequence diagrams](images/final-sequence-diagram.png)](images/final-sequence-diagram.png)

The PNG above combines the two authoritative Mermaid sequences below and
reflects the current final system.

## Sequence 1: Report an item with an optional photo

The lost-item and found-item routes share `save_item_report()`. Their route-specific values are `report_type` (`lost` or `found`) and the date form field (`date-lost` or `date-found`). The report templates mark the non-photo fields as HTML `required` fields, but `save_item_report()` accesses those values directly and does not perform an additional explicit empty-field validation pass.

```mermaid
sequenceDiagram
    actor User
    participant Form as Browser/Form
    participant Route as Flask report route
    participant SaveReport as save_item_report()
    participant Files as File Storage
    participant DB as MySQL

    User->>Form: Open /report-lost-item or /report-found-item
    Form->>Route: GET report route
    Route-->>Form: Render the corresponding report template
    Form-->>User: Display form with required fields and optional photo

    User->>Form: Enter report data and optionally select item-photo
    Form->>Route: POST multipart form
    Route->>SaveReport: save_item_report(report_type, date_field)
    SaveReport->>SaveReport: Inspect optional item-photo

    alt Photo supplied with an invalid extension
        SaveReport->>SaveReport: is_allowed_file(filename) returns false
        SaveReport-->>Route: Flash invalid-file message and return false
        Route-->>Form: Flash unable-to-save message and redirect to same report route
        Form-->>User: Display the report form and messages
    else No photo or an accepted extension
        opt Photo supplied with png, jpg, jpeg, or gif extension
            SaveReport->>SaveReport: secure_filename(original filename)
            SaveReport->>Files: Save under static/uploads
            Files-->>SaveReport: File stored
            SaveReport->>SaveReport: Set image_path to uploads/filename
        end

        SaveReport->>DB: get_database_connection()
        SaveReport->>DB: Parameterised INSERT into items

        alt INSERT and commit succeed
            SaveReport->>DB: commit()
            DB-->>SaveReport: Transaction committed
            SaveReport-->>Route: Return true
            Route-->>Form: Flash success and redirect to same report route
            Form-->>User: Display the report form and success message
        else MySQL operation fails
            DB--xSaveReport: mysql.connector.Error
            SaveReport-->>Route: Return false after closing resources
            Route-->>Form: Flash unable-to-save message and redirect
            Form-->>User: Display the report form and error message
        end
    end
```

When no file is supplied, `image_path` is inserted as `NULL`. File validation checks the filename extension only. The sequence does not imply MIME, size, filename-collision, or malware validation.

## Sequence 2: Submit a claim request

```mermaid
sequenceDiagram
    actor User
    participant ItemPage as Item Details Page
    participant ClaimRoute as Flask claim_request route
    participant DB as MySQL
    participant SaveClaim as save_claim_request()
    participant Success as Claim Success Page

    User->>ItemPage: Open a found item at /items/<item_id>
    ItemPage-->>User: Display item details
    Note over ItemPage: Submit Claim Request is displayed only when report_type is found
    User->>ItemPage: Select Submit Claim Request
    ItemPage->>ClaimRoute: GET /claim-request/<item_id>
    ClaimRoute->>DB: SELECT item by id using a parameter

    alt Item does not exist
        DB-->>ClaimRoute: No row
        ClaimRoute-->>User: 404 Item not found
    else Item exists
        DB-->>ClaimRoute: Selected item row
        ClaimRoute-->>User: Render claim-request form
        User->>ClaimRoute: POST name, contact, and message
        ClaimRoute->>DB: SELECT item by id using a parameter

        alt Item no longer exists
            DB-->>ClaimRoute: No row
            ClaimRoute-->>User: 404 Item not found
        else Item still exists
            DB-->>ClaimRoute: Selected item row
            ClaimRoute->>ClaimRoute: Strip name, contact, and message

            alt Any field is empty or whitespace-only
                ClaimRoute-->>User: Render form with required-fields message (HTTP 200)
                Note over ClaimRoute,DB: No claim INSERT and no commit
            else All fields contain values
                ClaimRoute->>SaveClaim: save_claim_request(...)
                SaveClaim->>DB: Parameterised INSERT into claims with status pending
                SaveClaim->>DB: commit()
                DB-->>SaveClaim: Transaction committed
                SaveClaim-->>ClaimRoute: Claim stored
                ClaimRoute-->>User: 302 redirect to /claim-success/<item_id>
                User->>Success: GET /claim-success/<item_id>
                Success-->>User: Claim Request Submitted, current status Pending
                Success-->>User: View Item Details and Browse More Items actions
                Note over Success,User: Submitted contact and verification values are not displayed
            end
        end
    end
```

The Item Details template conditionally exposes the claim action for a found item. This is a user-interface eligibility rule only: a direct request to `/claim-request/<int:item_id>` loads any existing item, because `claim_request()` does not independently enforce `report_type == "found"`.
