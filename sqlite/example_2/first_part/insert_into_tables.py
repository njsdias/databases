from second_part.utils import connect_db_cursor


def insert_into_signals(rows):
    conn, c = connect_db_cursor()

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





