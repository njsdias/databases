# **SQLITE3: First Examples**

In this example it is introduced SQLITE3 which is a framework
that allow us to work with DB without need to install 
any additional software. SQLI allow us to store a DB in memory
instead of hard disk. 

## **Simple Commands**
- To save the database in memory (creating a connection)
      
      conn = sqlite3.connect(':memory:')

- To created a DB in our folder if it do not exist (creating a connection) 

        conn = sqlite3.connect('customer.db')
        
- *cursor* allows to create and do operations with tables

        c = conn.cursor()

- To execute SQL commands

        c.execute(""" SQL commands """)
     
 - *commit* command is used after the *execute* command. It
 can be interpreted as doing a push to the table of execute results
 
        conn.commit()
 
 - It is to gather all results of a SELECT SQL command
 
        c.fetchall()
        
 - To close the connection
 
        conn.close()
        
# **Folder Structure** 
In folder intro/ we have a demonstration of the basic commands used in SQLite3.

In folder simple_app/ we have a more structured file split in functions and in
file simple_app/app.py execute those function in a sequential order.   
 
In folder db_created/ we find the database created. Before run the simple_app/app.py
we need to copy db_created/customer.db to folder simple_app/ . 
 
# **Result from "app"**

![app_sqlite](https://user-images.githubusercontent.com/37953610/96522845-3c28b200-126c-11eb-89d0-5f260ade57af.png)


 **More Information**

[SQLite Tutorial](https://www.pythoncentral.io/series/python-sqlite-database-tutorial/)


