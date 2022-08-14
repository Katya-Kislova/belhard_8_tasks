"""
Напишите класс GameObject, в котором будут храниться координаты объекта.

- private атрибут x (тип int)
- private атрибут y (тип int)
- магический метод __init__, который принимает начальные x и y

Координаты должны быть доступны для чтения (сделать property), а их изменение
должно происходить в методе move(delta_x, delta_y). (изменение - это +=)
"""


class GameObject:

    _x: int
    _y: int

    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def move(self, delta_x, delta_y):
        self._x += delta_x
        self._y += delta_y


if __name__ == '__main__':
    a = GameObject(10, 12)
    print(a.move(2, 4))
# Почему none при выводе? Где-то не так написала что-то?