import pytest

from main import BooksCollector
from data import TestConstants

@pytest.fixture(scope='function')
def collector():
    collector = BooksCollector()
    return collector
    
@pytest.fixture(scope='function')
def load_data_without_genre(collector):
    for book_name in TestConstants.BOOKS_DICTIONARY.keys():
        collector.add_new_book(book_name)
    return collector
    
pytest.fixture(scope='function')
def load_data_with_genre(collector):
    for book_name, genre in TestConstants.BOOKS_DICTIONARY.items():
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
    return collector
    
    