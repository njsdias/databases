# **Refine Selection**
- Limiting the results that appears
- Sort in alphabetic order
- Sort in numeric order
- Unique results back

# **DISTINCT**
Give the unique records.

    SELECT DISTINCT author_lname FROM books;

- Gives the distinct authors using the full full_name

    SELECT DISTINCT CONCAT(author_lname, ' ',author_lname)
     FROM books;

    SELECT DISTINCT author_fname, author_lname FROM books;


# **ORDER BY**

- If you add DESC at the end the results are order in the reverse way.

        SELECT author_lname FOM BOOKS ORDER BY author_lname;

        SELECT title, released_year, pages FROM books ORDER BY released_year;

-After order by last name  the order by first name

        SELECT author_fname, author_lname FROM books
        ORDER BY author_lname, author_fname;

# **LIMIT**

Shows a LIMIT records by given a number.

    SELECT title FROM books LIMIT 3;

    SELECT title, released_year FROM books ORDER BY released_year DESC LIMIT 5;

- Start from row 2 until to row 5

      SELECT title, released_year FROM books ORDER BY released_year DESC LIMIT 2,5;

# **LIKE**

Performance a better searching for data.

**WildCard %**

- It means contains 'da'. If we have 'da%'it means start with 'da'.
If we have '%da'it means ends with 'da'.

      SELECT title, author_fname FROM books WHERE author_fname LIKE '%da%';

- It means search titles with % character in title
      SELECT title FROM books WHERE title LIKE '%\%%';

**WildCard underscore**

- Select stock_quantity with two digits

      SELECT title, stock_quantity FROM books
      WHERE  stock_quantity LIKE '__';

- It means search titles with underscore character in title

      SELECT title FROM books WHERE title LIKE '%\_%';      


# **Exercise Solutions**

1- Select all story collections which contain the word: stories

    SELECT title FROM books WHERE title LIKE '%Stories%';

2- Find the Longest book. Print out the Title an the Pages.

    SELECT title, pages FROM books ORDER BY pages DESC LIMIT 1;

3- Print a summary containing the title and year, for the 3 most recent books

    SELECT CONCAT(title, '-', released_year) AS 'summary' FROM books
    ORDER BY released_year DESC LIMIT 3;

4- Find all books with and author_lname that contains a space character (" ")

    SELECT title, author_lname FROM books
    WHERE author_lname LIKE '% %';

5- Find the 3 books with the lowest stock quantity

    SELECT title, released_year, stock_quantity FROM books
    ORDER BY stock_quantity LIMIT 3;

6- Print title and author_lname, sorted first by author_lname and then by title  

    SELECT title, author_lname FROM books
    ORDER BY author_lname, title;

7- Make a column that shows:
- MY FAVORITE AUTHOR IS author_fname author_lname !
in which author_lname is alphabetic ordered.

      SELECT UPPER(CONCAT(
        'my favorite author is ',
        author_fname, ' ',
        author_lname)) AS 'something' FROM books
      ORDER BY author_lname;
