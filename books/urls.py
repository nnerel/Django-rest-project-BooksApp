from django.urls import path
from django.views.generic import TemplateView

app_name = 'books'

urlpatterns = [
    path('', TemplateView.as_view(template_name='book/index.html'))
]
