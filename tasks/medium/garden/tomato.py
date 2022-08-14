class Tomato:
    index: int
    ripeness: str
    states: tuple = ('Отсутствует', 'Цветение', 'Зеленый', 'Красный')

    def __init__(self, index):
        self.index = index
        self.ripeness = self.states[0]

    def grow(self):
        if self.ripeness != self.states[3]:
            new_ripeness = self.states.index(self.ripeness)
            self.ripeness = self.states[new_ripeness + 1]
        else:
            return self.ripeness

    def is_ripe(self):
        if self.ripeness == self.states[3]:
            return True
        else:
            return False
