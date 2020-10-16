# **LOGICAL OPERATORS**

## **NOT EQUAL (!=)**

- Books that were not released in 2017.

      SELECT title FROM books
      WHERE year!=2017;

## **NOT LIKE**

- Select books with titles that don't start with 'W'

      SELECT title FROM books
      WHERE title NOT LIKE 'W%';

## **GREATER THAN**

- Select books released after the year 2000

      SELECT * FROM books
      WHERE released_year > 2000;

## **GREATER THAN OR EQUAL TO**

- Select books released after the year 2000 including 2000 year

      SELECT * FROM books
      WHERE released_year >= 2000;

## **AND / &&**

All conditions need to be true.

- Select books written by Dave Eggers, published after the year 2010.

      SELECT title,author_fname, author_lname, released_year FROM books
      WHERE CONCAT(author_fname, ' ',author_lname) = 'Dave Eggers' AND released_year > 2010;

- Select books written by Dave Eggers, published after the year 2010 and contains 'novel' in the title.

      SELECT * FROM books
      WHERE CONCAT(author_fname, ' ',author_lname) = 'Dave Eggers'
      AND released_year > 2010 AND title LIKE '%novel%';

## **OR / ||**

At least one condition needs to be true.

- Select books written by Dave Eggers or published after the year 2010.

      SELECT title,author_fname, author_lname, released_year FROM books
      WHERE CONCAT(author_fname, ' ',author_lname) = 'Dave Eggers' OR released_year > 2010;

## **BETWEEN / NOT BETWEEN***

- Shows the books published between 2010 and 2015.

      SELECT title, released_year FROM books
      WHERE released_year BETWEEN 2004 AND 2015;

it is equal to

    SELECT title, released_year FROM books
    WHERE released_year >= 2004 AND released_year <= 2015
    ORDER BY released_year;

## **CAST and BETWEEN**

For the best results when using BETWEEN with data or time, use CAST() to explicitly convert the values to the desired data type.
For instance,

      SELECT name, birthdt FROM people
      WHERE birthdt BETWEEN CAST('1980-01-01' AS DATETIME)
      AND CAST('2000-01-01' AS DATETIME);

## **IN / NOT IN**

Select all books written by 'Carver', 'Lahiri', 'Smith'.

    SELECT title, author_lname FROM books
    WHERE author_lname='Carver' OR
          author_lname='Lahiri' OR
          author_lname='Smith';

    SELECT title, author_lname FROM books
    WHERE author_lname IN ('Carver',
          author_lname='Lahiri',
          author_lname='Smith');
Select books released in 2017 or in 1985 years.

    SELECT title, released_year FROM books
    WHERE released_year IN (2017, 1985);

Select all books not publish in 2000 until 2016.   

    SELECT title, released_year FROM books
    WHERE released_year NOT IN (2000, 2002, 2004, 2006,
      2008, 2010, 2012, 2014, 2016);

- It selects books that are inside of 2000's and are not belong to
the next years 2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016.

      SELECT title, released_year FROM books
      WHERE released_year >= 2000
      AND released_year NOT IN (2000, 2002, 2004, 2006,
      2008, 2010, 2012, 2014, 2016);

## **MODULO %**
- A more elegant solution is using module or the rest of a division once hour years are even years.

      SELECT title, released_year FROM books
      WHERE released_year >= 2000
      AND released_year % 2 != 0;


## **CASE**

Imagine you want categorize books using the published year:
  - books published in 2000's will be 'Modern Lit'
  - books published before 200's will be '20th Century Lit'

        SELECT title, released_year,
          CASE
            WHEN released_year >= 2000 THEN 'Modern Lit'
            ELSE '20th Century Lit'
          END AS GENRE
        FROM books;

Imagine you want categorize the book quantities with stars:
- one star(*) for low stock
- two stars(* *) for medium stock
- three stars(* * *) for high stock

        SELECT title, stock_quantity,
          CASE
            WHEN stock_quantity BETWEEN 0 AND 50 THEN '*'
            WHEN stock_quantity BETWEEN 51 AND 100 THEN '* *'
            WHEN stock_quantity BETWEEN 101 AND 300 THEN '* * *'
            ELSE '* * * *'
          END AS STOCK
        FROM books;


        SELECT title, stock_quantity,
          CASE
            WHEN stock_quantity <= 50 THEN'*'
            WHEN stock_quantity <= 100 THEN '* *'
            WHEN stock_quantity <= 300 THEN '* * *'
            ELSE '* * * *'
          END AS STOCK
        FROM books;

# **Exercise Solutions**

- Select all books written before 1980 (non inclusive)

      SELECT title, released_year FROM books
      WHERE released_year < 1980;

- Select all books written by Eggers or Chabon

      SELECT title, author_lname FROM books
      WHERE  author_lname = 'Eggers' OR
             author_lname = 'Chabon';

- Select all books written by Lahiri, published after 2000

      SELECT title, author_lname, released_year FROM books
      WHERE  author_lname = 'Lahiri' AND
             released_year > '2000';

- Select all books with page counts between 100 and 200.

    SELECT title, pages FROM books
    WHERE  pages BETWEEN 100 AND 200;

- Select all books where author_lname starts with a 'C or and 'S'

    SELECT author_lname, title FROM books
    WHERE author_lname LIKE 'C%' OR
          author_lname LIKE 'S%';

- Categorize 'title' as:
    - if contains 'stories' -> 'Short Stories'
    - if contains 'Just kinds' and 'A Heartbreaking Work' -> 'Memoir'
    - everything else -> 'Novel'

          SELECT title, author_lname,
            CASE
              WHEN title LIKE '%stories%' THEN 'Short Stories'
              WHEN title LIKE '%Just Kids%' OR  title LIKE '%A Heartbreaking Work%' THEN 'Memoir'
              ELSE 'Novel'
            END AS TYPE
            FROM books;

- Build a table where you have author_fname, author_lname and how many book(s) each author published

          SELECT author_fname, author_lname,
            CASE
              WHEN COUNT(*) = 1 THEN '1 book'
              ELSE CONCAT(COUNT(*), ' books')
            END AS COUNT
          FROM books
          GROUP BY author_fname, author_lname;
