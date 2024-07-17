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
    
    