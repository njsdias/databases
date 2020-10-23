import first_part.create_tables as create_tables
import first_part.insert_into_tables as insert_into_tables
import first_part.read_files as read_files

if __name__ == "__main__":

    # create table signals
    create_tables.create_signals()

    # read csv
    rows = read_files.read_csv_files('../dataset/files_csv/VED_171101_week.csv')

    # insert values into table signals
    insert_into_tables.insert_into_signals(rows)



