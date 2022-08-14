from tomato import Tomato
from tomato_bush import TomatoBush
from gardener import Gardener


if __name__ == '__main__':
    tomato_1 = Tomato(1)
    tomato_2 = Tomato(2)
    tomato_3 = Tomato(3)
    tomato_4 = Tomato(4)
    tomato_5 = Tomato(5)
    tomato_6 = Tomato(6)
    tomato_7 = Tomato(7)
    tomato_8 = Tomato(8)
    tomato_9 = Tomato(9)
    bush_1 = TomatoBush(tomato_1, tomato_2, tomato_3)
    bush_2 = TomatoBush(tomato_4, tomato_5, tomato_6)
    bush_3 = TomatoBush(tomato_7, tomato_7, tomato_9)
    gardener_1 = Gardener('Bob', bush_1, bush_2, bush_3)
    gardener_1.work()
    gardener_1.harvest()
    gardener_1.work()
    print(len(gardener_1.harvest()))
