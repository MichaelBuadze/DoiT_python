-- Active: 1736342422552@@127.0.0.1@3307@lesson26

-- 1. შექმენით ცხრილი - Authors, პირველადი გასაღებით;
CREATE TABLE Authors (
    AuthorID INT AUTO_INCREMENT PRIMARY KEY,
    authorName VARCHAR(255) NOT NULL,
    BirthYear INT
);

-- 2. შექმენით ცხრილი - Books, მეორადი გასაღებით AuthorID;
CREATE TABLE Books (
    BookID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    Genre VARCHAR(100),
    PublishYear INT,
    AuthorID INT,
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID)
);

-- 3. დაამატეთ მინიმუმ 5 ჩანაწერი Authors და Books ცხრილებში
-- 3.1 Author ჩანაწერები
INSERT INTO authors(`authorName`, `BirthYear`)
VALUES
    ('ნიკოლოზ ბარათაშვილი', 1817),
    ('ილია ჭავჭავაძე', 1837),
    ('აკაკი წერეთელი', 1840),
    ('გალაკტიონ ტაბიძე', 1892),
    ('კონსტანტინე გამსახურდია', 1893);

-- 3.2 Books ჩანაწერები
INSERT INTO Books (`Title`, `Genre`, `PublishYear`, `AuthorID`) 
VALUES
    ('მერანი', 'ლირიკა', 1844, 1),
    ('გლახის ნაამბობი', 'პროზა', 1866, 2),
    ('თორნიკე ერისტავი', 'ეპიკური პოემა', 1871, 3),
    ('მე და ღამე', 'ლირიკა', 1919, 4),
    ('დიდოსტატის მარჯვენა', 'ისტორიული რომანი', 1939, 5);

-- 4. განახლების ბრძანება Books ცხრილში
UPDATE Books
SET Genre = 'სოციალური პროზა'
WHERE Title = 'გლახის ნაამბობი';

-- 5. გაერთიანებული ცხრილების დაბეჭდვა
SELECT 
    Authors.`AuthorID`, 
    Authors.`authorName` AS AuthorName, 
    Books.`BookID`, 
    Books.`Title` AS BookTitle, 
    Books.`Genre`, 
    Books.`PublishYear`
FROM Authors
INNER JOIN Books ON Authors.`AuthorID` = Books.`AuthorID`;

-- 6. წაშალეთ ყველა ჩანაწერი Author და Books ცხრილებიდან
DELETE FROM Books;
DELETE FROM Authors;

-- 7. წაშალეთ Authors და Books ცხრილები
DROP TABLE Books;
DROP TABLE Authors;
