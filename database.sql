CREATE DATABASE IF NOT EXISTS campus_lost_and_found;

USE campus_lost_and_found;

CREATE TABLE items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    report_type VARCHAR(10) NOT NULL,
    location VARCHAR(150) NOT NULL,
    report_date DATE NOT NULL,
    description TEXT NOT NULL,
    contact_information VARCHAR(150) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'active',
    image_path VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE claims (
    id INT AUTO_INCREMENT PRIMARY KEY,
    item_id INT NOT NULL,
    claimant_name VARCHAR(100) NOT NULL,
    claimant_contact VARCHAR(150) NOT NULL,
    verification_details TEXT NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (item_id) REFERENCES items(id)
);