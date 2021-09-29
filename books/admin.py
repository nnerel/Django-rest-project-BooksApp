from django.contrib import admin
from .models import Author, Genre, Book


@admin.register(Genre)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'slug', 'genre', 'in_stock', 'link')
    list_editable = ('title',)
    list_display_links = ('link',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Author)
