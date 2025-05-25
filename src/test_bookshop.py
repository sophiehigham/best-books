import unittest
from bookshop import Book, Inventory

class TestInventory(unittest.TestCase):
    def setUp(self):
        # Set up the test environment by creating an Inventory instance
        self.inventory = Inventory()
        # Create two Book instances with title, author, stock, and ISBN
        self.book_1984 = Book("1984", "George Orwell", 3, "111-222-333-444-555")
        self.book_brave_new_world = Book("Brave New World", "Aldous Huxley", 5, "222-333-444-555-666")
        # Add the books to the inventory
        self.inventory.add_book(self.book_1984)
        self.inventory.add_book(self.book_brave_new_world)

    def test_find_book_by_isbn(self):
        # Test finding a book by its ISBN
        found_book = self.inventory.find_book("111-222-333-444-555")
        # Assert that the found book's author is "George Orwell"
        self.assertEqual(found_book.author, "George Orwell")

    def test_get_quantity_of_existing_book(self):
        # Test getting the quantity of an existing book by its ISBN
        self.assertEqual(self.inventory.get_quantity("111-222-333-444-555"), 3)

    def test_get_quantity_of_nonexistent_book(self):
        # Test getting the quantity of a non-existent book by its ISBN
        self.assertEqual(self.inventory.get_quantity("111"), 0)

    def test_add_books_to_inventory(self):
        # Test that books are correctly added to the inventory
        self.assertEqual(len(self.inventory.books), 2)
        # Assert that the second book's title is "Brave New World"
        self.assertEqual(self.inventory.books[1].title, "Brave New World")

    def test_successful_book_sale(self):
        # Test selling a book successfully
        result = self.inventory.sell_book("111-222-333-444-555")
        # Assert that the sale was successful
        self.assertTrue(result)
        # Assert that the stock quantity is reduced by 1
        self.assertEqual(self.inventory.get_quantity("111-222-333-444-555"), 2)

    def test_unsuccessful_book_sale_due_to_stock(self):
        # Test selling a book until stock is depleted
        self.inventory.sell_book("111-222-333-444-555")
        self.inventory.sell_book("111-222-333-444-555")
        self.inventory.sell_book("111-222-333-444-555")
        # Attempt to sell the book again when out of stock
        result = self.inventory.sell_book("111-222-333-444-555")
        # Assert that the sale was unsuccessful
        self.assertFalse(result)
        # Assert that the stock quantity is 0
        self.assertEqual(self.inventory.get_quantity("111-222-333-444-555"), 0)

    def test_unsuccessful_book_sale_due_to_nonexistence(self):
        # Test selling a book that does not exist in the inventory
        result = self.inventory.sell_book("999-999-999-999-999")
        # Assert that the sale was unsuccessful
        self.assertFalse(result)

if __name__ == "__main__":
    # Run the unit tests
    unittest.main()
