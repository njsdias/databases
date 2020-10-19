import sqlite3
import os

# remove de db if you already have in your disk
os.system('rm customer.db')
# clear the window before display results
os.system('clear')


# it allow us to save the database in memory
# conn = sqlite3.connect(':memory:')

# connect to a database
#  if it do not exist it is created in this folder
conn = sqlite3.connect('customer.db')

# create a cursor
# This allows us to create tables and do operations with tables
c = conn.cursor()

# create a table
c.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        first_name text,
        last_name text,
        email text
        ) 
    """)


# this put table in database
# It is like a push to database (repository in github)
# commit our command (c.execute)
conn.commit()


# insert multi-values on a table
many_customers = [('John', 'Elder', 'john@codemy.com'),
                  ('Tim', 'Smith', 'rim@codemy.com'),
                  ('Mary', 'Brown', 'mary@codemy.com'),
                  ('Wes', 'Brown', 'wes@brown.com'),
                  ('Steph', 'Kuewa', 'steph@kuewa.com'),
                  ('Dan', 'Pas', 'dan@pas.com'),]

c.executemany("""
    INSERT INTO customers VALUES (?,?,?)""", many_customers)
conn.commit()


# Query the Database
c.execute("SELECT rowid, * FROM customers")
# gather results of the query
# it returns a list of tuples
items = c.fetchall()
for item in items:
    # print(item[0] + " " + item[1] + "\t " + item[2])
    print(item)

# Using WHERE
print('\n Using WHERE')
c.execute("""
    SELECT * FROM customers 
    WHERE last_name = 'Elder'
""")
items = c.fetchall()
for item in items:
    print(item)


# Using WHERE and LIKE
print('\n Using WHERE and LIKE')
c.execute("""
    SELECT * FROM customers 
    WHERE last_name LIKE 'Br%'
""")
items = c.fetchall()
for item in items:
    print(item)

# Using WHERE and LIKE
print('\n Using WHERE and LIKE')
c.execute("""
    SELECT * FROM customers 
    WHERE email LIKE '%codemy.com'
""")
items = c.fetchall()
for item in items:
    print(item)

# Update Records
print('\n Update Results...')
c.execute("""
    UPDATE customers 
    SET first_name = 'Bob'
    WHERE rowid = 1
""")
conn.commit()


print('\n Select all records to see the Update results')
c.execute("""
    SELECT * FROM customers 
""")
items = c.fetchall()
for item in items:
    print(item)


# Delete Records
print('\n Delete Results...')
c.execute("""
    DELETE FROM customers 
    WHERE rowid = 6
""")
conn.commit()


print('\n Select all records to see the Delete results')
c.execute("""
    SELECT * FROM customers 
""")
items = c.fetchall()
for item in items:
    print(item)

# Order Results: ORDER BY
print('\n Order By using: rowid')
c.execute("""
    SELECT rowid, * FROM customers
    ORDER BY rowid DESC 
""")
items = c.fetchall()
for item in items:
    print(item)

# Order Results: ORDER BY
print('\n Order By using: last_name')
c.execute("""
    SELECT rowid, * FROM customers
    ORDER BY last_name DESC 
""")
items = c.fetchall()
for item in items:
    print(item)


# close connection
conn.close()




