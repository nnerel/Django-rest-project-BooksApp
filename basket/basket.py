from books.models import Book 

# Initialize session for basket 
class Basket():   

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket 

# Adding and updating the basket session data
    def add(self, book):
        book_id = book.id 
        if book_id not in self.basket:
             self.basket['book_id'] = {'price': str(book.price)}

        self.session.modified = True

