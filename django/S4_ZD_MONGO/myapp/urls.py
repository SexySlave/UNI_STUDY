from django.contrib import admin
from django.urls import path

from django.urls import path
from .views import add_article, list_articles, index, delete_article

urlpatterns = [
    path("", index, name="index"),  # Главная страница
    path("list_articles/", list_articles, name="list_articles"),  # Список статей
    path("add_article/", add_article, name="add_article"),  # Добавление статьи
path('delete_article/<str:article_id>/', delete_article, name='delete_article'),
]