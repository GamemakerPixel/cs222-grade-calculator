import pytest

from main.criteria import Criteria


GET_MAXIMIZED_LEVEL_TEST_DATA = [
    ([5, 5, 5], 0),
    ([5, 3, 5], 1),
    ([4, 5, 5], 1),
    ([2, 5, 5], 2),
    ([2, 2, 2], 2),
]

@pytest.mark.parametrize("input,expected", GET_MAXIMIZED_LEVEL_TEST_DATA)
def test_get_maximized_level(input: list[int], expected: int):
    criteria_minimums = [
        [5, 5, 5],
        [4, 3, 2],
        [2, 2, 2],
    ]

    criteria = Criteria(criteria_minimums)
    maximized_level = criteria.get_maximized_level(input)
    assert maximized_level == expected

