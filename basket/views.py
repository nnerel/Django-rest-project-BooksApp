from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from books.models import Book
from .basket import Basket

def basket(request):
    return render(request, 'basket/basket.html', {})

def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        book_id = int(request.POST.get('bookid'))
        book = get_object_or_404(Book, id=book_id)
        basket.add(book=book)
        response = JsonResponse({'test': 'data'})
        return response 
