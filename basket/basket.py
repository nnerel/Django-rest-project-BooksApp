from books.models import Book 


# Initialize session for basket 
class Basket():   

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {'test': 11212}
        self.basket = basket 