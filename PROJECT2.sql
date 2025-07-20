CREATE TABLE Products (
    ProductID INT,
    ProductName VARCHAR(100),
    Price DECIMAL(5,2),
    Quantity INT
);

INSERT INTO Products (ProductID, ProductName, Price, Quantity) VALUES
(1, 'Laptop', 750.00, 10),
(2, 'Mouse', 15.50, 25),
(3, 'Keyboard', 30.00, 5),
(4, 'Monitor', 120.00, 8),
(5, 'Headphones', 40.75, 20);

SELECT * FROM Products
WHERE Price > 100;

SELECT * FROM Products
WHERE Price < 50 AND Quantity > 10;

