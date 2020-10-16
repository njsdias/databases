# **Relations: ONE to MANY**
For instance:
- one Book has many Reviews (one to many [1:many])
- one Review belongs to one book (one to one [1:1])
- several authors can written more one book (many to many [many:many])

## **Customers & Orders [1:many]**
One customer has many orders. One order has one customer associated with it.

We want to store:
- a customer's first and last name;
- a customer's email;
- the date of the purchase;
- the price of the order.

The avoid duplication and missing values are only the two problems that we can find in a real database. to avoid these problems it is better has the data stores in two tables:
 - customers: customer_id (PK), first_name, last_name, email
 - orders: order_id(PK), order_date, amount, customer_id(FK)

- PK: primary key
- FK: foreign key

To create the two tables just run the file: customers_clients.sql .

# **CROSS JOIN or CARTESIAN JOIN**

What are the orders did by Boy George?

    SELECT * from orders WHERE customer_id = (
        SELECT id FROM customers
        WHERE last_name='George'
        );

    SELECT * FROM customers, orders;

It gives all possible combination. It is not answer our main question.

# **INNER JOIN**
Gives the values in common that are in the two tables.
Select all records from A and B where the join condition is met.
Interception values between two tables. Used the most of the time.


We want a table that gives us first_name, last_name, email and orders.

- Implicit Inner Join

      SELECT first_name, last_name, order_date, amount, orders.id as 'orders' FROM customers, orders
      WHERE customers.id = orders.customer_id;

- Explicit Inner Join: We pick the data from _customers_ table and we join with _orders_ table where (customers.id = orders.customer_id). We can use INNER JOIN or simply JOIN.

      SELECT first_name, last_name, order_date, amount, orders.id as 'orders' FROM customers
      INNER JOIN orders ON customers.id = orders.customer_id;

- Total spent by customer

      SELECT ANY_VALUE(first_name), ANY_VALUE(last_name), SUM(amount) AS total_spent FROM customers
      INNER JOIN orders ON customers.id = orders.customer_id
      GROUP BY orders.customer_id
      ORDER BY total_spent DESC;

# **LEFT JOIN**
Select everything from A, along with any matching records in B.
Takes all from A inclusive what is common with B. If it is not found
any match we will see NULL values.

    SELECT first_name, last_name, order_date, amount, orders.id as 'orders' FROM customers
    LEFT JOIN orders ON customers.id = orders.customer_id;

In this situation we get some NULL values in the _amount_ and _orders_ columns. This is due to on _orders_ table (Table B) we don't
have orders for customer_id =  3 and 4. So, the result show us a table with all customers but some of them don't have any order.

- Get the total of orders per customer and those customers that didn't have any order get zero value.

      SELECT ANY_VALUE(first_name), ANY_VALUE(last_name), IFNULL(SUM(amount),0) AS total_spent FROM customers
      LEFT JOIN orders ON customers.id= orders.customer_id
      GROUP BY customers.id
      GROUP BY total_spent;

# **RIGHT JOIN**
Select everything from B, along with any matching records in A.
Takes all from B inclusive what is common with A. If it is not found
any match we will see NULL values.


     SELECT  * FROM customers
     RIGHT JOIN orders
        ON customers.id=orders.customer_id;


**NOTE**
The command ON DELETE CASCADE allows us to delete a customer in _customers_ table and the correspondent record in the _orders_ table.

    CREATE TABLE orders (
      id INT AUTO_INCREMENT PRIMARY KEY,
      order_date DATE
      amount DECIMAL(8,2)
      customer_id INT,
      FOREIGN KEY (customer_id)
          REFERENCES customers(id)
          ON DELETE CASCADE
      )

# **Exercise Solutions**

    CREATE DATABASE students_papers;
    USE students_papers;

    CREATE TABLE students(
      id INT AUTO_INCREMENT PRIMARY KEY,
      first_name VARCHAR(100)
    );

    CREATE TABLE papers(
      title VARCHAR(100),
      grade INT,
      student_id INT,
      FOREIGN KEY (student_id)
        REFERENCES students(id)
        ON DELETE CASCADE
      );

    INSERT INTO students (first_name) VALUES
    ('Caleb'),
    ('Samantha'),
    ('Raj'),
    ('Carlos'),
    ('Lisa');

    INSERT INTO papers (student_id, title, grade ) VALUES
    (1, 'My First Book Report', 60),
    (1, 'My Second Book Report', 75),
    (2, 'Russian Lit Through The Ages', 94),
    (2, 'De Montaigne and The Art of The Essay', 98),
    (4, 'Borges and Magical Realism', 89);

1- Build a output with columns first_name, title, grade.

    SELECT first_name, title, grade FROM papers
    INNER JOIN students
    ON students.id = papers.student_id
    ORDER BY grade DESC;

2- Build a output with columns first_name, title, grade
that appears NULL values on title and on grade columns.

    SELECT first_name, title, grade
    FROM students
    LEFT JOIN papers
    ON students.id = papers.student_id;


3- Build a output with columns first_name, title, grade
that appears NULL values on title and on grade columns.
For NULL values in title change to MISSING and for NULL
values for grade change to 0.

    SELECT first_name,
           IFNULL(title, 'MISSING') AS title,
           IFNULL(grade,0)  AS grade
    FROM students
      LEFT JOIN papers
      ON students.id = papers.student_id;

4- Build a output with columns first_name and average()
For NULL values in average change to 0.

    SELECT first_name,
           IFNULL(AVG(grade),0) AS average
    FROM students
      LEFT JOIN papers
      ON students.id = papers.student_id
    GROUP BY students.first_name
    ORDER BY average DESC;

5- Build a output with columns first_name, average(grade) and passing_values. For NULL values in average change to 0. On column passing values write:
- PASSING: for cases when grade is <= 75,
- FAILING: for the other cases.

        SELECT first_name,
               IFNULL(AVG(grade),0) AS average,
               CASE
                  WHEN AVG(grade) IS NULL THEN 'FAILING'
                  WHEN AVG(grade) >= 75 THEN 'PASSING'
                  ELSE 'FAILING'
                END AS passing_status
        FROM students
          LEFT JOIN papers
          ON students.id = papers.student_id
        GROUP BY students.first_name
        ORDER BY average DESC;
