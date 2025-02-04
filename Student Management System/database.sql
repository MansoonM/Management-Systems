CREATE DATABASE IF NOT EXISTS student_management_db;
USE student_management_db;

CREATE TABLE IF NOT EXISTS student_personal (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(255) NOT NULL,
    student_branch VARCHAR(255) NOT NULL,
    student_year INT NOT NULL,
    bput_reg_no VARCHAR(20) UNIQUE NOT NULL,
    phone_number VARCHAR(15) NOT NULL,
    address TEXT NOT NULL,
    guardian_name VARCHAR(255) NOT NULL,
    guardian_number VARCHAR(15) NOT NULL,
    complaint TEXT
);

CREATE TABLE IF NOT EXISTS student_fees (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(255) NOT NULL,
    student_branch VARCHAR(255) NOT NULL,
    student_year INT NOT NULL,
    fees DECIMAL(10,2) NOT NULL,
    fees_paid ENUM('yes', 'no') NOT NULL,
    hostel_staying ENUM('yes', 'no') NOT NULL,
    any_fine DECIMAL(10,2) DEFAULT 0.00,
    fine_paid ENUM('yes', 'no') NOT NULL
);