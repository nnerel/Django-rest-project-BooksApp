from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse

from .managers import BookQueryset, BookManager


class Author(models.Model):
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    date_of_birth = models.DateField()

    class Meta:
        verbose_name_plural = 'authors'

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Genre(models.Model):
    name = models.CharField(max_length=155, db_index=True)
    slug = models.SlugField(max_length=155, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('books:genre_list', args=[self.slug])


class Book(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    title = models.CharField(max_length=155)
    slug = models.SlugField(max_length=155)
    premiere = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/', default='default.png')
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='added_by')
    created = models.DateTimeField(auto_now_add=True)
    in_stock = models.BooleanField(default=True)

    objects = models.Manager()
    books = BookManager()

    link = 'edit'

    class Meta:
        verbose_name_plural = 'books'
        ordering = ('-premiere',)

    def get_absolute_url(self):
        return reverse('books:book_detail', args=[self.slug])

    def __str__(self):
        return self.title
