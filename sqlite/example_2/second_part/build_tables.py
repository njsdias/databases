from second_part.create_tables import create_vehicles
from second_part.create_tables import create_signals

from second_part.insert_into_tables import insert_into_vehicles
from second_part.insert_into_tables import insert_into_signals

import numpy as np
import pandas as pd
from tqdm import tqdm
import os


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


def build_signals_table(csv_path):
    print('Create Table')
    create_signals()

    print("\n Get Files Info...")
    get_filenames = [os.path.join(csv_path, file) for file in tqdm(os.listdir(csv_path)) if file.endswith(".csv")]

    total_filenames = len(get_filenames)
    file_i = 0

    for filenames in get_filenames:
        # read csv
        file_i = file_i + 1
        print(f"\n Reading file...{file_i} / {total_filenames}")
        df_temp = pd.read_csv(filenames)

        # get values from each row
        print(f"\n Gather row values")
        rows = [row for name, row in df_temp.iterrows()]

        # insert each row in table
        print(f"\n Insert values into table...")
        insert_into_signals(rows)
