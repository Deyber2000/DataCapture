from typeguard import typechecked



class DataCapture:
    """
    A class for capturing data and building statistics from it.
    Methods:
        add(n: int): Add a new data point to the records.
        build_stats() -> Stats: Build a Stats object containing statistics about the captured data.
    """

    def __init__(self):
        self.records = {}
        self.max_number = 0

    def add(self, value) -> None:
        self.max_number = value if value > self.max_number else self.max_number
        self.records[value] = self.records.get(value, 0) + 1

    def build_stats(self):
        count_dict = {}
        current_count = 0
        for i in range(self.max_number + 1):
            if i in self.records:
                count_dict[i] = self.records[i] + current_count
                current_count = count_dict[i]
                print(f"{i} record and current count: {current_count}")
            else:
                count_dict[i] = current_count
        print(self.records)
        return count_dict

if __name__ == '__main__':
    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    stats = capture.build_stats()
    print(stats)
