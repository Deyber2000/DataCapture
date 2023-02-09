from typing import Annotated
from annotated_types import Gt


class Stats:
    def __init__(self, count_dict: dict, items_amount: Annotated[int, Gt(0)]):
        self.count_dict = count_dict
        self.items_amount = items_amount

    def greater(self, value: Annotated[int, Gt(0)]):
        return 0 if value > self.items_amount else\
            self.count_dict[self.items_amount] - self.count_dict[value]

    def less(self, value: Annotated[int, Gt(0)]):
        if value > self.items_amount:
            return self.count_dict[self.items_amount]
        elif value < 1:
            return 0
        return self.count_dict[value-1]

    def between(self, low_value: Annotated[int, Gt(0)], high_value: Annotated[int, Gt(0)]):
        return self.less(high_value + 1) - self.less(low_value)