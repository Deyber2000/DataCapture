class Stats:
    def __init__(self, count_dict, items_amount):
        self.count_dict = count_dict
        self.items_amount = items_amount

    def greater(self, value):
        if value > self.items_amount:
            return 0
        return self.count_dict[self.items_amount] - self.count_dict[value]