# **MANY:MANY**

## **Database Description**
This database is related with TV series and contains three tables:
- reviewers: id, first_name, last_name
- series: id, title, released_year, genre  
- reviewer: id, rating, series_id, reviewer_id

A reviewer as a persons has a name (first and last) and is identified by an ID.
The person do series reviews. Series have a title, a release year, a genre and
it is identified as a ID. Series receives a rating and each that is identified by an ID, who did the review for which serie.

To create the databse anda the tables runs the script that is in file:
- /sql_sources/tv_shows.sql

# **Exercises**

1- Create a table that contains titles and ratings.

    SELECT title, rating FROM reviews
    LEFT JOIN series
    ON reviews.series_id = series.id;

    SELECT title, rating FROM reviews
    INNER JOIN series
    ON reviews.series_id = series.id;

2- Create a table with title and average rating.

    SELECT title, AVG(rating) AS avg_rating FROM reviews
    INNER JOIN series
    ON reviews.series_id = series.id
    GROUP BY series.id
    ORDER BY avg_rating;

3- Build a table with contains the ratings for each reviewer: first_name, last_name and rating.

    SELECT first_name, last_name, rating FROM reviewers
    INNER JOIN reviews
    ON reviews.reviewer_id = reviewers.id;

4- Build a table that shows an unreviewed serie.

    SELECT title, rating FROM series
    LEFT JOIN reviews
    ON series.id =  reviews.series_id
    WHERE rating is NULL;

5- Build a table that gives the rating average by serie genre.

    SELECT genre, ROUND(AVG(rating),2) AS avg_rating from series
    INNER JOIN reviews
    ON reviews.series_id = series.id
    GROUP BY series.genre;

6- Build a table that contains per reviewer:
- first_name, last_name;
- COUNT: amount of reviews the reviewer did
- the MIN, MAX and AVG of ratings
- STATUS:
  - ACTIVE if COUNT>0
  - ELSE INACTIVE

        SELECT first_name, last_name,
          COUNT(rating),
          IFNULL(MIN(rating),0) AS MIN,
          IFNULL(MAX(rating),0) AS MAX,
          IFNULL(ROUND(AVG(rating),2),0) AS AVG,
          CASE
            WHEN COUNT(rating) > 0 THEN 'ACTIVE'
            ELSE 'INACTIVE'  
          END AS STATUS
        FROM reviewers
        LEFT JOIN reviews
        ON reviews.reviewer_id = reviewers.id
        GROUP BY reviewers.id;

7- Build a table with title, rating, reviewer (first_name and last_name)

    SELECT title, rating, CONCAT(first_name,' ', last_name) AS reviewer
    FROM reviewers
    INNER JOIN reviews
        ON reviewers.id = reviews.reviewer_id
    INNER JOIN series
        ON series.id = reviews.series_id
    ORDER BY title;
