from django.db.models.signals import post_save
from django.dispatch import receiver, Signal
from django.core.signals import request_finished
import logging

from .models import Author, Genre, Book


custom_signal = Signal()


# logs for author object model
author_log = logging.getLogger('author_log')
author_log.setLevel(logging.DEBUG)
author_log_handler = logging.FileHandler('logs/author.log')
author_log_handler.setLevel(logging.DEBUG)
author_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
author_log_handler.setFormatter(author_formatter)
author_log.addHandler(author_log_handler)

# logs for genre object model 
genre_log = logging.getLogger('genre_log')
genre_log.setLevel(logging.DEBUG)
genre_log_handler = logging.FileHandler('logs/genre.log')
genre_log_handler.setLevel(logging.DEBUG)
genre_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
genre_log_handler.setFormatter(genre_formatter)
genre_log.addHandler(genre_log_handler)

# logs for book objects model 
book_log = logging.getLogger('book_log')
book_log.setLevel(logging.DEBUG)
book_log_handler = logging.FileHandler('logs/book.log')
book_log_handler.setLevel(logging.DEBUG)
book_formatter = logging.Formatter('%(ascitime)r - %(name)s - %(levelname)s - %(message)s')
genre_log_handler.setFormatter(book_formatter)
book_log.addHandler(book_log_handler)


@receiver(post_save, sender=Author)
def author_after_save(sender, instance, **kwargs):
    full_name = instance.first_name + ' ' + instance.last_name
    print(f"{full_name!r} created")
    author_log.info(f"Author created: {instance.first_name} {instance.last_name}")


@receiver(post_save, sender=Genre)
def genre_after_save(sender, instance, **kwargs):
    print(f"{instance.name} created")
    genre_log.info(f"Genre created: {instance.name}")


@receiver(post_save, sender=Book)
def book_after_save(sender, instance, **kwargs):
    print(f"{instance.title} created")
    book_log.info(f"Book created: {instance.title}")


@receiver(request_finished)
def page_loaded(sender, **kwargs):
    print("Page loaded")


@receiver(custom_signal)
def func_name(sender, **kwargs):
    print("Given name")