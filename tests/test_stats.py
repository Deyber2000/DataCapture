from ..stats.datacapture import DataCapture
from ..stats.stats import Stats
import pytest
from typing import List


@pytest.fixture()
def get_data_captured() -> Stats:
    capture = DataCapture()
    capture.add(0)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    stats = capture.build_stats()

    return stats


class TestStats():
    def test_less(self, get_data_captured: Stats):
        stats = get_data_captured

        assert stats.less(0) == 0, "Negatives should not be supported"
        assert stats.less(9) == 4

        with pytest.raises(TypeError):
            stats.less(None)

        with pytest.raises(TypeError):
            stats.less('invalid string')

    def test_greater(self, get_data_captured: Stats):
        stats = get_data_captured

        assert stats.greater(0) == 4
        assert stats.greater(9) == 0

        with pytest.raises(TypeError):
            stats.greater(None)

        with pytest.raises(TypeError):
            stats.greater('invalid string')


    def test_between(self, get_data_captured: Stats):
        stats = get_data_captured

        assert stats.between(0, 9) == 5
        assert stats.between(0, 0) == 1

        with pytest.raises(TypeError):
            stats.between(None, None)

        with pytest.raises(TypeError):
            stats.between('invalid string', None)