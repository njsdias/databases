# **Instagram Questions**

Run instagram_db_v2.sql file stored in instagram_database folder and answer the next questions using SQL: Structured Query Language.

1-We want to reward or users who have been around the longest.

SELECT * FROM users
ORDER BY created_at ASC LIMIT 5;


2- What day of the week do most users register on?

    SELECT DAYNAME(created_at) as day,
      COUNT(*) AS total FROM users
      GROUP BY day
      ORDER BY total DESC;

3- We want to target our inactive users with an email campaign. An inactive user is an user who have never posted a photo.

    SELECT username, user_id FROM users
    LEFT JOIN photos
    ON photos.user_id = users.id
    WHERE user_id IS NULL ;

4- Who can get the most likes on a single photo?

    SELECT
        photo_id,
        photos.user_id,
        username,
        COUNT(*) AS total
    FROM likes
    INNER JOIN photos
        ON likes.photo_id = photos.id
    INNER JOIN users
        ON users.id = photos.user_id  
      GROUP BY photo_id
      ORDER BY total DESC LIMIT 1;

5- How many times does the average user post?

    SELECT
      (SELECT COUNT(*) from photos)
      /
      (SELECT COUNT(*) from users) As average;


6- A brand wants to know which hashtags to use in a post.
What are the top 5 commonly used hashtags?

      SELECT tag_name, COUNT(*) as total FROM photo_tags
      INNER JOIN tags
        ON tags.id = photo_tags.tag_id
      GROUP BY tag_id
      ORDER BY total DESC
      LIMIT 5;

7- Find users who have liked every single photo on the site.

    SELECT user_id, username, count(*) AS total from likes
        INNER JOIN users
          ON users.id = likes.user_id
        GROUP BY user_id
        HAVING total = (SELECT COUNT(*) FROM photos);
