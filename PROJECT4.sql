CREATE TABLE Orders (
    OrderID INT,
    CustomerName VARCHAR(100),
    Product VARCHAR(100),
    Quantity INT,
    Price DECIMAL(6,2)
);

INSERT INTO Orders (OrderID, CustomerName, Product, Quantity, Price) VALUES
(1, 'Ama', 'Laptop', 2, 750.00),
(2, 'Kwame', 'Mouse', 5, 15.50),
(3, 'Ama', 'Monitor', 1, 120.00),
(4, 'Kojo', 'Laptop', 1, 750.00),
(5, 'Kwame', 'Keyboard', 2, 30.00),
(6, 'Ama', 'Headphones', 3, 40.75);

SELECT CustomerName, SUM(Quantity) AS TotalItems
FROM Orders
GROUP BY CustomerName;