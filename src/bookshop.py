class Book:
    def __init__(self, title, author, stock):
        self.title = title
        self.author = author
        self.stock = stock

    def __repr__(self):
        self.books = []
    
class Inventory:
    def __init__(self):
        self.books = []
    
    def add_books(self, book):
        self.books.append(book)
    
    def find_book(self, title):
        for book in self.books:
            print(title, self)
            if book.title == title:
                return book
        return None

    def sell_book(self, title):
        book = self.find_book(title)
        if book and book.stock > 0:
            book.stock-=1
            return True
        return False
