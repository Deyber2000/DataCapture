from annotated_types import Gt
from .stats import Stats
from typing import Annotated

class DataCapture:
    """
    A class for capturing data and building statistics
    Methods:
        add(n: int): Add a new positive value to the records.
        build_stats() -> Stats: Build a Stats object containing the statistics about the captured data.
    """

    def __init__(self):
        self.records = {}
        self.max_number = 0

    def add(self, value: Annotated[int, Gt(0)]) -> None:
        if value < 0 or type(value) is not int:
            raise ValueError('Work with Positive integers Only')
        self.max_number = value if value > self.max_number else self.max_number
        self.records[value] = self.records.get(value, 0) + 1

    def build_stats(self) -> Stats:
        count_dict = {}
        current_count = 0
        for i in range(self.max_number + 1):
            if i in self.records:
                count_dict[i] = self.records[i] + current_count
                current_count = count_dict[i]
            else:
                count_dict[i] = current_count
        return Stats(count_dict, self.max_number)