"""
Написать логгирующий декоратор log_decorator, который будет логгировать
вызов функции. До выполнения функции необходимо вывести в консоль строку
"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}". А после вывести
строку "Выполнено {func.__name__}".

Написать логгирующий метакласс LogMeta, который ко всем методам класса добавляет
функционал декоратора log_decorator.
"""


def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f'Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}')
        print(f'Выполнено {func.__name__}')
        result = func(*args, **kwargs)
        return result
    return wrapper


class LogMeta(type):
    def __new__(mcs, name, bases, attr, **extra_kwargs):
        new_class = super().__new__(mcs, name, bases, attr, **extra_kwargs)
        functions = {k: v for k, v in new_class.__dict__.items() if callable(v)}
# Ну тут даже не понимаю, что не понимаю....