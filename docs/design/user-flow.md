# Implemented User Flows

This document records the delivered navigation and request outcomes. The Mermaid flowcharts are authoritative for the current Flask implementation.

## 1. Report Lost Item

```mermaid
flowchart TD
    H[Home] --> L[Report Lost Item]
    L --> LF[Enter item details]
    LF --> LP{Attach optional photo?}
    LP -->|No| LS[Submit report]
    LP -->|Yes| LChoose[Select photo]
    LChoose --> LS
    LS --> LPhoto{Photo supplied?}
    LPhoto -->|No| LInsert[Parameterised INSERT into items]
    LPhoto -->|Yes| LE{Filename extension allowed?}
    LE -->|No| LErr[Flash upload and save errors]
    LErr --> LR[Redirect to lost-item form]
    LE -->|Yes| LSave[Save file under static/uploads]
    LSave --> LInsert
    LInsert --> LI{INSERT and commit succeed?}
    LI -->|Yes| LOk[Flash success]
    LI -->|No| LFail[Flash save error]
    LOk --> LR
    LFail --> LR
```

The form sends a multipart `POST` to `/report-lost-item`. Item Name, Category, Location Lost, Date Lost, Description and Contact Information are browser-required; the photo is optional. The handled success, invalid-extension and database-error paths redirect back to the same form with feedback.

## 2. Report Found Item

```mermaid
flowchart TD
    H[Home] --> F[Report Found Item]
    F --> FF[Enter item details]
    FF --> FP{Attach optional photo?}
    FP -->|No| FS[Submit report]
    FP -->|Yes| FChoose[Select photo]
    FChoose --> FS
    FS --> FPhoto{Photo supplied?}
    FPhoto -->|No| FInsert[Parameterised INSERT into items]
    FPhoto -->|Yes| FE{Filename extension allowed?}
    FE -->|No| FErr[Flash upload and save errors]
    FErr --> FR[Redirect to found-item form]
    FE -->|Yes| FSave[Save file under static/uploads]
    FSave --> FInsert
    FInsert --> FI{INSERT and commit succeed?}
    FI -->|Yes| FOk[Flash success]
    FI -->|No| FFail[Flash save error]
    FOk --> FR
    FFail --> FR
```

The form sends a multipart `POST` to `/report-found-item`. Its required fields mirror the lost-item form, and the optional photo follows the same extension-based upload path.

## 3. Browse, search, filter and view details

```mermaid
flowchart TD
    H[Home] --> B[Browse Items]
    B --> Q[Enter optional keyword q]
    Q --> T[Select optional report type]
    T --> C[Select optional category]
    C --> A[Apply Filters]
    A --> SQL[Combine supplied conditions with AND]
    SQL --> R{Matching results?}
    R -->|No| E[No Items Found]
    E --> VA[View All Items]
    VA --> B
    R -->|Yes| Cards[Item result cards]
    Cards --> VD[View Details]
    VD --> Lookup{Item ID exists?}
    Lookup -->|No| NotFound[404 Item not found]
    Lookup -->|Yes| D[Item Details]
    D --> P{image_path present and loadable?}
    P -->|Yes| Photo[View uploaded photo]
    P -->|No| Placeholder[View no-photo placeholder]
    D --> RB[Return to Browse Items]
    RB --> B
```

The keyword searches item name, description and location. Report type and category are single-choice selectors. The page has no pagination or multi-category filter.

## 4. Submit Claim Request

```mermaid
flowchart TD
    D[Item Details] --> RT{UI sees report_type found?}
    RT -->|No| Hidden[Claim button not displayed]
    RT -->|Yes| Button[Submit Claim Request]
    Button --> GET[GET claim-request/item_id]
    Direct[Direct claim-route request] -. bypasses UI decision .-> GET
    GET --> Select[SELECT item by ID]
    Select --> Exists{Item exists?}
    Exists -->|No| NF[404 Item not found]
    Exists -->|Yes| Form[Claim form]
    Form --> Input[Enter name, contact and message]
    Input --> POST[POST claim request]
    POST --> Strip[Strip all three values]
    Strip --> Valid{All values non-empty?}
    Valid -->|No| Error[Show required-fields message]
    Error --> NoWrite[No INSERT and no commit]
    NoWrite --> Form
    Valid -->|Yes| Insert[INSERT pending claim and commit]
    Insert --> Redirect[Redirect to claim-success/item_id]
    Redirect --> Success[Claim Request Submitted]
    Success --> Status[Display Pending]
    Status --> Choice{Next action}
    Choice -->|View Item Details| D
    Choice -->|Browse More Items| B[Browse Items]
```

The Item Details template makes the found-only decision for the visible claim button. The backend `/claim-request/<int:item_id>` route verifies that the item exists but does not independently enforce `report_type = found`; a direct request can therefore bypass the UI eligibility boundary.

The success screen is a separate `/claim-success/<int:item_id>` page. It shows Pending and links to the selected Item Details page or back to Browse Items, without displaying the submitted private form values.

## Historical design artifact

![Historical User Flow Diagram](images/user-flow-diagram.png)

The image is retained as an earlier planning artefact. It omits the delivered browse/search/filter, photo fallback, validation, 404 and dedicated claim-success paths, so it is not the authoritative current flow.
