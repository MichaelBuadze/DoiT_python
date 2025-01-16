-- Active: 1736342422552@@127.0.0.1@3307@lesson27_hw
-- CREATE DATABASE lesson27_hw; - ამ ბრძანებით შეიქმნა მონაცემთა ბაზა;
-- USE lesson27_hw; - ამ ბრძანებით კონსოლი გადმოდის მიმდინარე ბაზაზე;

CREATE TABLE migrations (
    id INT PRIMARY KEY,
    distance INT NOT NULL,
    days INT NOT NULL
);

INSERT INTO migrations (id, distance, days) VALUES
(10484, 1000, 107),
(11728, 1531, 56),
(11729, 1370, 37),
(11732, 1622, 62),
(11734, 1491, 58),
(11735, 2723, 82),
(11736, 1571, 52),
(11737, 1957, 92);


CREATE TABLE sea_lions (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    species VARCHAR(100) NOT NULL
);

INSERT INTO sea_lions (id, name, species) VALUES
(10484, 'Ayah', 'Zalophus californianus'),
(11728, 'Spot', 'Zalophus californianus'),
(11729, 'Tiger', 'Zalophus californianus'),
(11732, 'Mabel', 'Zalophus californianus'),
(11734, 'Rick', 'Zalophus californianus'),
(11790, 'Jolee', 'Zalophus californianus');


SELECT m.id, m.distance, m.days, s.name, s.species
FROM migrations AS m
JOIN sea_lions AS s
ON m.id = s.id;


SELECT m.id, m.distance, m.days, s.name, s.species
FROM migrations AS m
LEFT JOIN sea_lions AS s
ON m.id = s.id;


SELECT m.id, m.distance, m.days, s.name, s.species
FROM migrations AS m
RIGHT JOIN sea_lions AS s
ON m.id = s.id;


SELECT m.id, m.distance, m.days, s.name, s.species
FROM migrations AS m
LEFT JOIN sea_lions AS s
ON m.id = s.id

UNION

SELECT m.id, m.distance, m.days, s.name, s.species
FROM migrations AS m
RIGHT JOIN sea_lions AS s
ON m.id = s.id;

SELECT m.id, m.distance, m.days, s.name, s.species
FROM migrations AS m
LEFT JOIN sea_lions AS s
ON m.id = s.id

UNION ALL

SELECT m.id, m.distance, m.days, s.name, s.species
FROM migrations AS m
RIGHT JOIN sea_lions AS s
ON m.id = s.id;

SELECT m.id, m.distance, m.days, s.name, s.species
FROM migrations AS m
LEFT JOIN sea_lions AS s
ON m.id = s.id

UNION ALL

SELECT m.id, m.distance, m.days, s.name, s.species
FROM migrations AS m
RIGHT JOIN sea_lions AS s
ON m.id = s.id
WHERE m. id IS NULL ;