-- Create Database
CREATE DATABASE IF NOT EXISTS library_db;
USE library_db;

-- Create Staff Table
CREATE TABLE IF NOT EXISTS staff (
    staff_id INT PRIMARY KEY,
    staff_name VARCHAR(255) NOT NULL,
    staff_branch VARCHAR(255) NOT NULL,
    staff_job_position VARCHAR(255) NOT NULL,
    BookName VARCHAR(255) NOT NULL,
    BookType VARCHAR(255) NOT NULL,
    DateOfIssue DATE NOT NULL,
    DateOfReturn DATE NOT NULL,
    AnyFine INT DEFAULT 0
);

-- Create Students Table
CREATE TABLE IF NOT EXISTS students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(255) NOT NULL,
    student_branch VARCHAR(255) NOT NULL,
    student_year INT NOT NULL,
    BookName VARCHAR(255) NOT NULL,
    BookType VARCHAR(255) NOT NULL,
    DateOfIssue DATE NOT NULL,
    DateOfReturn DATE NOT NULL,
    AnyFine INT DEFAULT 0
);