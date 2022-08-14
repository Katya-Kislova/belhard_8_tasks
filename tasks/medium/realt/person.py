class Person:
    name: str
    age: int
    money: float
    realty: list

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.money = 0
        self.realty = []

    def info(self):
        print(self.name, self.age, self.realty, self.money)

    def earn_money(self, value):
        self.money += value

    def make_deal(self, house):
        if self.money >= house.cost:
            self.money -= house.cost
            self.realty.append(house)
            return f'Вы купили дом'
        else:
            return f'Мало деняк. Копи и живи дальше в съёмной однушке'
