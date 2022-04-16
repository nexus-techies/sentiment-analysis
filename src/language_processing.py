import json
from nltk import word_tokenize, pos_tag

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