from django.urls import path
from . import views

app_name = 'books_api'

urlpatterns = [
    path('<int:pk>/', views.BookDetail.as_view(), name='detail-create'),
    path('', views.BookList.as_view(), name='list-create'),
]
