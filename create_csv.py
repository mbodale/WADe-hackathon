import pandas as pd
import os


def create_csv(sheet_name, file_name):
    read_file = pd.read_excel(r'invatamant-superior-2020.xlsx', sheet_name=sheet_name)
    read_file.to_csv('raw_' + file_name, index=None, header=True)
    with open('raw_' + file_name, 'r', encoding="utf8") as f:
        with open(file_name, 'w', encoding="utf8") as f1:
            next(f)  # skip 2 lines
            next(f)
            for line in f:
                f1.write(line)

    os.remove('raw_' + file_name)
