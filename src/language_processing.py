import json
from nltk import word_tokenize, pos_tag
import numpy as np
import pandas as pd

from mlxtend.frequent_patterns import apriori

class nlp:

    def __init__(self) -> None:
        import nltk
        nltk.download('punkt')
        nltk.download('averaged_perceptron_tagger')


    def get_nouns(self):
        def apply_tokenization(review):
            return [token for token,
         pos in pos_tag(word_tokenize(review)) if pos.startswith('N')]

        def remove_smaller_nouns(nouns):
            return [noun for noun in nouns if len(noun) >= 3]

        self.df['nouns'] = self.df['review'].apply(lambda x: apply_tokenization(x))
        self.df['nouns'] = self.df['nouns'].apply(lambda x: remove_smaller_nouns(x))


    def dump_binary_matrix(self, matrix_path):
        df = pd.DataFrame(
            self.binary_matrix, index=range(self.reviews_count), columns=self.net_nouns)
        df.to_csv(matrix_path, index=True, header=True)


    def generate_binary_matrix(self):
        self.reviews_count = self.df.shape[0]
        self.net_nouns = self.df['nouns'].apply(tuple).explode().unique()
       
        self.shape = (self.reviews_count, len(self.net_nouns))
        self.binary_matrix = np.zeros(self.shape)
        self.binary_matrix = self.binary_matrix.astype(int)

        for review in self.df.iterrows():
            for noun in review[1]['nouns']:
                self.binary_matrix[review[1]['review_id']][int(np.where(self.net_nouns == noun)[0])] = 1
        
        # self.df.to_csv("./data/with_nouns.csv")


    def get_frequenct_items(self, freq_items_path):
        self.binary_matrix_df = pd.DataFrame(data=self.binary_matrix[1:,1:], index=self.binary_matrix[1:,0], 
        columns=self.binary_matrix[0,1:])  
        self.frq_items = apriori(self.binary_matrix_df.iloc[:, 1:], min_support = 0.1, use_colnames = True)

        self.frq_items.to_csv(freq_items_path)
