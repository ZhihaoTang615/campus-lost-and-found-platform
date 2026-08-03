# Implemented User Flows

This document records the delivered navigation and request outcomes. The Mermaid
flowcharts are authoritative for the current Flask implementation. Sections
1–4 retain the US01-US07 behavior behind the final login guard; Sections 5–7
document the account and viewing refinement. Earlier evidence of unauthenticated
baseline operation remains historical rather than describing current access.

## 1. Report Lost Item

```mermaid
flowchart TD
    H[Home] --> Auth{Logged in?}
    Auth -->|No| Login[Redirect to Login]
    Auth -->|Yes| L[Report Lost Item]
    L --> LF[Enter item details]
    LF --> LP{Attach optional photo?}
    LP -->|No| LS[Submit report]
    LP -->|Yes| LChoose[Select photo]
    LChoose --> LS
    LS --> LPhoto{Photo supplied?}
    LPhoto -->|No| LInsert[INSERT item with session user ID]
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

`/report-lost-item` requires login. The form sends a multipart `POST`; the
handled success, invalid-extension and database-error paths redirect back to the
same form with feedback. Every successful item insert stores the required
session user ID.

## 2. Report Found Item

```mermaid
flowchart TD
    H[Home] --> Auth{Logged in?}
    Auth -->|No| Login[Redirect to Login]
    Auth -->|Yes| F[Report Found Item]
    F --> FF[Enter item details]
    FF --> FP{Attach optional photo?}
    FP -->|No| FS[Submit report]
    FP -->|Yes| FChoose[Select photo]
    FChoose --> FS
    FS --> FPhoto{Photo supplied?}
    FPhoto -->|No| FInsert[INSERT item with session user ID]
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

`/report-found-item` requires login. Its required fields mirror the lost-item
form, and the optional photo follows the same extension-based upload path. Every
successful insert is owned by the authenticated account.

## 3. Browse, search, filter and view details

```mermaid
flowchart TD
    H[Home] --> Auth{Logged in?}
    Auth -->|No| Login[Redirect to Login]
    Auth -->|Yes| B[Browse Items]
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

The Browse, search/filter, generic details entry, and selected Item Details
routes require login. The keyword searches item name, description and location.
Report type and category are single-choice selectors. The page has no
pagination or multi-category filter.

## 4. Submit Claim Request

```mermaid
flowchart TD
    Access[Claim route request] --> Auth{Logged in?}
    Auth -->|No| Login[Redirect to Login]
    Auth -->|Yes| D[Item Details]
    D --> RT{UI sees report_type found?}
    RT -->|No| Hidden[Claim button not displayed]
    RT -->|Yes| Button[Submit Claim Request]
    Button --> GET[GET claim-request/item_id]
    Direct[Direct authenticated claim request] -. bypasses UI decision .-> GET
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
    Valid -->|Yes| Insert[INSERT owned pending claim and commit]
    Insert --> Redirect[Redirect to claim-success/item_id]
    Redirect --> Success[Claim Request Submitted]
    Success --> Status[Display Pending]
    Status --> Choice{Next action}
    Choice -->|View Item Details| D
    Choice -->|Browse More Items| B[Browse Items]
```

Login is required for the claim request and claim-success routes. The Item
Details template makes the found-only decision for the visible claim button.
The backend verifies that the item exists but does not independently enforce
`report_type = found`; an authenticated direct request can therefore bypass the
UI eligibility boundary.

The success screen is a separate login-protected page. It shows Pending and
links to Item Details or Browse Items without displaying submitted private
values. Every new claim stores the authenticated session user ID.

## 5. Register, log in, and log out

```mermaid
flowchart TD
    Visitor[Logged-out visitor] --> Register[GET or POST Register]
    Register --> RV{Registration values valid and email unique?}
    RV -->|No| RE[Show user-friendly validation message]
    RE --> Register
    RV -->|Yes| Hash[Generate password hash and insert role user]
    Hash --> Login[Redirect to Login]
    Visitor --> Login
    Login --> Credentials[Normalize email and check password hash]
    Credentials --> Valid{Credentials valid?}
    Valid -->|No| Generic[Show generic invalid-credentials message]
    Generic --> Login
    Valid -->|Yes| Rebuild[Clear old session and store user ID, name, and role]
    Rebuild --> Safe{Allowed local next supplied?}
    Safe -->|Yes| Destination[Local destination permitted for role]
    Safe -->|No| Role{Administrator role?}
    Role -->|No| My[My Reports]
    Role -->|Yes| Admin[Admin Dashboard]
    Destination --> MyOrAdmin[Requested authenticated page]
    My --> Logout[POST Logout]
    Admin --> Logout
    MyOrAdmin --> Logout
    Logout --> Clear[Clear session and return Home]
```

The safe-return check accepts local absolute paths only and rejects external or scheme-relative destinations. A normal user cannot use `next` to enter `/admin`. Public registration cannot create an administrator; the interactive `scripts/create_admin.py` script is the separate administrator-account path.

## 6. View My Reports

```mermaid
flowchart TD
    Request[GET My Reports] --> Auth{Session user ID present?}
    Auth -->|No| Login[Redirect to Login with local next]
    Auth -->|Yes| Query[SELECT items WHERE user_id equals session user ID]
    Query --> Order[Order newest first]
    Order --> Results{Owned reports exist?}
    Results -->|No| Empty[Show No Reports Yet and reporting actions]
    Results -->|Yes| Cards[Show owned report cards]
    Cards --> Details[Open authenticated Item Details]
```

The filter uses only the authenticated session user ID. It never accepts another user's ID from a URL or form. An administrator may use My Reports, but receives the same own-account filter.

## 7. View administrator records

```mermaid
flowchart TD
    Request[GET Admin] --> SignedIn{Authenticated?}
    SignedIn -->|No| Login[Redirect to Login]
    SignedIn -->|Yes| Role{Session role is admin?}
    Role -->|No| Forbidden[Return 403 Administrator access required]
    Role -->|Yes| Counts[SELECT item and claim summary counts]
    Counts --> Items[SELECT all items LEFT JOIN users]
    Items --> Claims[SELECT all claims LEFT JOIN items and users]
    Claims --> Dashboard[Render read-only Admin Dashboard]
    Dashboard --> Legacy[Show pre-enhancement NULL owners with legacy fallback]
```

The dashboard exposes viewing only. It has no POST route and no delete, ban,
approval, rejection, or status-update action. `LEFT JOIN` keeps all
pre-enhancement records with `NULL` ownership visible; current application
submissions are always owned.

## Historical design artifact

![Historical User Flow Diagram](images/user-flow-diagram.png)

The image is retained as an earlier planning artefact. It omits the delivered browse/search/filter, photo fallback, validation, 404 and dedicated claim-success paths, so it is not the authoritative current flow.
