class Book:
    def __init__(self, title, author, stock, isbn):
        # Initialize a Book object with title, author, stock quantity, and ISBN
        self.title = title
        self.author = author
        self.stock = stock
        self.isbn = isbn

    def __repr__(self):
        # Return a string representation of the Book object for easy debugging
        return f"Book(title={self.title}, author={self.author}, stock={self.stock}, isbn={self.isbn})"

class Inventory:
    def __init__(self):
        # Initialize an empty list to store books in the inventory
        self.books = []

    def add_book(self, book):
        # Add a book to the inventory list
        self.books.append(book)

    def find_book(self, isbn):
        # Search for a book in the inventory by its ISBN
        for book in self.books:
            if book.isbn == isbn:
                # Return the book if found
                return book
        # Return None if the book is not found
        return None

    def sell_book(self, isbn):
        # Find the book in the inventory by its ISBN
        book = self.find_book(isbn)
        # If the book is found and stock is available, reduce stock by 1
        if book and book.stock > 0:
            book.stock -= 1
            return True
        # Return False if the book is not found or out of stock
        return False

    def get_quantity(self, isbn):
        # Find the book in the inventory by its ISBN
        book = self.find_book(isbn)
        # Return the stock quantity if the book is found, otherwise return 0
        return book.stock if book else 0
