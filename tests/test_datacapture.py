from ..stats.datacapture import DataCapture
import pytest
from typing import List


@pytest.fixture()
def get_data_captured() -> List:
    capture = DataCapture()
    capture.add(0)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    stats = capture.build_stats()

    return [capture, stats]


class TestDataCapture():
    def test_add_negative(self, get_data_captured: List):
        data_capture, _ = get_data_captured

        with pytest.raises(ValueError) as e_info:
            data_capture.add(-1)

    def test_add_float(self, get_data_captured: List):
        data_capture, _ = get_data_captured

        with pytest.raises(ValueError) as e_info:
            data_capture.add(2.5)

    def test_value_is_added(self):
        value = 5
        capture = DataCapture()
        capture.add(value)
        assert capture.records.get(value) is not None

    def test_amount_of_values(self, get_data_captured: List):
        data_capture, _ = get_data_captured
        assert data_capture.records.get(0) == 1