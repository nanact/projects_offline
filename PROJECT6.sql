CREATE TABLE Customers (
    CustomerID INT,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    City VARCHAR(50)
);

INSERT INTO Customers (CustomerID, FirstName, LastName, Email, City) VALUES
(1, 'Ama', 'Mensah', 'ama.mensah@gmail.com', 'Accra'),
(2, 'Kojo', 'Owusu', 'kojo_owusu@outlook.com', 'Kumasi'),
(3, 'Kwame', 'Boateng', 'kwameb@yahoo.com', 'Takoradi'),
(4, 'Abena', 'Asante', 'abena.asante@gmail.com', 'Accra'),
(5, 'Ama', 'Mensah', 'ama.mensah@gmail.com', 'Accra');

SELECT * FROM Customers
WHERE Email LIKE '%gmail.com';

SELECT * FROM Customers
WHERE City = 'Accra' AND FirstName LIKE 'A%';

SELECT * FROM Customers
ORDER BY LastName ASC;

SELECT DISTINCT City FROM Customers;

SELECT DISTINCT FirstName FROM Customers
WHERE Email LIKE '%gmail.com'
ORDER BY FirstName ASC;

SELECT * FROM Customers
WHERE Email LIKE '%_%';

SELECT DISTINCT LastName FROM Customers
WHERE City = 'Accra'
ORDER BY LastName;

SELECT * FROM Customers
ORDER BY CustomerID DESC;

SELECT City, COUNT(*) AS TotalCustomers
FROM Customers
GROUP BY City;

SELECT City, COUNT(*) AS TotalCustomers
FROM Customers
GROUP BY City
HAVING COUNT(*) > 1;

SELECT City, COUNT(*) AS TotalCustomers
FROM Customers
GROUP BY City
ORDER BY TotalCustomers DESC;