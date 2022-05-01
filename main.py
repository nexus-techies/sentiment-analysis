import string
from src import common_functions as common
from src import language_processing as lp
from src import clean_data as clean

data_path = "./webscrapping/data.csv"
csv_path = "./data/cleaned_data.csv"
json_path = "./data/collected_data.json"
matrix_path = "./data/binary_matrix.csv"
freq_items_path = "./data/association_mapping.csv"

def clean_data(product):
    clean.clean_reviews.make_review_lowercase(product)
    clean.clean_reviews.remove_urls(product)
    clean.clean_reviews.remove_punctuations(product)
    clean.clean_reviews.remove_emojis(product)
    clean.clean_reviews.remove_multiple_dots(product)
    clean.clean_reviews.remove_special_symbols(product)
    clean.clean_reviews.remove_whitespace(product)
   
    product.df['review'] = product.reviews_data
    product.df['review_id'] = product.reviews_data.index
    product.reviews_data.index = product.reviews_data.index.map(str)
    product.df['Uid'] = f"AMAZON_" + product.reviews_data.index

    common.df_to_csv(product.df, csv_path)


def sentiment_analysis(product):
    product.get_nouns()
    product.generate_binary_matrix()
    product.dump_binary_matrix(matrix_path)
    product.get_frequenct_items(freq_items_path)


def main():
    product = lp.nlp()
    product.df = common.create_df_from_csv(data_path)
    clean_data(product)
    sentiment_analysis(product)


if __name__ == '__main__':
    main()