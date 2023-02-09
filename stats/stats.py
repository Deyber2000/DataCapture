from typing import Annotated
from annotated_types import Gt


class Stats:
    def __init__(self, count_dict: dict, items_amount: Annotated[int, Gt(0)]):
        """Intantiates object for items counting
        Parameters
        ----------
        count_dict : dict
            Dictionary with items count
        items_amount : int
            Amount of items to process
        """
        self.count_dict = count_dict
        self.items_amount = items_amount

    def greater(self, value: Annotated[int, Gt(0)]) -> int:
        """Receives integer and returns the amount of items greater than the given value
        Parameters
        ----------
        value : int
            Value to compare
        Returns
        -------
        int
            Amount of numbers greater than the given value    
        """
        return 0 if value > self.items_amount else\
            self.count_dict[self.items_amount] - self.count_dict[value]

    def less(self, value: Annotated[int, Gt(0)]):
        """Receives integer and returns the amount of items less than the given value
        Parameters
        ----------
        value : int
            Value to compare
        Returns
        -------
        int
            Amount of numbers less than the given value    
        """
        if value > self.items_amount:
            return self.count_dict[self.items_amount]
        elif value < 1:
            return 0
        return self.count_dict[value-1]

    def between(self, low_value: Annotated[int, Gt(0)], high_value: Annotated[int, Gt(0)]):
        """Receives two integers and returns the amount of items between them
        Parameters
        ----------
        low_value : int
            low bound value to compare against
        high_value : int
            upper bound value to compare against
        Returns
        -------
        int
            Amount of numbers between the given values 
        """
        return self.less(high_value + 1) - self.less(low_value)