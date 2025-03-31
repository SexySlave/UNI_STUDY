from django.conf import settings
from bson import ObjectId

class Article:
    collection = settings.MONGO_DB["parsed"]

    @staticmethod
    def add_article(author, date_posted, summary, content, url, title):
        article_data = {
            "Автор": author,
            "Дата размещения": date_posted,
            "Краткое описание": summary,
            "Полное содержание статьи": content,
            "Ссылка": url,
            "Наименование": title,
        }
        return Article.collection.insert_one(article_data).inserted_id

    @staticmethod
    def get_all_articles():
        return list(Article.collection.find({}, {"_id": 1, "Наименование": 1, "Автор": 1, "Дата размещения": 1, "Краткое описание": 1, "Ссылка": 1,}))

    @staticmethod
    def get_article_by_id(article_id):
        return Article.collection.find_one({"_id": ObjectId(article_id)}, {"_id": 0})

    @staticmethod
    def delete_article(id):
        Article.collection.delete_one({"_id": ObjectId(id)})
