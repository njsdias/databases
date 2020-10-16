SELECT author_fname, author_lname FROM books;
--CONCAT
CONCAT(x,y,z) // from slides

CONCAT(column, anotherColumn) // from slides

CONCAT(author_fname, author_lname)

CONCAT(column, 'text', anotherColumn, 'more text')

CONCAT(author_fname, ' ', author_lname)

CONCAT(author_fname, author_lname); // invalid syntax

SELECT CONCAT('Hello', 'World');

SELECT CONCAT('Hello', '...', 'World');

SELECT
  CONCAT(author_fname, ' ', author_lname)
FROM books;

SELECT
  CONCAT(author_fname, ' ', author_lname)
  AS 'full name'
FROM books;

SELECT author_fname AS first, author_lname AS last,
  CONCAT(author_fname, ' ', author_lname) AS full
FROM books;

SELECT author_fname AS first, author_lname AS last,
  CONCAT(author_fname, ', ', author_lname) AS full
FROM books;

SELECT CONCAT(title, '-', author_fname, '-', author_lname) FROM books;

SELECT
    CONCAT_WS(' - ', title, author_fname, author_lname)
FROM books;

-- SUBSTRING
SELECT SUBSTRING('Hello World', 1, 4);

SELECT SUBSTRING('Hello World', 7);

SELECT SUBSTRING('Hello World', 3, 8);

SELECT SUBSTRING('Hello World', 3);

SELECT SUBSTRING('Hello World', -3);

SELECT SUBSTRING('Hello World', -7);

SELECT title FROM books;

SELECT SUBSTRING("Where I'm Calling From: Selected Stories", 1, 10);

SELECT SUBSTRING(title, 1, 10) FROM books;

SELECT SUBSTRING(title, 1, 10) AS 'short title' FROM books;

SELECT SUBSTR(title, 1, 10) AS 'short title' FROM books;

SELECT CONCAT
    (
        SUBSTRING(title, 1, 10),
        '...'
    )
FROM books;


-- REPLACE

SELECT REPLACE('Hello World', 'Hell', '%$#@');

SELECT REPLACE('Hello World', 'l', '7');

SELECT REPLACE('Hello World', 'o', '0');

SELECT REPLACE('HellO World', 'o', '*');

SELECT
  REPLACE('cheese bread coffee milk', ' ', ' and ');

SELECT REPLACE(title, 'e ', '3') FROM books;

-- SELECT
--    CONCAT
--    (
--        SUBSTRING(title, 1, 10),
--        '...'
--    ) AS 'short title'
-- FROM books;

SELECT
    SUBSTRING(REPLACE(title, 'e', '3'), 1, 10)
FROM books;

SELECT
    SUBSTRING(REPLACE(title, 'e', '3'), 1, 10) AS 'weird string'
FROM books;

-- REVERSE
SELECT REVERSE('Hello World');

SELECT REVERSE('meow meow');

SELECT REVERSE(author_fname) FROM books;

SELECT CONCAT('woof', REVERSE('woof'));

SELECT CONCAT(author_fname, REVERSE(author_fname)) FROM books;

-- CHAR_LENGTH

SELECT CHAR_LENGTH('Hello World');

SELECT author_lname, CHAR_LENGTH(author_lname) AS 'length' FROM books;

SELECT CONCAT(author_lname, ' is ', CHAR_LENGTH(author_lname), ' characters long') FROM books;

-- UPPER LOWER
SELECT UPPER('Hello World');

SELECT LOWER('Hello World');

SELECT UPPER(title) FROM books;

SELECT CONCAT('MY FAVORITE BOOK IS ', UPPER(title)) FROM books;

SELECT CONCAT('MY FAVORITE BOOK IS ', LOWER(title)) FROM books;

SELECT CONCAT(UPPER(author_fname, ' ', author_lname)) AS "full name in caps"
FROM books;

-- SOLUTIONS
SELECT REVERSE(UPPER('Why does my cat look at me with such hatred?'));


SELECT UPPER(REVERSE('Why does my cat look at me with such hatred?'));


I-like-cats


SELECT REPLACE(CONCAT('I', ' ', 'like', ' ', 'cats'), ' ', '-');


SELECT REPLACE(title, ' ', '->') AS title FROM books;



SELECT
   author_lname AS forwards,
   REVERSE(author_lname) AS backwards
FROM books;


SELECT
   UPPER
   (
      CONCAT(author_fname, ' ', author_lname)
   ) AS 'full name in caps'
FROM books;


SELECT
   CONCAT(title, ' was released in ', released_year) AS blurb
FROM books;
SELECT
   title,
   CHAR_LENGTH(title) AS 'character count'
FROM books;


SELECT
   CONCAT(SUBSTRING(title, 1, 10), '...') AS 'short title',
   CONCAT(author_lname, ',', author_fname) AS author,
   CONCAT(stock_quantity, ' in stock') AS quantity
FROM books;
