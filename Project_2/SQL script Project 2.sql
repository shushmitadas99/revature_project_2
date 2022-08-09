DROP TABLE IF EXISTS assignments;
DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS teachers;
DROP TABLE IF EXISTS students;

CREATE TABLE students (
	s_id SERIAL PRIMARY KEY,
	username VARCHAR(20) NOT NULL UNIQUE,
	password VARCHAR(20) NOT NULL,
	s_name VARCHAR(200) NOT NULL,
	s_email	VARCHAR(200) NOT NULL UNIQUE
);

INSERT INTO students (username, password, s_name, s_email)
VALUES
('student1', 'password1', 'Student One', 'student1@email.com'), 
('student2', 'password2', 'Student Two', 'student2@email.com');

CREATE TABLE teachers (
	t_id SERIAL PRIMARY KEY,
	username VARCHAR(20) NOT NULL UNIQUE,
	password VARCHAR(20) NOT NULL,
	t_name VARCHAR(200) NOT NULL,
	t_email	VARCHAR(200) NOT NULL UNIQUE
);

INSERT INTO teachers (username, password, t_name, t_email)
VALUES
('teacher1', 'password1', 'Teacher One', 'teacher1@email.com'),
('teacher2', 'password2', 'Teacher Two', 'teacher2@email.com');

CREATE TABLE courses (
	c_id SERIAL PRIMARY KEY,
	c_name VARCHAR(200) NOT NULL,
	c_desc VARCHAR(200) NOT NULL,
	s_id INT NOT NULL,
	t_id INT NOT NULL,
	CONSTRAINT fk_s_id FOREIGN KEY (s_id) REFERENCES students(s_id),
	CONSTRAINT fk_t_id FOREIGN KEY (t_id) REFERENCES teachers(t_id)
);

INSERT INTO courses (c_name, c_desc, s_id, t_id)
VALUES
('science', 'chemistry', '1', '1'),
('science', 'chemistry', '2', '1'),
('math', 'algebra', '2', '2'),
('english', 'academic', '2', '2'); -- added by Shushmita for test_course_service

CREATE TABLE assignments (
	assn SERIAL PRIMARY KEY,
	c_id INT NOT NULL,
    submitted TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    grade VARCHAR(4),
    grade_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_c_id FOREIGN KEY (c_id) REFERENCES courses(c_id)
);

INSERT INTO assignments (c_id, grade)
VALUES
('1', NULL),
('2', NULL);
