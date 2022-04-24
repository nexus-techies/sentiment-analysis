
class db_ops:
    def get_reviews_schema(self):
        return {
            "review_id": 0,
            "title": "",
            "review": "",
            "date": "",
            "variant": "",
            "images": "",
            "author": "",
            "rating": "",
            "product": "",
            "url": "",
            "source": "",
            "clean_review": "",
            "nouns": []
        }

    def get_product_schema(self):
        return {
            "product": "",
            "variant": "",
            "all_nouns": [],
            "   ": [],
            "association_mapping" : []
        }

        