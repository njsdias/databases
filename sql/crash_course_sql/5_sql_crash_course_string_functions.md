# **String Functions**

First task is search for string functions in Google and go to MySQL documentation page to figure out which
string functions are available.

# **CONCAT**

When you want combine data.

    CONCAT(column, anotherColumn)

    CONCAT(column, 'text', anotherColumn, 'more text')

- Adding space between texts

      CONCAT(column, ' ', anotherColumn, ' ')

      SELECT CONCAT('Hello', ' ', 'World');

- Create a column full_name with a author full name

      SELECT CONCACT(author_fname,' ', author_lname) AS full_name FROM books;

# **CONCAT_WS (with separator)**

      SELECT
          CONCAT_WS('-'. title, author_fname, author_lname)
      FROM books;

# **SUBSTRING**

      SELECT SUBSTRING('Hello World', 1, 4);

      Result: Hell (from 1rst character to 4 character)

      SELECT SUBSTRING('Hello World', 1, 4);

      Result: World (from 7th until the end)

      SELECT SUBSTRING('Hello World', -3);

      Result: World (from the end until 3rth character)

- Select the first ten characters in each string.
      SELECT SUBSTRING(title, 1,10) AS 'short title' FROM books;

- Combine functions: It selects the first 10 characters of a string and add the '...' using CONCAT function, which concatenate two strings.
        SELECT
            CONCAT
            (
              SUBSTRING(title, 1, 10),
              '...'
            )
        FROM books;

# REPLACE
Replace a string by other string.

        SELECT REPLACE('Hello World', 'Hell', '%$#@');

        Result: %$#@o World

        SELECT REPLACE('Hello World', 'l', '7');

        Result: He77o Word7d

# REVERSE

        SELECT REVERSE('Hello World')

        Result: dlroW olleH

# CHAR_LENGTH
Gives how much characters that we have in the string

        CHAR_LENGTH('Hello World')

        Result: 11

# UPPER and LOWER

Convert strings to up or lower case strings. The next code converts all strings to upper case in title column from books table.

    SELECT UPPER(title) FROM books;


REVERSE( UPPER("Why does my cat look at me with such hatred?"));
