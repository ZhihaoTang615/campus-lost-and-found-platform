# Project Class Diagram

This class diagram adapts the Date and Event structure from the Head First example to our Campus Lost and Found Platform.

```mermaid
classDiagram
    class ReportDate {
        -String dateValue
        +getDateValue() String
        +formatDate() String
        #validateEvent(event: ItemEvent) boolean
    }

    class ItemEvent {
        <<abstract>>
        -int id
        -ReportDate eventDate
        +getName() String
        +validateEvent() boolean
    }

    class LostItemReportEvent {
        -String name = "LostItemReport"
        -String itemName
        -String category
        -String location
        -String description
        -String contactInformation
        -String imagePath
        +getName() String
        +validateEvent() boolean
    }

    class FoundItemReportEvent {
        -String name = "FoundItemReport"
        -String itemName
        -String category
        -String location
        -String description
        -String contactInformation
        -String imagePath
        +getName() String
        +validateEvent() boolean
    }

    class ClaimRequestEvent {
        -String name = "ClaimRequest"
        -int itemId
        -String claimantName
        -String claimantContact
        -String verificationDetails
        +getName() String
        +validateEvent() boolean
    }

    class PhotoUploadEvent {
        -String name = "PhotoUpload"
        -String filename
        -String fileType
        -String imagePath
        +getName() String
        +validateEvent() boolean
    }

    class Item {
        -int id
        -String itemName
        -String category
        -String reportType
        -String location
        -ReportDate reportDate
        -String description
        -String contactInformation
        -String status
        -String imagePath
        +isLostItem() boolean
        +isFoundItem() boolean
    }

    class ClaimRequest {
        -int id
        -int itemId
        -String claimantName
        -String claimantContact
        -String verificationDetails
        -String status
        +submitClaim() void
        +updateStatus() void
    }

    ItemEvent <|-- LostItemReportEvent
    ItemEvent <|-- FoundItemReportEvent
    ItemEvent <|-- ClaimRequestEvent
    ItemEvent <|-- PhotoUploadEvent

    ReportDate "1" --> "0..*" ItemEvent : events
    LostItemReportEvent --> Item : creates
    FoundItemReportEvent --> Item : creates
    PhotoUploadEvent --> Item : updates imagePath
    ClaimRequestEvent --> ClaimRequest : creates
    Item "1" --> "0..*" ClaimRequest : receives
