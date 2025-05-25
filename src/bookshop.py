class Book:
    def __init__(self, title, author, stock, isbn):
        self.title = title
        self.author = author
        self.stock = stock
        self.isbn = isbn

    def __repr__(self):
        return f"Book(title={self.title}, author={self.author}, stock={self.stock}, isbn={self.isbn})"

class Inventory:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        # Don't include hyphen in isbn for consistency
        book.isbn = book.isbn.replace("-", "")
        self.books.append(book)

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def sell_book(self, isbn):
        book = self.find_book(isbn)
        if book and book.stock > 0:
            book.stock -= 1
            return True
        return False

    def get_quantity(self, isbn):
        book = self.find_book(isbn)
        return book.stock if book else 0