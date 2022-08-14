"""
Написать декоратор класса class_benchmark, который будет проводить
бенчмарк (замер времени выполнения) всех публичных методов класса
(те, которые не начинаются с _).

Чтобы у методов класса изменить поведение - дополнительно написать
декоратор функции def_benchmark.

До выполнения метода должен быть вывод в консоль:
Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}
Время начала: {start_time}

После выполнения метода должен быть вывод в консоль:
Выполнено {func.__name__}
Время окончания: {end_time}
Всего затрачено времени на выполнение: {end_time - start_time}
"""
import time

# start_time = time.time()
# end_time = time.time()
# difference = e - s


def def_benchmark(func):
    def wrapper(*args, **kwargs):
        print(f'Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}')
        start_time = time.time()
        print(f'Время начала: {start_time}')
        result = func(*args, **kwargs)
        print(f'Выполнено {func.__name__}')
        end_time = time.time()
        print(f'Время окончания: {end_time}')
        print(f'Всего затрачено времени на выполнение: {end_time - start_time}')
        return result
    return wrapper


def class_benchmark(cls):
    attr_dict = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for k, v in attr_dict.items():
        if not k.startswith('__'):
            wrapped_v = def_benchmark(v)
            setattr(cls, k, wrapped_v)
    return cls


@class_benchmark
class Cat:
    name: str

    def __init__(self, name):
        self.name = name

    def say(self):
        return f'{self.name} - кошка. Говорит МЯУ!'


if __name__ == '__main__':
    cat_1 = Cat('Bylka')
    print(cat_1.say())
#     Почему так некрасиво выводит время?..((
