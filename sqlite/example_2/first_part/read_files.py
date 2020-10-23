
import pandas as pd


def read_csv_files(filename):
    # insert multi values on a table
    print("\n Reading File...")
    df = pd.read_csv(filename, sep=",")
    rows = [row for name, row in df.iterrows()]

    return rows

