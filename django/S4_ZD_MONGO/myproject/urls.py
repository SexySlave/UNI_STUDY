from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),  # Админка Django (по желанию)
    path("", include("myapp.urls")),  # Подключаем маршруты из "myapp"
]
