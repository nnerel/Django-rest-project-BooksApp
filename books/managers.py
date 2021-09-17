from django.db import models

class BookQueryset(models.QuerySet):
    def is_available(self):
        return self.filter(in_stock=True)

    def is_disavailable(self):
       return self.filter(in_stock=False)


class BookManager(models.Manager):
    def get_queryset(self):
        return BookQueryset(self.model, using=self._db)

    def is_disavailable(self):
        return self.get_queryset().in_stock_true()

    def is_disavailable(self):
        return self.get_queryset().in_stock_false()
