import json
from nltk import word_tokenize, pos_tag
import numpy as np
import pandas as pd

class nlp:

    def __init__(self) -> None:
        import nltk
        nltk.download('punkt')
        nltk.download('averaged_perceptron_tagger')


    def get_nouns(self, json_file_path):
        with open(json_file_path) as file:
            self.data = json.load(file)
            for record in self.data:
                nouns = [token for token,
                pos in pos_tag(word_tokenize(record['content'])) if pos.startswith('N')]
                # print(nouns)
                record['nouns'] = nouns

        with open(json_file_path, "w") as f:
            json.dump(self.data, f)


    def dump_binary_matrix(self, matrix_path):
        df = pd.DataFrame(
            self.binary_matrix, index=range(self.reviews_count), columns=self.net_nouns)
        df.to_csv(matrix_path, index=True, header=True)


    def generate_binary_matrix(self):
        self.reviews_count = len(self.data)
        self.net_nouns = []
        for review in self.data:
            for noun in review['nouns']:
                if noun not in self.net_nouns:
                    self.net_nouns.append(noun)

        self.shape = (self.reviews_count, len(self.net_nouns))
        self.binary_matrix = np.zeros(self.shape)
        self.binary_matrix = self.binary_matrix.astype(int)

        for review in self.data:
            for noun in review['nouns']:
                self.binary_matrix[review['review_id']][self.net_nouns.index(noun)] = 1
