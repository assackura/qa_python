from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_nine_books(self, load_data_without_genre):
        # создаем экземпляр (объект) класса BooksCollector

        # добавляем две книги
        #collector.add_new_book('Гордость и предубеждение и зомби')
        #collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(load_data_without_genre.get_books_genre()) == 9

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.mark.parametrize('book_name', ['', 'testtestetstestesttesttestetstestesttesttestetstestesttesttestetstestesttesttestetstestest', 'testtestetstestesttesttestetstestesttesttestetstestesttesttestetstestesttesttestetstestesttesttestetstestesttesttestetstestesttesttestetstestesttesttestetstestesttesttestetstestest'])
    def test_add_new_book_not_add_not_correct_name_books(self, book_name, collector):
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 0
        
    def test_add_new_book_not_add_two_identical_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1
        
    def test_add_new_book_not_add_genre(self, collector):
        book_name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(book_name)
        assert collector.get_books_genre()[book_name] == ''
        
        
    @pytest.mark.parametrize('list_genres', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_genre_checking_list_for_genres(self, list_genres, collector):
        assert list_genres in collector.genre
        
    def test_set_book_genre_set_genre(self, collector):
        book_name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Ужасы')
        assert collector.get_books_genre()[book_name] == 'Ужасы'
        
    def test_get_books_with_specific_genre_various_genres_books_specified_genre(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.add_new_book('Незнайка на луне')
        collector.set_book_genre('Незнайка на луне', 'Мультфильмы')
        collector.add_new_book('Золотой ключик')
        collector.set_book_genre('Золотой ключик', 'Мультфильмы')
        collector.add_new_book('12 стульев')
        collector.set_book_genre('12 стульев', 'Комедии')
        collector.add_new_book('Бедная лиза')
        collector.set_book_genre('Бедная лиза', 'Детективы')
        collector.add_new_book('Странные игры')
        collector.set_book_genre('Странные игры', 'Детективы')
        assert collector.get_books_with_specific_genre('Детективы') == ['Бедная лиза', 'Странные игры']
        
    def test_get_books_with_specific_genre_not_list_genre_0(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_books_with_specific_genre('Сказки') == []
        
    def test_get_books_for_children_get_not_age_rating_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.add_new_book('Незнайка на луне')
        collector.set_book_genre('Незнайка на луне', 'Мультфильмы')
        collector.add_new_book('Золотой ключик')
        collector.set_book_genre('Золотой ключик', 'Мультфильмы')
        collector.add_new_book('12 стульев')
        collector.set_book_genre('12 стульев', 'Комедии')
        collector.add_new_book('Бедная лиза')
        collector.set_book_genre('Бедная лиза', 'Детективы')
        collector.add_new_book('Странные игры')
        collector.set_book_genre('Странные игры', 'Детективы')
        result = list(set(['Гордость и предубеждение и зомби', 'Бедная лиза', 'Странные игры']) & set(collector.get_books_for_children()))
        assert len(result) == 0
        
    def test_add_book_in_favorites_books_list_favorite_list(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Незнайка на луне')
        collector.add_new_book('Золотой ключик')
        collector.add_new_book('12 стульев')
        collector.add_new_book('Бедная лиза')
        collector.add_new_book('Странные игры')
        collector.add_book_in_favorites('Незнайка на луне')
        collector.add_book_in_favorites('Золотой ключик')
        assert collector.get_list_of_favorites_books() == ['Незнайка на луне', 'Золотой ключик']
        
    @pytest.mark.parametrize('name_book', ['', 'sdhfbsdjfbjh', 'Незнайка на луне'])
    def test_add_book_in_favorites_not_add_favorite_list(self, name_book, collector):
        collector.add_new_book('Незнайка на луне')
        collector.add_book_in_favorites('Незнайка на луне')
        collector.add_book_in_favorites(name_book)
        assert len(collector.get_list_of_favorites_books()) == 1
        
    def test_delete_book_in_favorites_books_list_favorite_list(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.add_new_book('Незнайка на луне')
        collector.set_book_genre('Незнайка на луне', 'Мультфильмы')
        collector.add_new_book('Золотой ключик')
        collector.set_book_genre('Золотой ключик', 'Мультфильмы')
        collector.add_new_book('12 стульев')
        collector.set_book_genre('12 стульев', 'Комедии')
        collector.add_new_book('Бедная лиза')
        collector.set_book_genre('Бедная лиза', 'Детективы')
        collector.add_new_book('Странные игры')
        collector.set_book_genre('Странные игры', 'Детективы')
        collector.add_book_in_favorites('Незнайка на луне')
        collector.add_book_in_favorites('Золотой ключик')
        collector.delete_book_from_favorites('Золотой ключик')
        assert collector.get_list_of_favorites_books() == ['Незнайка на луне']  
        
        
        
        