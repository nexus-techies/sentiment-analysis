from src import common_functions as common
from src import language_processing as lp

data_path = "./webscrapping/data.csv"
int_json = "./data/collected_data.json"

def main():
    product = lp.nlp()
    csvreader = common.read_csv(data_path)
    header = next(csvreader)
    common.dump_to_json(int_json, header, csvreader)
    product.get_nouns(int_json)


if __name__ == '__main__':
    main()