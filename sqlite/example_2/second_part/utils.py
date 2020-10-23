import sqlite3


def connect_db_cursor():
    """
    Connect to Database and Create a Cursor
    :return:
        conn: connection
        c: cursor
    """
    # create and connect to database
    conn = sqlite3.connect('../databases/ved.db')

    # create a cursor
    c = conn.cursor()

    return conn, c


def drop_table():

    # create to databse and create cursor
    conn, c = connect_db_cursor()

    # Drop Table
    c.execute("DROP TABLE signals")

    # commit our command
    conn.commit()


if __name__ == "__main__":
    drop_table()

