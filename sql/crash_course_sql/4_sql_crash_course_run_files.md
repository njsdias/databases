# How run SQL files from MySQL

You can have a dql file with that contains a bunch of commands.
As instance:

    DROP DATABASE IF EXISTS test_app;
    CREATE DATABASE test_app;
    USE test_app;

To run this commands using MySQL, xectute the command:

    source /path_to_source_file/file_name.sql

# **String Functions**

Run commands inside a file rather type commands in command line interface (CLI).

    This way it is:
    - most easy to fix errors
    - you have the history of your work
    - and share the content with people/team.
