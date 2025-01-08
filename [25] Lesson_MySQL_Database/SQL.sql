SELECT * 
FROM customers
;
SELECT customerName, phone
FROM customers
;
SELECT customerName, phone
FROM customers
LIMIT 10
;

SELECT *
FROM customers
WHERE city = "NYC"
;
SELECT *
FROM customers
WHERE city in ("NYC", "Milan")
;

SELECT *
FROM customers
WHERE city in ("NYC", "Milan")
ORDER BY customerName
;

SELECT *
FROM customers
WHERE city in ("NYC", "Milan")
ORDER BY customerNumber
;