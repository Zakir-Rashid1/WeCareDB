
-- Create student table

CREATE TABLE student(
    student_id INT PRIMARY KEY,
    student_fname VARCHAR(30) NOT NULL,
    student_lname VARCHAR(30) NOT NULL,
    student_locality VARCHAR(30) NOT NULL,
    student_district VARCHAR(30) NOT NULL,
    student_city VARCHAR(30) NOT NULL,
    student_state VARCHAR(30) NOT NULL
);


-- Create id proof table
CREATE TABLE idproof(
    id_number BIGINT PRIMARY KEY,
    id_type VARCHAR(30),
    id_expiry_date VARCHAR(30),
    student_id INT,
    FOREIGN KEY (student_id) REFERENCES student(student_id)
    ON DELETE SET NULL
);


-- Create exam table
CREATE TABLE exam(
    student_id INT PRIMARY KEY,
    exam_type VARCHAR(30) NOT NULL,
    exam_rank INT NOT NULL,
    exam_marks INT NOT NUll,
    FOREIGN KEY (student_id) REFERENCES student(student_id) 
    ON DELETE CASCADE
);


-- Create class table
CREATE TABLE institution(
    student_id INT PRIMARY KEY,
    present_class VARCHAR(30) NOT NULL,
    name_of_school VARCHAR(30) NOT NULL,
    FOREIGN KEY (student_id) REFERENCES student(student_id)
    ON DELETE CASCADE
);



SELECT * FROM student;
SELECT * FROM idproof;
SELECT * FROM exam;
SELECT * FROM institution;