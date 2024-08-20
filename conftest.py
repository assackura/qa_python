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
    
@pytest.fixture(scope='function')
def load_data_with_genre(collector):
    for book_name, genre in TestConstants.BOOKS_DICTIONARY.items():
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
    return collector
    
@pytest.fixture(scope='function')
def get_list_age_rating(collector):
    result = []
    for book_name, genre in TestConstants.BOOKS_DICTIONARY.items():
        if genre in collector.genre_age_rating:
            result.append(book_name)
    return result
    
@pytest.fixture(scope='function')
def load_data_in_favorite(load_data_with_genre):
    for book_name in TestConstants.FAVORITES_BOOK:
        load_data_with_genre.add_book_in_favorites(book_name)
    return load_data_with_genre
    