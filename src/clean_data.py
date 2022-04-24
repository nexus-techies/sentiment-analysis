import re
import string


class clean_reviews:
    def make_review_lowercase(self):
        self.reviews_data = self.df['content'].str.lower()

    def remove_urls(self):
        def cleaning_url(text):
            return re.sub('((https?://[^\s]+)|(http?://[^\s]+)|(www\.[^\s]+))','',str(text))

        self.reviews_data = self.reviews_data.apply(lambda x: cleaning_url(x))

    def remove_punctuations(self):
        include = string.punctuation
        include = include.replace(".", "")
        include = include.replace("-", "")

        def cleaning_punctuation(text):
            return text.translate(str.maketrans('','',include))

        self.reviews_data = self.reviews_data.apply(lambda x: cleaning_punctuation(x))

    def remove_emojis(self):
        def cleaning_emojis(data):
            emoj = re.compile("["
                u"\U0001F600-\U0001F64F"  # emoticons
                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                u"\U00002500-\U00002BEF"  # chinese char
                u"\U00002702-\U000027B0"
                u"\U00002702-\U000027B0"
                u"\U000024C2-\U0001F251"
                u"\U0001f926-\U0001f937"
                u"\U00010000-\U0010ffff"
                u"\u2640-\u2642"
                u"\u2600-\u2B55"
                u"\u200d"
                u"\u23cf"
                u"\u23e9"
                u"\u231a"
                u"\ufe0f"  # dingbats
                u"\u3030"
                            "]+", re.UNICODE)
            return re.sub(emoj, '', data)

        self.reviews_data = self.reviews_data.apply(lambda x: cleaning_emojis(x))

    def remove_whitespace(self):
        def cleaning_whitespace(text):
            return ' '.join(text.split())

        self.reviews_data = self.reviews_data.apply(lambda x: cleaning_whitespace(x))

    def remove_multiple_dots(self):
        def cleaning_dots(text):
            return re.sub('\.+', ' ', str(text))

        self.reviews_data = self.reviews_data.apply(lambda x: cleaning_dots(x))

    def remove_special_symbols(self):
        def cleaning_symbols(text):
            return re.sub('[^A-Za-z0-9]+', ' ', text)

        self.reviews_data = self.reviews_data.apply(lambda x: cleaning_symbols(x))
