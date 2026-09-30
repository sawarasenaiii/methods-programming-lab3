import tempfile
import unittest
from pathlib import Path

from main import Book, ShapeFactory, TextFile


class ObjectOrientedTests(unittest.TestCase):
    def test_book_and_static_method(self):
        self.assertEqual(str(Book("1984", "Джордж Оруэлл")), "1984 — Джордж Оруэлл")
        self.assertTrue(Book.is_valid_title("1984"))
        self.assertFalse(Book.is_valid_title("   "))

    def test_file_operations(self):
        with tempfile.TemporaryDirectory() as directory:
            file = TextFile(Path(directory) / "note.txt")
            file.write("один")
            file.append(" два")
            self.assertEqual(file.read(), "один два")

    def test_factory(self):
        self.assertEqual(ShapeFactory.create("rectangle", width=3, height=4).area(), 12)
