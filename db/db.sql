CREATE DATABASE lic_db;

USE lic_db;

CREATE TABLE processed_files (
    id INT AUTO_INCREMENT PRIMARY KEY,
    file_name VARCHAR(255),
    file_path VARCHAR(255),
    processing_time FLOAT,
    processed_date DATETIME
);

CREATE TABLE aggregate_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    total_processing_time FLOAT,
    total_files_processed INT
);

CREATE TABLE analyzed_texts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    military_units TEXT,
    political_divisions TEXT,
    publication_date DATE,
    newspaper_name VARCHAR(255),
    processing_time FLOAT,
    processed_date DATETIME
);
