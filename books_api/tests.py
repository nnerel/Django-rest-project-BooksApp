from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from books.models import Author, Book


class BookTests(APITestCase):

    def test_view_ports(self):
        url = reverse('books_api:list-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
