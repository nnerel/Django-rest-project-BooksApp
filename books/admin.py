from django.contrib import admin
from .models import Book, Author

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'in_stock', 'link')
    list_editable = ('title',)
    list_display_links = ('link',)



admin.site.register(Author)
