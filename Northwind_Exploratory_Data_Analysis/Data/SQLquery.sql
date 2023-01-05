SHOW DATABASES;
USE northwind;

SHOW TABLES;

SELECT*FROM customerdemographics;

-- Table 1
SELECT
	o.OrderID,
    o.CustomerID,
    cu.CompanyName AS CustomerCompany,
    o.OrderDate,
	o.ShippedDate,
	o.RequiredDate,
    DATEDIFF(o.RequiredDate,o.ShippedDate) AS DayDifference,
	o.ShipCountry,
    p.ProductID,
	p.ProductName,
	p.CategoryID,
	od.Quantity,
	p.QuantityPerUnit AS UnitPerQuantity,
	p.UnitPrice,
	p.SupplierID,
    su.CompanyName AS SupplierName,
    su.Country AS SupplierCountry
FROM orders o LEFT JOIN customers cu
		USING (CustomerID)
	 LEFT JOIN orderdetails od
		USING (OrderID)
	 LEFT JOIN products p
		USING (ProductID)
	 LEFT JOIN categories c
		USING (CategoryID)
	 LEFT JOIN suppliers su
		USING (SupplierID);

-- Table2
WITH cte1 AS (
SELECT 
	p.CategoryID,
    SUM(od.Quantity) AS TotalOrdered
FROM products p LEFT JOIN categories c 
		USING (CategoryID)
	 LEFT JOIN orderdetails od
		USING (ProductID)
GROUP BY p.CategoryID)

SELECT
	c.CategoryID,
    c.CategoryName,
    c.Description,
    COUNT(p.ProductID) AS NumberOfProducts,
    SUM(p.UnitsInStock) AS TotalStock,
    SUM(p.UnitsOnOrder) AS TotalOngoingRestock,
    cte1.TotalOrdered,
    SUM(p.UnitPrice) AS TotalPriceValue,
    SUM(p.Discontinued) AS TotalDiscontinued
FROM products p LEFT JOIN categories c 
		USING (CategoryID)
	 LEFT JOIN cte1
		USING (CategoryID)
GROUP BY c.CategoryID
ORDER BY c.CategoryID ASC;

-- Table 3
SELECT
	p.ProductID,
    p.ProductName,
    c.CategoryName,
    su.CompanyName AS SupplierName,
    p.QuantityPerUnit AS UnitPerQuantity,
    p.UnitPrice,
    p.UnitsInStock,
    p.UnitsOnOrder,
    p.ReorderLevel,
    p.Discontinued 
FROM products p LEFT JOIN categories c 
		USING (CategoryID)
	 LEFT JOIN suppliers su
		USING (SupplierID);

-- Q3 table top 25%
SELECT 
	p.ProductID,
    p.ProductName,
	p.ReorderLevel,
    SUM(od.Quantity) AS TotalQuantityOrdered
FROM products p LEFT JOIN orderdetails od
		USING (ProductID)
	LEFT JOIN orders o
		USING (OrderID)
GROUP BY p.ProductID
ORDER BY SUM(od.Quantity) DESC
LIMIT 19;

-- Q3 table bottom 25%
SELECT 
	p.ProductID,
    p.ProductName,
	p.ReorderLevel,
    SUM(od.Quantity) AS TotalQuantityOrdered
FROM products p LEFT JOIN orderdetails od
		USING (ProductID)
	LEFT JOIN orders o
		USING (OrderID)
GROUP BY p.ProductID
ORDER BY SUM(od.Quantity) ASC
LIMIT 19;