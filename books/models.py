from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from .managers import BookQueryset, BookManager

class Author(models.Model):
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    date_of_birth = models.DateField()

    class Meta:
        verbose_name_plural = 'authors'

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Book(models.Model):

    GENRE = (
    ('thriller', 'thriller'),
    ('fantasy', 'fantasy'),
    ('scifi', 'sci-fi'),
    ('horror', 'horror'),
    )

    title = models.CharField(max_length=155)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    premiere = models.DateField()
    genre = models.CharField(max_length=20, choices=GENRE)
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

    def __str__(self):
        return self.title
