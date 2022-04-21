from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_news', views.get_news, name='fetch_newsapi'),
]