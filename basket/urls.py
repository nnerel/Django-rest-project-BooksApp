from django.urls import path 
from . import views

app_name = 'basket'

urlpatterns = [
    path('b/', views.basket, name='basket'),
    path('add/', views.basket_add, name='basket_add'),
]