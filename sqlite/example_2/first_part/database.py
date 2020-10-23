import sqlite3
import pandas as pd

# connect db and cursor
conn = sqlite3.connect("databases/ved.db")
c = conn.cursor()

# Data Type
# NULL, INTEGER, REAL, TEXT, BLOB

# create table
c.execute(""" 
        CREATE TABLE IF NOT EXISTS signals (
            signal_id       INTEGER PRIMARY KEY ASC,
            day_num         FLOAT NOT NULL,
            vehicle_id      INT NOT NULL,
            trip_id         INT NOT NULL,
            time_stamp      INT NOT NULL,
            latitude        FLOAT NOT NULL,
            longitude       FLOAT NOT NULL,
            speed           FLOAT,
            maf             FLOAT,
            rpm             FLOAT,
            abs_load        FLOAT,
            oat             FLOAT,
            fuel_rate       FLOAT,
            ac_power_kw     FLOAT,
            ac_power_w      FLOAT,
            heater_power_w  FLOAT,
            hv_bat_current  FLOAT,
            hv_bat_soc      FLOAT,
            hv_bat_volt     FLOAT,
            st_ftb_1        FLOAT,
            st_ftb_2        FLOAT,
            lt_ftb_1        FLOAT,
            lt_ftb_2        FLOAT
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
    INSERT INTO signals (
        day_num,
        vehicle_id,
        trip_id,
        time_stamp,
        latitude,
        longitude,
        speed,
        maf,
        rpm,
        abs_load,
        oat,
        fuel_rate,
        ac_power_kw,
        ac_power_w,
        heater_power_w,
        hv_bat_current,
        hv_bat_soc,
        hv_bat_volt,
        st_ftb_1,
        st_ftb_2,
        lt_ftb_1,
        lt_ftb_2
    )
    VALUES (
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
        ?, ?
    )""", rows)

conn.commit()
