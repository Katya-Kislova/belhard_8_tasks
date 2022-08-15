"""
Описать класс Warrior:

- атрибут name - имя юнита (тип str)
- атрибут health_points - показатель здоровья (тип int от 0 до 100)
- магический метод __init__, который принимает аргумент name и создает юнита со
  100 health_points
- метод hit, который принимает аргумент other типа Warrior. Если значение
 health_points у other <= 0 бросить исключение ValueError("Второй воин мертв").
 Если нет, то снять у other 20 health_points и вывести на экран сообщение
 "{self.name} атаковал {other.name}. У {other.name} {other.health_points} HP"

Описать класс Arena:

- атрибут warriors - все воины на арене (тип list)
- магический метод __init__, который принимает необязательный аргумент warriors.
 Если был передан список warriors, та заполняет им атрибут. Если нет, то заполняет
 пустым списком.
- метод add_warrior, который принимает аргумент warrior и добавляет его к warriors.
 Если данный воин уже есть в списке, то бросить исключение ValueError("Воин уже на арене").
 Если нет, то добавить воина к списку warriors и вывести сообщение на экран
 "{warrior.name} участвует в битве"
- метод choose_warrior, который не принимает аргументов и возвращает случайного
  воина из warriors
- метод battle, который не принимает аргументов и симулирует битву. Сперва
 должна пройти проверка, что воинов на арене больше 1. Если меньше, то бросить
 исключение ValueError("Количество воинов на арене должно быть больше 1").
 Битва продолжается, пока на арене не останется только один воин. Сперва
 в случайном порядке выбираются атакующий и защищающийся. Атакующий ударяет
 защищающегося. Если у защищающегося осталось 0 health_points, то удалить его
 из списка воинов и вывести на экран сообщение "{defender.name} пал в битве".
 Когда останется только один воин, то вывести сообщение "Победил воин: {winner.name}".
 Вернуть данного воина из метода battle.
"""
import random


class Warrior:
    name: str
    health_points: int

    def __init__(self, name):
        self.name = name
        self.health_points = 100

    def hit(self, other):
        if other.health_points <= 0:
            raise ValueError("Второй воин мертв")
        else:
            other.health_points -= 20
            return f"{self.name} атаковал {other.name}. У {other.name} {other.health_points} HP"


class Arena:
    warriors_list: list

    def __init__(self, warriors):
        self.warriors = warriors

    def add_warrior(self, warrior):
        if warrior not in self.warriors:
            self.warriors.append(warrior)
            print(f"{warrior.name} участвует в битве")
        else:
            raise ValueError("Воин уже на арене")

    def choose_warrior(self):
        return random.choice(self.warriors)

    def battle(self):
        if len(self.warriors) < 1:
            raise ValueError("Количество воинов на арене должно быть больше 1")
        while True:
            for i in range(len(self.warriors)):
                attacking_warrior = random.choice(self.warriors)
                defensive_warrior = random.choice(self.warriors)
                if attacking_warrior.name == defensive_warrior.name:
                    continue
                else:
                    Warrior.hit(attacking_warrior, defensive_warrior)
                if defensive_warrior.health_points <= 0:
                    self.warriors.remove(defensive_warrior)
                    print(f"{defensive_warrior.name} пал в битве")
            if len(self.warriors) == 1:
                print(f"Победил воин: {self.warriors[0].name}")
                return self.warriors[0].name


if __name__ == '__main__':
    warrior_1 = Warrior('1')
    warrior_2 = Warrior('2')
    warrior_3 = Warrior('3')

    warriors = [warrior_1, warrior_2, warrior_3]
    arena_1 = Arena(warriors)
    print(arena_1.battle())
