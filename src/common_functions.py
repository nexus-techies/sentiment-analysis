import csv
import json
import pandas as pd


def create_df_from_csv(csv_path):
    data = pd.read_csv(csv_path, skip_blank_lines=True)
    data = data.dropna(how="all").reset_index(drop=True)
    return data


def read_csv(path):
    file = open(path, encoding='utf8')
    return csv.reader(file)


def df_to_json(df, json_path):
    df.to_json(json_path, orient='records', lines=True)


def df_to_csv(df, csv_path):
    df.to_csv(csv_path)


def dump_to_json(json_path, keys, data):
    row_number = 0
    data_dump = []
    with open(json_path, "w") as json_file:
        for row in data:
            if any(row):
                temp = dict(zip(keys, row))
                temp["review_id"] = row_number
                row_number+=1
                data_dump.append(temp)

        json.dump(data_dump, json_file, indent=4, sort_keys=True)
