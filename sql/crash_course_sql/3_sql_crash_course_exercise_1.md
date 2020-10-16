# Exercises using Fundamental Commands

- Create Database
- Use Database
- Read Records
- Update Records
- Delete Records

      create database shirts_db;

      use shirts_db;

      create table shirts(
        shirt_id INT NOT NULL AUTO_INCREMENT,
        article VARCHAR(100),
        color VARCHAR(100),
        shirt_size VARCHAR(100),
        last_worn INT,
        PRIMARY KEY (shirt_id)
        );

      DESC shirts;

      INSERT INTO shirts(article, color, shirt_size, last_worn) VALUES
                        ('t-shirt', 'white', 'S', 10),
                        ('t-shirt', 'green', 'S', 200),
                        ('polo shirt', 'black', 'M', 10),
                        ('tank top', 'blue', 'S', 50),
                        ('t-shirt', 'pink', 'S', 0),
                        ('polo shirt', 'red', 'M', 5),
                        ('tank top', 'white', 'S', 200),
                        ('tank top', 'blue', 'M', 15);

      SELECT * FROM shirts;

      INSERT INTO shirts(color, article, shirt_size, last_worn)
                  VALUES('purple', 'polo shirt', 'medium', 50);

      SELECT * FROM shirts;

      SELECT article, color, shirt_size FROM shirts
           WHERE shirt_size='medium';

      UPDATE shirts
      SET shirt_size="M"
      WHERE shirt_size="medium";

      UPDATE shirts
      SET shirt_size='L'
      WHERE article='polo shirt';

      UPDATE shirts
      SET last_worn= 0
      WHERE last_worn=15;

      SELECT article, color, shirt_size FROM shirts
      WHERE color='white';

      UPDATE shirts
      SET color='off white', shirt_size='XS'
      WHERE color='white';

      DELETE FROM shirts
      WHERE last_worn=200;

      DELETE FROM shirts
      WHERE article='tank top';

      DELETE FROM shirts;

      DROP TABLE shirts;

      DROP DATABASE shirts_db;
