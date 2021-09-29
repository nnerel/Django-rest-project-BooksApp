from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_all, name='book_all'),
    path('books/<slug:genre_slug>/', views.genre_list, name='genre_list'),
    path('<slug:slug>', views.book_detail, name='book_detail'),
]