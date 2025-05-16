import unittest
from bookshop import Book, Inventory

class TestInventory(unittest.TestCase):
    def setUp(self):
        self.Inventory = Inventory()
        self.book1 = Book("1984", "George Orwell", 3, "111-222-333-444-555")
        self.Inventory.add_books(self.book1)

    def test_find_book(self):
        found = self.Inventory.find_book("111-222-333-444-555")
        self.assertEqual(found.author, "George Orwell")

    def test_get_quantity_three(self):
        self.assertEqual(self.Inventory.get_quantity("111-222-333-444-555"),3)

    def test_get_quantity_none(self):
        self.assertEqual(self.Inventory.get_quantity("111"),0)

if __name__ == "__main__":
    unittest.main()