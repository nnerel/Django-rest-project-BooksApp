from rest_framework import serializers
from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'slug', 'premiere', 'genre', 'image',
            'description', 'added_by', 'in_stock')
        