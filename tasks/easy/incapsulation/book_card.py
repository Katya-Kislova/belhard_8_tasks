"""
Создать класс BookCard, в классе должны быть:

- private атрибут author - автор (тип str)
- private атрибут title - название книги (тип str)
- private атрибут year - год издания (тип int)
- магический метод __init__, который принимает author, title, year
- магические методы сравнения для сортировки книг по году издания
- сеттеры и геттеры к атрибутам author, title, year. В сеттерах сделать проверку
  на тип данных, если тип данных не подходит, то бросить ValueError. Для года
  издания дополнительно проверить на валидность (> 0, <= текущего года).

Аксессоры реализоваться через property.
"""
from datetime import date

CURRENT_YEAR = date.today().year


class BookCard:
    _author: str
    _title: str
    _year: int

    def __init__(self, author, title, year):
        self._author = author
        self._title = title
        self._year = year

    def __eq__(self, other):
        return self._year == self._year

    def __lt__(self, other):
        return self._year < self._year

    def __repr__(self):
        return f'{self.author}, "{self.title}", {self.year}.\n'

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if not isinstance(author, str):
            raise ValueError
        else:
            self._author = author

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if not isinstance(title, str):
            raise ValueError
        else:
            self._title = title

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        if not isinstance(year, int):
            raise ValueError
        elif year < 0 or year >= 2022:
            raise ValueError
        else:
            self._year = year


if __name__ == '__main__':
    book_list = [
        BookCard('Стивен Кинг', 'Сияние', 1977),
        BookCard('Дэниел Киз', 'Цветы для Элджернона', 1959),
        BookCard('Дуглас Адамс', 'Автостопом по галактике', 1979)
    ]
    print(sorted(book_list))
# Не понимаю, почему не сортируется и почему некрасиво выводится, с запятой впереди.
