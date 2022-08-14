from house import House


class Townhouse(House):
    def __init__(self, address, cost):
        super().__init__(address, 60, cost)