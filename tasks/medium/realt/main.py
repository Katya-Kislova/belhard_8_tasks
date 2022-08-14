from house import House
from townhouse import Townhouse
from person import Person


if __name__ == '__main__':
    house_1 = House('Road 1', 45, 12000)
    house_2 = House('Road_2', 35, 9000)
    house_3 = Townhouse('Road_3', 32000)
    house_4 = Townhouse('Road_4', 58999)
    person = Person('Zahar', 23)
    print(person.make_deal(house_2))
    person.earn_money(25000)
    print(person.make_deal(house_1))
