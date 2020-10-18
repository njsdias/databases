
# **The Ultimate MySQL Bootcamp go from SQL Beginner to Expert**

# **Course Content**
- Linux MySQL Installation
- Create Databases and Tables
- String Functions, Aggregation Functions
- JOINS: Inner, Left, Right and amoung more than two tables
- Instagram Project: Build Database and Tables.
- Website Development using node.js


# **My SQL Installation**

The next installation steps are for Ubuntu (Debian) OS.

- sudo apt update
- sudo apt upgrade
- sudo apt install mysql-server

      reply with: Y

- mysql version

      output is: mysql  Ver 14.14 Distrib 5.7.31, for Linux (x86_64) using  EditLine wrapper

- sudo mysql_secure_installation
    - reply with: Y
    - choose the strength of your password
    - type your password
    - confirm the password

- the next few question answer with: Y

- sudo mysql -u root -p -> only needed for the first time that you enter in MySQL

- on the MySQL prompt type:

      SHOW DATABASES;
- to exit from MySQL type in the prompt: exit
