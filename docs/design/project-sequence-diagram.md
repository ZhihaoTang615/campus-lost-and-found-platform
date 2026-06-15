# Project Sequence Diagram

This sequence diagram illustrates the key operation of submitting a lost item report with an uploaded photo in the Campus Lost and Found Platform.

```mermaid
sequenceDiagram
    actor User as Student/User
    participant Page as Report Lost Item Page
    participant LostEvent as LostItemReportEvent
    participant ReportDate as ReportDate
    participant PhotoEvent as PhotoUploadEvent
    participant Item as Item
    participant DB as MySQL Database

    User->>Page: Open lost item report page
    Page-->>User: Display report form

    User->>Page: Enter item details and select photo
    User->>Page: Submit report form

    Page->>LostEvent: create LostItemReportEvent
    LostEvent->>ReportDate: create report date
    ReportDate-->>LostEvent: return date value

    LostEvent->>LostEvent: validateEvent()

    alt Valid report data
        LostEvent->>PhotoEvent: create PhotoUploadEvent
        PhotoEvent->>PhotoEvent: validateEvent()

        alt Valid image file
            PhotoEvent-->>LostEvent: return imagePath
            LostEvent->>Item: create Item with report data and imagePath
            Item->>DB: save item record
            DB-->>Item: confirm record saved
            Item-->>LostEvent: return success
            LostEvent-->>Page: report saved successfully
            Page-->>User: Display success message
        else Invalid image file
            PhotoEvent-->>Page: return invalid file message
            Page-->>User: Display error message
        end
    else Invalid report data
        LostEvent-->>Page: return validation error
        Page-->>User: Display error message
    end
```

## Explanation

This sequence diagram applies the Date and Event structure from the class diagram to one key operation in the project.

When a student submits a lost item report with a photo, the system creates a `LostItemReportEvent`. The event is linked with a `ReportDate`, which records when the report happens. The system then validates the report data. If the report data is valid, a `PhotoUploadEvent` validates the uploaded image file. If the image is valid, the system returns an `imagePath`, creates an `Item` object, and saves the item record into the MySQL database.

The alternate path shows that if the uploaded file is invalid, the system returns an error message instead of saving the item.
