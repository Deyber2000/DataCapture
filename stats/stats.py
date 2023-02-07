class Stats:
    def __init__(self, count_dict, items_amount):
        self.count_dict = count_dict
        self.items_amount = items_amount

    def greater(self, value):
        return 0 if value > self.items_amount else\
            self.count_dict[self.items_amount] - self.count_dict[value]

    def less(self, value):
        if value > self.items_amount:
            return self.count_dict[self.items_amount]
        elif value < 1:
            return 0
        return self.count_dict[value-1]