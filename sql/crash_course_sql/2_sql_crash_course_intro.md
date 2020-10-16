
# **The Ultimate MySQL Bootcamp Go from SQL Beginner to Expert**

The best way is start to do simple code and understand the commands interpreting the results obtained.

Go to the [website](http://w3schoools.com) and type the next code

    SELECT
      customerName,
      COUNT(*) AS 'number of orders'
    FROM customers
    INNER JOIN orders
	   ON orders.customerID = customers.customerID
    GROUP BY customers.customerID

First, it counts how many times a customer appears in the table Customers. Second, it do an INNER JOIN with the table Orders using the key _customers.id_. Finally, the result is grouped by customer. The results gives us a table with two columns:
- customerName
- number of Orders
- and shows how many times a customer required an order.

# **Simple commands**

To present you which databases (DB) you have in your MySQL Server

    SHOW Databases;

To create a DB.

    CREATE DATABASE <name>;

To drop a DB

    DROP DATABASE <name>;

To use a DATABASE

    USE <database_name>;

To current use the database

    SELECT database();


**NOTES**

- A Database is a bunch of tables (in relational databases)
- Tables holds data
- A table has several Columns (or Headers) and Rows (tabular format)


# **Data Types**

When we create a table we need to specify the type of the data
provided for each column. For instance:

  - INT: to represent numbers
  - CHAR : to limit a set of characters
  - VARCHAR: to represent strings (1-255 characters)
    - VARCHAR(100) to specify the maximum is 100 characters

# **Create Tables**

    CREATE TABLE tablename
    (
      column_name data_type,
      column_name data_type
    );


# **Deleting Tables**

    DROP TABLE tablename;

# **A simple example**

In this example you create a DATABASE named _cats_ (always in plural),
indicate that you want to use this DATABASE and CREATE  TABLE named as cat_app
that has two columns: name and age

    CREATE DATABASE cat_app;

    USE cat_app;

    CREATE TABLE cats (
    name VARCHAR(100),
    age INT
    );

To have sure you did the right job, you can ask to see the table:

    SHOW TABLES;

or

    DESC <tablename>;

# **Insert Values**

    INSERT INTO cats(name, age)
    VALUES ("Jetson", 7);

or insert multiple values

    INSERT INTO cats(name, age)
    VALUES ('Charlie', 10),
          ('Sadie, 3'),
          ('Lazy Bear', 1)


# **NULLS**
 When you do

    DESC tablename

you can see a column NULL with
YES values. It means that, the
field accepts NULL values. In other words, if you don't provide any values MySQL fill it with word NULL.

To not allow NULL values, you need to specify you don't allow NULL values in the fields:


    CREATE TABLE cats2
    (
      name VARCHAR(100) NOT NULL,
      age INT NOT NULL
      );

In this case if you don't provide a value for a field
the value by DEFAULT is:
- for a VARCHAR: an empty string;
- for a INT: zero value

# **Default Values**

    CREATE TABLE cats3
    (
        name VARCHAR(100) DEFAULT 'unnamed',
        age INT DEFAULT 99
      );


In this case the table not allow the word NULL

      CREATE TABLE cats4
      (
          name VARCHAR(100) NOT NULL DEFAULT 'unnamed',
          age INT NOT NULL DEFAULT 99
        );


**WARNINGS**
 To see a descriptions of a warning type:

     SHOW WARNINGS;

# **KEYS**

## **Primary Key**
It is a column that has a unique value that can be used to identify each record in the table.

    CREATE TABLE unique_cats(
      cat_id INT NOT NULL,
      name VARCHAR(100),
      age INT,
      PRIMARY KEY (cat_id)
      );


To automatize the fill of primary key field add AUTO_INCREMENT, like this

    CREATE TABLE unique_cats(
      cat_id INT NOT NULL AUTO_INCREMENT,
      name VARCHAR(100),
      age INT,
      PRIMARY KEY (cat_id)
      );

When you do

    DESC unique_cats;

you will see cat_id has the value PRI in the Key column. When you set a field as Primary Key it is not allow a duplicate entry.

    INSERT INTO unique_cats(name, age)
    VALUES("James", 3);

More than that you can have more than one cat with the same name.

    CREATE TABLE employees(
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        last_name VARCHAR(30) NOT NULL,
        first_name VARCHAR(30) NOT NULL,
        middle_name VARCHAR(30),
        age INT NOT NULL,
        current_status VARCHAR(30) NOT NULL DEFAULT 'employed');

    INSERT INTO employees (first_name, last_name, age)
    VALUES ('Dora', 'Smith', 58);


# **CRUD**: Create , Read, Update, Delete

**Delete the Table cats**

      DROP TABLE cats;

**Re-create the table**

    CREATE TABLE cats(
      cat_id INT NOT NULL AUTO_INCREMENT,
      name VARCHAR(100),
      breed VARCHAR(100),
      age INT,
      PRIMARY KEY (cat_id)
      );

    INSERT INTO cats(name, breed, age)
    VALUES ('Ringo', 'Tabby', 4),
           ('Cindy', 'Maine Coon', 10),
           ('Dumbledore', 'Maine Coon', 11),
           ('Egg', 'Persian', 4),
           ('Misty', 'Tabby', 13),
           ('George Michael', 'Ragdoll', 9),
           ('Jackson', 'Sphynx', 7);

## Refine the **SELECT** with **WHERE** command

    SELECT * FROM cats WHERE age=4;
    SELECT * FROM cats WHERE name='Egg';

    SELECT cat_id FROM cats;
    SELECT name, breed FROM cats;

    SELECT name, age FROM cats
    WHERE breed='Tabby';

    SELECT cat_id, age FROM cats
    WHERE cat_id = age;

## ALIAS

Alias is usually used when you are working with several tables at same table. It gives a new name to your selection. Here only a few simple examples, using only one table.

    SELECT cat_id AS id, name FROM cats;

    SELECT name AS 'cat name', breed AS 'kitty breed' FROM cats;

# **UPDATE: Modify a value into a table**

        UPDATE cats
        SET age = 13
        WHERE name = 'Charlie';

        UPDATE cats
        SET name='Jack'
        WHERE name='Jackson';

        UPDATE cats
        SET breed='British Shorthair'
        WHERE name='Ringo';

        UPDATE cats
        SET age=12
        WHERE breed='Maine Coon';

# **DELETE Command**

        DELETE FROM cats WHERE name='egg';

        DELETE FROM cats WHERE age='4';
        DELETE FROM cats WHERE age=cat_id;


**Warning:**
It deletes everything from table cats

        DELETE FROM cats;


**Important Rule of Thumb:**
Before use **UPDATE** and **DELETE** use **SELECT**
to be sure you are catching the records of your interest.

    SELECT FROM * from CATS WHERE breed="Maine Coon";
