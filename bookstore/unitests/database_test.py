from database import UserCredentials, Book
import pytest

def test_user_creation():
    user = UserCredentials(id=1, email="testuser@example.com", password="password123")
    assert user.id == 1
    assert user.email == "testuser@example.com"
    assert user.password == "password123"

def test_book():
    book = Book()
    book.id = 1
    book.name = "testbook"
    book.author = "testauthor"
    book.published_year = 2010
    book.book_summary = "testing book"
    assert book.id == 1
    assert book.name == "testbook"
    assert book.author ==  "testauthor"
    assert book.published_year ==  2010
    assert book.book_summary == "testing book"