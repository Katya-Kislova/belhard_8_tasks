from tomato import Tomato


class TomatoBush:
    tomato_list: list = []

    def __init__(self, *args: Tomato):
        for i in range(len(args)):
            self.tomato_list.append(args[i])

    def grow_all(self):
        for i in self.tomato_list:
            Tomato.grow(i)

    def all_are_ripe(self):
        counter = 0
        for i in self.tomato_list:
            Tomato.is_ripe(i)
            if Tomato.is_ripe(i):
                counter += 1
                if len(self.tomato_list) == counter:
                    return True
                else:
                    return False

    def give_away_all(self):
        tomato_list_2 = [i for i in self.tomato_list]
        self.tomato_list.clear()
        return tomato_list_2
