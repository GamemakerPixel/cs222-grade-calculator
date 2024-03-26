import pytest

from main.criterion import Criterion
from main.mapped_criterion import MappedCriterion

MINIMUMS = [75, 50, 25]

MAP_TEST_DATA = [
    ([0, 2, 3], 60, 2),
    ([1, -2, 6], 30, 6),
    ([-1, -2, -3], 100, -1)
]


@pytest.mark.parametrize("mapping,value,expected", MAP_TEST_DATA)
def test_map(mapping: list[int], value: int, expected: int):
    mapped_criterion = MappedCriterion(MINIMUMS, mapping)
    level = mapped_criterion.get_level(value)
    assert level == expected
