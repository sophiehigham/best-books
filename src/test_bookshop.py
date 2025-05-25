import unittest
from bookshop import Book, Inventory

class TestInventory(unittest.TestCase):
    def setUp(self):
        self.inventory = Inventory()
        self.book_1984 = Book("1984", "George Orwell", 3, "111-222-333-444-555")
        self.book_brave_new_world = Book("Brave New World", "Aldous Huxley", 5, "222-333-444-555-666")
        self.inventory.add_book(self.book_1984)
        self.inventory.add_book(self.book_brave_new_world)

    def test_find_book_by_isbn(self):
        found_book = self.inventory.find_book("111-222-333-444-555")
        self.assertEqual(found_book.author, "George Orwell")

    def test_get_quantity_of_existing_book(self):
        self.assertEqual(self.inventory.get_quantity("111-222-333-444-555"), 3)

    def test_get_quantity_of_nonexistent_book(self):
        self.assertEqual(self.inventory.get_quantity("111"), 0)

    def test_add_books_to_inventory(self):
        self.assertEqual(len(self.inventory.books), 2)
        self.assertEqual(self.inventory.books[1].title, "Brave New World")

    def test_successful_book_sale(self):
        result = self.inventory.sell_book("111-222-333-444-555")
        self.assertTrue(result)
        self.assertEqual(self.inventory.get_quantity("111-222-333-444-555"), 2)

    def test_unsuccessful_book_sale_due_to_stock(self):
        self.inventory.sell_book("111-222-333-444-555")
        self.inventory.sell_book("111-222-333-444-555")
        self.inventory.sell_book("111-222-333-444-555")
        result = self.inventory.sell_book("111-222-333-444-555")
        self.assertFalse(result)
        self.assertEqual(self.inventory.get_quantity("111-222-333-444-555"), 0)

    def test_unsuccessful_book_sale_due_to_nonexistence(self):
        result = self.inventory.sell_book("999-999-999-999-999")
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
