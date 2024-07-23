"notes - crud opeartions" - mysql


/*
    workbench of the mysql:
    -- create database 
    CREATE DATABASE notes_search_db;

    -- to switch to the database as current database 
    USE notes_search_db;

    -- to drop the database
    DROP DATABASE notes_search_db;
    -- best practice: delte database tables etc and then drop the database
*/

-- to create notes table 
CREATE TABLE notes (
    id INT PRIMARY KEY AUTO_INCREMENT, 
    title VARCHAR(255) not null, 
    notes VARCHAR(3500) not null 
);
-- to see the tables definition 
DESC notes;
-- to display the rows of the table 
SELECT * FROM notes;
-- to insert a row 
INSERT INTO notes(title, notes) VALUES('HTML 5', 'HTML 5 is web development language');
INSERT INTO notes(title, notes) 
    VALUES('CSS 3', 'CSS 3 makes web site look and feel.');
-- to inser many rows
INSERT INTO notes(title, notes) 
    VALUES
        ('Python', 'Python is a eash high level language.'),
        ('Flask', 'Flask is a web development framework and library of python.');
-- to change the notes of the 'HTML 5' as 
-- 'HTML 5 is the web development language for markup the content of the web site'
UPDATE notes 
    SET notes = 'HTML 5 is the web development language for markup the content of the web site'
    WHERE id = 1; -- best practice : coz : id pk, indexed

    -- OR 
UPDATE notes 
    SET notes = 'HTML 5 is the web development language for markup the content of the web site'
    WHERE title = 'HTML 5'; -- title is not indexed, so lag may be there in update

-- to delete, first we will create row for title 'Science' with notes 'Study of nature'
INSERT INTO notes(title, notes) VALUES('Science', 'Study of nature');

-- science is irrelevant to the web technology subject matter
-- so we delete it 
DELETE FROM notes WHERE id=5; -- best practice

    -- OR 
DELETE FROM notes WHERE title='Science'; -- lag may be in delete coz of non-indexed title column

-- display all rows of notes and all fields 
SELECT id, title, notes 
FROM notes;

-- display only HTML 5 notes
SELECT id, title, notes 
FROM notes 
WHERE title='HTML 5';

-- display only Python notes
SELECT id, title, notes 
FROM notes 
WHERE title='Python';

-- display notes which have language in its text -- display notes which contains the text 'language'
SELECT id, title, notes 
FROM notes 
WHERE notes LIKE '%language%';

-- display notes which contains the text 'web'
SELECT id, title, notes 
FROM notes 
WHERE notes LIKE '%web%';

-- - to drop the table
-- DROP TABLE notes;
