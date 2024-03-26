import pytest

from main.grade_calculator import GradeCalculator

ASSIGNMENT_TEST_DATA = [
    (7, "A"),
    (6, "B"),
    (5, "C"),
    (4, "D"),
    (3, "F"),
]


@pytest.mark.parametrize("count,grade", ASSIGNMENT_TEST_DATA)
def test_assignments(count: int, grade: str) -> None:
    calculator = GradeCalculator(count, 5)
    result_grade = calculator.calculateGrade()
    assert result_grade == grade


ACHIEVEMENT_TEST_DATA = [
    (5, "A"),
    (4, "B"),
    (3, "C"),
    (2, "D"),
    (1, "F"),
]


@pytest.mark.parametrize("count,grade", ACHIEVEMENT_TEST_DATA)
def test_achievements(count: int, grade: str) -> None:
    calculator = GradeCalculator(7, count)
    result_grade = calculator.calculateGrade()
    assert result_grade == grade

