# **AGGREGATE FUNCTIONS**

## **COUNT**

Count the records in the selection procedure

- Gives how many books we have in the table

      SELECT COUNT(*) FROM books;

- How many unique authors we have in the table?

      SELECT COUNT(DISTINCT author_lname, author_fname) FROM books;

- How many titles contains "the"?

    SELECT COUNT(*) FROM books
    WHERE title LIKE ('%the%');

## **GROUP BY**

Check your MySQL Server version. My version is:

- mysql  Ver 14.14 Distrib 5.7.31, for Linux (x86_64) using  EditLine wrapper

If you have any error using GROUP BY check this [site](https://dev.mysql.com/doc/refman/8.0/en/group-by-handling.html).

- Count how many books each author has written.

      SELECT ANY_VALUE(author_lname), COUNT(*) FROM books
      GROUP BY author_lname;

      SELECT author_fname, author_lname, COUNT(*) FROM books
      GROUP BY author_lname, author_fname;

- How many books were released by year?      

      SELECT CONCAT('In ', released_year,' ',COUNT(*), ' book(s) released') AS 'Release books by year' from books
      GROUP BY released_year;

## **MIN and MAX**

- Gives the year when the oldest book was released.

      SELECT MIN(released_year) from books;

- Who wrote the book with more pages? What is the title of this book? Here we are using **Sub-queries**. **Note** the sub-query is executed first. This is slow because it is running two queries.

      SELECT * FROM books
      WHERE pages=(
        SELECT MAX(pages) FROM books);

  - We can do the same using ORDER BY

        SELECT *  FROM books
        ORDER BY pages DESC LIMIT 1;

- Find the year each author published their first book.

      SELECT author_fname, author_lname, MIN(released_year) FROM books
      GROUP BY author_lname, author_fname
      ORDER BY MIN(released_year);

- Find the longest page count for each author.

      SELECT author_fname, author_lname, MAX(pages) FROM books
      GROUP BY author_lname, author_fname
      ORDER BY MAX(pages) DESC;

      SELECT CONCAT(author_fname, ' ',author_lname) AS author, MAX(pages) AS 'longest book' FROM books
      GROUP BY author_lname, author_fname;

- The same as the last one but showing all collumns

      SELECT * FROM books t1
      WHERE (t1.author_fname, t1.author_lname, t1.pages) =
        ANY(
          SELECT t2.author_fname, t2.author_lname, MAX(t2.pages) FROM books t2
          GROUP BY t2.author_lname, t2.author_fname
          ORDER BY MAX(t2.pages) DESC
        )
        ORDER BY t1.pages DESC;

## **SUM**

- How many pages each author wrote so far?

      SELECT author_fname, author_lname, SUM(pages) FROM books
      GROUP BY  author_lname, author_fname;

## **AVERAGE**

- Calculate the average stock quantity for books released in the same year

      SELECT released_year, AVG(stock_quantity) FROM books
      GROUP BY released_year;

- Calculate the average pages published by each author

      SELECT author_fname, author_lname, AVG(pages) FROM books
      GROUP BY author_lname, author_fname;

# **EXERCISE SOLUTIONS**

1- Print out the number of books in the database

    SELECT COUNT(*) FROM books;

2- Print out how many books were released in each year

    SELECT released_year, COUNT(*) FROM books
    GROUP BY released_year
    ORDER BY released_year;

3- Print out the total number of books in stock

    SELECT SUM(stock_quantity) FROM books;

4- Find the average year for each author

    SELECT author_fname, author_lname, AVG(released_year) FROM books
    GROUP BY author_lname, author_fname;

5- Find the full name of the author who wrote the longest book

    SELECT CONCAT(author_fname, ' ', author_lname), pages FROM books ORDER BY pages DESC LIMIT 1;

6- Make a table with year, number of books released, average of pages.

    SELECT released_year AS year, COUNT(*) AS '# books', AVG(pages) AS 'avg pages' FROM books
    GROUP BY released_year
    ORDER BY released_year;
