import sqlite3
import pandas as pd

# connect db and cursor
conn = sqlite3.connect("databases/ved.db")
c = conn.cursor()

# Data Type
# NULL, INTEGER, REAL, TEXT, BLOB

# create table
c.execute(""" 
        CREATE TABLE IF NOT EXISTS veds(
             DayNum real,
             VehId int64,
             Trip int64,
             Timestamp_ms real,
             Latitude_deg real,
             Longitude_deg real,
             VehicleSpeed_km_h real,
             MAF_g_sec real,
             Engine_rpm real,
             AbsoluteLoad_perc real,
             OAT_celcius real,
             FuelRate_L_h real,
             AirConditioningPower_kw real,
             AirConditioningPower_w real,
             HeaterPower_w real,
             HVBatteryCurrent_a real,
             HVBatterySOC real,
             HVBattery real,
             ShortTermFuelTrimBank1 real,
             ShortTermFuelTrimBank2 real,
             LongTermFuelTrimBank1 real,
             LongTermFuelTrimBank2 real
        )""")

conn.commit()

# insert multi values on a table
# first: read dataset
print("\n Reading File...")
df = pd.read_csv("dataset/VED_171101_week.csv", sep=",")

# second: insert information into table

rows = [row for name, row in df.iterrows()]
print("\n Inserting Values...")
c.executemany("""
    INSERT INTO veds VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", rows)
conn.commit()
