CREATE TABLE Students (
    StudentID INT,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Grade INT
);

INSERT INTO Students (StudentID, FirstName, LastName, Grade) VALUES
(1, 'Ama', 'Mensah', 85),
(2, 'Kwame', 'Boateng', 92),
(3, 'Abena', 'Owusu', 76),
(4, 'Kojo', 'Asante', 88);

SELECT * FROM Students;

SELECT * FROM Students
WHERE Grade > 80;

SELECT * FROM Students
ORDER BY Grade DESC;