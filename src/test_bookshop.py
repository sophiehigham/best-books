import unittest
from bookshop import Book, Inventory

class TestInventory(unittest.TestCase):
    def setUp(self):
        self.Inventory = Inventory()
        self.book1 = Book("1984", "George Orwell", 3)
        self.Inventory.add_books(self.book1)

    def test_find_book(self):
        found = self.Inventory.find_book("1984")
        self.assertEqual(found.author, "George Orwell")

if __name__ == "__main__":
    unittest.main()