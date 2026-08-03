-- ONE-TIME MIGRATION: add the lecturer-requested user and administrator system.
-- Run this file once against the existing campus lost-and-found database.
-- The new ownership columns are nullable, so every existing item and claim row
-- is preserved as an anonymous/legacy record with a NULL user_id.

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(20) NOT NULL DEFAULT 'user',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Link future item reports to an account while retaining all existing rows.
ALTER TABLE items
    ADD COLUMN user_id INT NULL,
    ADD CONSTRAINT fk_items_user
        FOREIGN KEY (user_id) REFERENCES users(id);

-- Link future claim requests to an account while retaining all existing rows.
ALTER TABLE claims
    ADD COLUMN user_id INT NULL,
    ADD CONSTRAINT fk_claims_user
        FOREIGN KEY (user_id) REFERENCES users(id);
