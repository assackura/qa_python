# qa_python
1) **test_add_new_book_not_add_not_correct_name_books**
	* Тест проверяет метод добавления книг в словарь books_genre *
	
2) **test_add_new_book_not_add_not_correct_name_books**
	* Тест проверяет, что в словарь не будут записываться книги, имя которых не соответствует условиям *
			* Тестом выялено, что метод не переваривает данные типа int, float, bool *
			
3)	**test_default_books_genre**
	 * Тест проверяет значение по умолчанию в словаре books_genre *
	 
4)	**test_default_favorites**
	 * Тест проверяет значение по умолчанию в списке favorites *
	 
5)	**test_add_new_book_not_add_genre**
	 * Тест проверяет, что у вновь добавленной книги отсутствует жанр *
	 
6)	**test_genre_checking_list_for_genres**
	 * Тест проверяет значение по умолчанию в списке genre *
	 
7)	**test_genre_checking_list_for_genre_age_rating**
	 * Тест проверяет значение по умолчанию в списке genre_age_rating *
	 
8)	**test_set_book_genre_set_genre**
	 * Тест проверяет метод, который устанавливает доступный жанр из списка genre *
	 
9)	**test_get_books_with_specific_genre_various_genres_books_specified_genre**
	 * Тест проверяет метод поиска наименований книг по их жанру *
	 
10)	**test_get_books_with_specific_genre_not_list_genre_0**
	 * Тест проверяет, как метод __get_books_with_specific_genre__ реагирует на различные наборы данных, не подходящих для его работы *
	 
11)	**test_get_books_for_children_get_not_age_rating_books**
	 * Тест проверяет, что метод __get_books_for_children__ не возвращает книги, жанр которых имеет возрастное ограничение *
	 
12)	**test_add_book_in_favorites_books_list_favorite_list**
	 * Тест проверяет метода, который добавляет книги в избранное *
	 
13) **test_add_book_in_favorites_not_add_favorite_list**
	 * Тест проверяет, как метод __add_book_in_favorites__ реагирует на различные наборы данных, не подходящих для его работы *
	 
14) **test_delete_book_in_favorites_books_list_favorite_list**
	 * Тест проверяет метод удаления из избранного одной из книг *
	 
15) **test_delete_book_in_favorites_books_not_data_in_favorite**
	 * Тест проверяет, как метод __delete_book_in_favorites_books__ реагирует на различные наборы данных, не подходящих для его работы *
	 
**Константы для тестирования вынесены в data.py**

**В файле conftest.py описаны фикстуры необходимые для тестирования**