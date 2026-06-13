# Database Design

The Campus Lost and Found Platform will use a MySQL database to store lost item reports, found item reports, and ownership claim requests.

---

## Database Overview

The database is designed to support:

* Reporting lost items
* Reporting found items
* Searching and filtering items
* Uploading item photos
* Submitting ownership claims
* Managing item status

---

## Items Table

The Items table stores information about lost and found items.

Fields:

* item_id (Primary Key)
* item_name
* category
* description
* location
* report_type (Lost or Found)
* image_path
* report_date
* status

---

## Claims Table

The Claims table stores ownership claim requests submitted by users.

Fields:

* claim_id (Primary Key)
* item_id (Foreign Key)
* claimant_name
* contact_information
* ownership_evidence
* claim_status
* submission_date

---

## Users Table (Future Feature)

The Users table may be introduced in future iterations to support user accounts and authentication.

Possible fields:

* user_id (Primary Key)
* full_name
* email
* password_hash

---

## Entity Relationship

One item may have multiple ownership claims.

Relationship:

Items (1) -------- (Many) Claims

A detailed Entity Relationship (ER) Diagram is provided in the design images folder and may be refined in future iterations.

---

## ER Diagram

![Database ER Diagram](images/database-er-diagram.png)

---

## Future Enhancements

Future database improvements may include:

* User authentication
* Admin accounts
* Claim approval history
* Notification records
* Audit logging
