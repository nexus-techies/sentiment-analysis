from src import common_functions as common
from src import language_processing as lp

data_path = "./webscrapping/data.csv"
json_path = "./data/collected_data.json"
matrix_path = "./data/binary_matrix.csv"

def main():
    product = lp.nlp()
    csvreader = common.read_csv(data_path)
    header = next(csvreader)
    common.dump_to_json(json_path, header, csvreader)
    product.get_nouns(json_path)
    product.generate_binary_matrix()
    product.dump_binary_matrix(matrix_path)


if __name__ == '__main__':
    main()