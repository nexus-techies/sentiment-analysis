import csv
import json


def read_csv(path):
    file = open(path, encoding='utf8')
    return csv.reader(file)


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
