CREATE TABLE Sales (
    SaleID INT,
    ProductName VARCHAR(100),
    Quantity INT,
    Price DECIMAL(6,2)
);

INSERT INTO Sales (SaleID, ProductName, Quantity, Price) VALUES
(1, 'Laptop', 2, 750.00),
(2, 'Mouse', 5, 15.50),
(3, 'Keyboard', 3, 30.00),
(4, 'Monitor', 1, 120.00),
(5, 'Headphones', 4, 40.75);

SELECT SUM(Quantity) AS TotalItemsSold FROM Sales;

SELECT AVG(Price) AS AverageProductPrice FROM Sales;