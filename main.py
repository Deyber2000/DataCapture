from typeguard import typechecked
from stats.stats import Stats
from typing import Annotated
from annotated_types import Gt


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
        if value < 0:
            raise ValueError('Work with Positive Numbers Only')
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


if __name__ == '__main__':
    capture = DataCapture()
    capture.add(0)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    stats = capture.build_stats()
    print(stats.between(4, 9))
