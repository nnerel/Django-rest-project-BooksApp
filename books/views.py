from django.shortcuts import render, get_object_or_404
from .models import Author, Genre, Book
from .signals import custom_signal


def home(request):
    custom_signal.send(sender=Author)
    return render(request, 'books/home.html', {})


def book_all(request):
    books = Book.books.all()
    return render(request, 'books/all.html', {'books': books})


def genre_list(request, genre_slug=None):
    genre = get_object_or_404(Genre, slug=genre_slug)
    books = Book.objects.filter(genre=genre)
    return render(request, 'books/genre.html', {'genre': genre, 'books': books})


def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug, in_stock=True)
    return render(request, 'books/single.html', {'book': book})