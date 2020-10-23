from first_part.utils import connect_db_cursor


def create_signals():
    conn, c = connect_db_cursor()

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


def create_vehicles():
    conn, c = connect_db_cursor()

    c.execute = ("""
        CREATE TABLE vehicles(
            vehicle_id INTEGER PRIMARY KEY ASC,
            vehicle_type TEXT,
            vehicle_class TEXT,
            engine TEXT,
            transmission TEXT,
            drive_wheels TEXT,
            weight FLOAT
        )""")

    conn.commit()






