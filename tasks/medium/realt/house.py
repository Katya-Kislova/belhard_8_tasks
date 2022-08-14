class House:
    address: str
    area: int
    cost: float

    def __init__(self, address, area, cost):
        self.address = address
        self.area = area
        self.cost = cost

    def increase_cost(self, value):
        self.cost += value

    def decrease_cost(self, value_2):
        self.cost -= value_2
