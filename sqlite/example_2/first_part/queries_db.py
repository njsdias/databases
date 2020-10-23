import sqlite3
import pandas as pd
import os


def connect_db_cursor():
    """
    Connect to Database and Create a Cursor
    :return:
        conn: connection
        c: cursor
    """
    # connect to database
    conn = sqlite3.connect('databases/ved.db')

    # create a cursor
    c = conn.cursor()

    return conn, c


def show_all():
    """
    Query the DB and Return all record
    """
    os.system('clear')

    print("\n Show all results...")

    # create to databse and create cursor
    conn, c = connect_db_cursor()

    # Query the database
    c.execute("SELECT VehId, COUNT(VehId) AS vehid FROM veds GROUP BY Vehid LIMIT 10")

    # gather all information using fetch
    items = c.fetchall()

    # show results from sql command
    for item in items:
        print(item)

    # close connection
    conn.close()


def show_df():
    os.system('clear')
    conn, c = connect_db_cursor()
    # df = pd.read_sql("SELECT * FROM veds LIMIT 5", conn)
    # df = pd.read_sql("SELECT VehId, COUNT(VehId) AS total FROM veds GROUP BY VehId LIMIT 10", conn)

    c.execute("DROP TABLE signals")
    conn.commit()

    #df = pd.read_sql("SELECT * FROM signals", conn)
    #print(df)


# show all results
show_df()
