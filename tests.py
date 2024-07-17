from main import BooksCollector
from data import TestConstants

import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_nine_books(self, load_data_without_genre):
        assert len(load_data_without_genre.get_books_genre()) == 9

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.mark.parametrize('book_name', ['', 'testtestetstestesttesttestetstestesttesttestetstestesttesttestetstestesttesttestetstestest', 'testtestetstestesttesttestetstestesttesttestetstestesttesttestetstestesttesttestetstestesttesttestetstestesttesttestetstestesttesttestetstestesttesttestetstestesttesttestetstestest'])
    def test_add_new_book_not_add_not_correct_name_books(self, book_name, collector):
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 0
        
    def test_add_new_book_not_add_genre(self, load_data_without_genre):
        assert load_data_without_genre.get_books_genre()[TestConstants.BOOK] == ''
        
    @pytest.mark.parametrize('list_genres', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_genre_checking_list_for_genres(self, list_genres, collector):
        assert list_genres in collector.genre
        
    @pytest.mark.parametrize('list_age_rating', ['Ужасы', 'Детективы'])
    def test_genre_checking_list_for_genre_age_rating(self, list_age_rating, collector):
        assert list_age_rating in collector.genre_age_rating 
        
    def test_set_book_genre_set_genre(self, load_data_with_genre):
        assert load_data_with_genre.get_books_genre()[TestConstants.BOOK] == 'Ужасы'
        
    def test_get_books_with_specific_genre_various_genres_books_specified_genre(self, load_data_with_genre):
        assert load_data_with_genre.get_books_with_specific_genre('Детективы') == ['Бедная лиза', 'Странные игры']
        
    def test_get_books_with_specific_genre_not_list_genre_0(self, load_data_with_genre):
        assert load_data_with_genre.get_books_with_specific_genre('Сказки') == []
        
    def test_get_books_for_children_get_not_age_rating_books(self, load_data_with_genre, get_list_age_rating):
        result = list(set(get_list_age_rating) & set(load_data_with_genre.get_books_for_children()))
        assert len(result) == 0
        
    def test_add_book_in_favorites_books_list_favorite_list(self, load_data_in_favorite):
        assert load_data_in_favorite.get_list_of_favorites_books() == TestConstants.FAVORITES_BOOK
        
    @pytest.mark.parametrize('name_book', ['', 'sdhfbsdjfbjh', 'Незнайка на луне'])
    def test_add_book_in_favorites_not_add_favorite_list(self, name_book, load_data_in_favorite):
        load_data_in_favorite.add_book_in_favorites(TestConstants.BOOK)
        assert len(load_data_in_favorite.get_list_of_favorites_books()) == 2
        
    def test_delete_book_in_favorites_books_list_favorite_list(self, load_data_in_favorite):
        load_data_in_favorite.delete_book_from_favorites(TestConstants.BOOK)
        assert len(load_data_in_favorite.get_list_of_favorites_books()) == 1
        
        
        
        