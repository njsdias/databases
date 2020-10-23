import sqlite3
import pandas as pd
import numpy as np
from tqdm import tqdm
import os


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


def create_vehicles():
    conn, c = connect_db_cursor()

    # create table
    c.execute(""" 
               CREATE TABLE IF NOT EXISTS vehicles (
                   vehicle_id      INTEGER PRIMARY KEY ASC,
                   vehicle_type    TEXT,
                   vehicle_class   TEXT,
                   engine          TEXT,
                   transmission    TEXT,
                   drive_wheels    TEXT,
                   weight          FLOAT
               )""")

    conn.commit()


def insert_into_vehicles(rows):
    conn, c = connect_db_cursor()

    c.executemany("""
        INSERT INTO vehicles(
            vehicle_id,
            vehicle_type,
            vehicle_class,
            engine,
            transmission,
            drive_wheels,
            weight
    )
        VALUES (?, ?, ?, ?, ?, ?, ?)""", rows)

    conn.commit()


def build_vehicles_table(xlsx_path):

    print('Create Table')
    create_vehicles()

    print("\n Get Files Info...")
    get_filenames = [os.path.join(xlsx_path, file) for file in tqdm(os.listdir(xlsx_path)) if file.endswith(".xlsx")]

    total_filenames = len(get_filenames)
    file_i = 0

    for filenames in get_filenames:
        file_i = file_i + 1
        # read xlsx
        print(f"\n Reading file...{file_i} / {total_filenames}")
        df_temp = pd.read_excel(filenames).replace('NO DATA', np.nan)

        # get values from each row
        print(f"\n Gather row values")
        rows = [row for name, row in df_temp.iterrows()]

        # insert each row in table
        print(f"\n Insert values into table...")
        insert_into_vehicles(rows)


if __name__ == "__main__":

    build_vehicles_table('../dataset/files_xlsx')
