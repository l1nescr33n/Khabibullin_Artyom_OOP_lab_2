BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:  # Создаём класс Book
    def __init__(self, id_, name, pages):  # Инициализируем атрибуты класса
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:  # Вызываем специальный метод __str__ для более удобного отображения информации о книгах
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:  # Вызываем специальный метод __repr__ для вызова текстового образа объекта
        return f"Book(id_={self.id_}, name='{self.name}', pages={self.pages})"


class Library:  # Создаём класс Library

    def __init__(self, books=None):  # Инициализируем атрибут со списком книг
        self.books = books

    def get_next_book_id(self):  # Объявление метода для получения следующего id книги
        if self.books is None:
            return 1  # Получение единицы, если список книг пустой
        else:
            return len(self.books) + 1  # Получение следующего номера, если список книг содержит в себе книги

    @staticmethod
    def get_index_by_book_id(books_id):  # Объявление метода, возвращающего индекс книги
        for book_id, name in enumerate(BOOKS_DATABASE):  # Получение пары индекс-значение в последовательности
            return book_id  # Возврат полученного значения
        if books_id not in BOOKS_DATABASE:  # Вызов исключения при отсутствии номера книги
            raise ValueError('"Книги с запрашиваемым id не существует"')


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
