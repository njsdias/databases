import sqlite3


def connect_db_cursor():
    """
    Connect to Database and Create a Cursor
    :return:
        conn: connection
        c: cursor
    """
    # connect to database
    conn = sqlite3.connect('simple_app/customer.db')

    # create a cursor
    c = conn.cursor()

    return conn, c


def show_all():
    """
    Query the DB and Return all record
    """

    print("\n Show all results...")

    # create to databse and create cursor
    conn, c = connect_db_cursor()

    # Query the database
    c.execute("SELECT rowid, * FROM customers")

    # gather all information using fetch
    items = c.fetchall()

    # show results from sql command
    for item in items:
        print(item)

    # close connection
    conn.close()


def add_one(first, last, email):
    """
    Adding one record to db
    """

    print("\n Add one record...")

    # create to databse and create cursor
    conn, c = connect_db_cursor()

    # add a record to table customer
    c.execute("""
        INSERT INTO customers VALUES
            (?,?,?)
    """, (first, last, email))

    # commit our command
    conn.commit()


def add_many(list):
    """
    Adding many records to db
    """

    print("\n Add one record...")

    # create to databse and create cursor
    conn, c = connect_db_cursor()

    # add a record to table customer
    c.executemany("INSERT INTO customers VALUES (?,?,?) ", list)

    # commit our command
    conn.commit()

    # close connection
    conn.close()


def delete_one(id):
    """
    Delete one record from db
    """

    print(f"\n Delete record number: {id}...")

    # create to databse and create cursor
    conn, c = connect_db_cursor()

    # add a record to table customer
    c.execute("""
        DELETE FROM customers 
        WHERE rowid = (?)
    """, id)

    # commit our command
    conn.commit()

    # close connection
    conn.close()


def email_lookup(email):

    """
    Delete one record from db
    """

    print(f"\n Find record with the email: {email}...")

    # create to databse and create cursor
    conn, c = connect_db_cursor()

    c.execute("""
        SELECT * from customers
        WHERE email = (?)
    """, (email,))

    # gather all information using fetch
    items = c.fetchall()

    # show results from sql command
    for item in items:
        print(item)

    # close connection
    conn.close()


