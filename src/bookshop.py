class Book:
    def __init__(self, title, author, stock, isbn):
        self.title = title
        self.author = author
        self.stock = stock
        self.isbn = isbn

    def __repr__(self):
        self.books = []
    
class Inventory:
    def __init__(self):
        self.books = []
    
    def add_books(self, book):
        self.books.append(book)
    
    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def sell_book(self, isbn):
        book = self.find_book(isbn)
        if book and book.stock > 0:
            book.stock-=1
            return True
        return False

    def get_quantity(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book.stock
        return 0
