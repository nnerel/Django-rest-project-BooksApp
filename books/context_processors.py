from .models import Genre


def book_genre(request):
    return {
        'book_genre': Genre.objects.all()
    }