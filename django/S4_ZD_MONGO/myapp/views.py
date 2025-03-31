from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Article
import json
from django.shortcuts import render
from pymongo import MongoClient

MONGO_URI = "mongodb://remote_user:qwerty123@192.168.0.112:27017/admin"
client = MongoClient(MONGO_URI)
db = client["your_database"]
collection = db["parsed"]


def index(request):
    """Главная страница с поиском"""
    query = request.GET.get("q", "").strip()  # Получаем параметр ?q= в URL
    if query:
        return redirect(f"/list_articles/?q={query}")  # Перенаправляем на страницу поиска

    return render(request, "myapp/index.html")


def list_articles(request):
    articles = list(collection.find({}))  # <-- Добавляем list(), чтобы данные читались
    # print(articles)
    formatted_articles = [
        {
            "id": str(article["_id"]),
            "author": article.get("Автор", "Неизвестный автор"),
            "date": article.get("Дата размещения", "Неизвестная дата"),
            "title": article.get("Наименование", "Без названия"),
            "description": article.get("Краткое описание", "Нет описания"),
            "url": article.get("Полная ссылка на статью", "Нет ссылки")
        }
        for article in articles
    ]
    # print(formatted_articles)
    return render(request, "myapp/articles.html", {"articles": formatted_articles})
def add_article(request):
    if request.method == "POST":
        data = request.POST
        Article.add_article(
            author=data["author"],
            date_posted=data["date_posted"],
            summary=data["summary"],
            content=data["content"],
            url=data["url"],
            title=data["title"],
        )
        return redirect("list_articles")
    return render(request, "myapp/index.html", {"message": "Ошибка ввода"})


def delete_article(request, article_id):

    result = Article.delete_article(article_id)
    return redirect('list_articles')