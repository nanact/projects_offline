CREATE TABLE Employees (
    EmployeeID INT,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Department VARCHAR(50),
    Salary DECIMAL(8,2),
    ExperienceYears INT
);

INSERT INTO Employees (EmployeeID, FirstName, LastName, Department, Salary, ExperienceYears) VALUES
(1, 'Ama', 'Mensah', 'HR', 4500.00, 5),
(2, 'Kojo', 'Owusu', 'IT', 5500.00, 7),
(3, 'Abena', 'Asante', 'Finance', 6000.00, 10),
(4, 'Kwame', 'Boateng', 'IT', 4800.00, 4),
(5, 'Efua', 'Adjei', 'Marketing', 4300.00, 3);

UPDATE Employees
SET ExperienceYears = ExperienceYears + 1
WHERE Department = 'IT';

DELETE FROM Employees
WHERE Salary < 4500;

SELECT * FROM Employees
WHERE Department = 'IT' AND ExperienceYears >= 5;

SELECT * FROM Employees
ORDER BY Salary DESC;

SELECT Department, SUM(Salary) AS TotalSalary
FROM Employees
GROUP BY Department;

SELECT FirstName, LastName, MAX(ExperienceYears) AS MaxExperience
FROM Employees;

SELECT Department, SUM(Salary) AS TotalSalary
FROM Employees
GROUP BY Department
HAVING SUM(Salary) > 10000;

SELECT Department, SUM(Salary) AS TotalSalary
FROM Employees
GROUP BY Department
ORDER BY TotalSalary DESC;