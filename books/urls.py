from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.home, name='home'),
    path('expected/', views.expected, name='expected'),
    path('all/', views.book_all, name='book_all'),
    path('<slug:genre_slug>/', views.genre_list, name='genre_list'),
    path('<slug:slug>', views.book_detail, name='book_detail'),
]
