from second_part.build_tables import build_vehicles_table
from second_part.build_tables import build_signals_table


if __name__ == "__main__":
     build_vehicles_table('../dataset/files_xlsx')
     build_signals_table('../dataset/files_csv')

