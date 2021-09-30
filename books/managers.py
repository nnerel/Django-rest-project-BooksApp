from django.db import models


class BookManager(models.Manager):
    def get_queryset(self):
        return super(BookManager, self).get_queryset().filter(in_stock=True)

    def in_stock_qty(self):
        return super(BookManager, self).get_queryset().filter(in_stock=True).count()

    def not_in_stock(self):
        return super(BookManager, self).get_queryset().filter(in_stock=False)

    def not_in_stock_qty(self):
        return super(BookManager, self).get_queryset().filter(in_stock=False).count()

  