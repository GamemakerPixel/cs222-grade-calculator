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
    calculator = GradeCalculator(count, 5, 1, 2)
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
    calculator = GradeCalculator(7, count, 1, 2)
    result_grade = calculator.calculateGrade()
    assert result_grade == grade


MIDSEMESTER_TEST_DATA = [
    (1, "A"),
    (0, "D"),
]


@pytest.mark.parametrize("completed,grade", MIDSEMESTER_TEST_DATA)
def test_midsemester(completed: int, grade: str) -> None:
    calculator = GradeCalculator(7, 5, completed, 2)
    result_grade = calculator.calculateGrade()
    assert result_grade == grade


FINAL_TEST_DATA = [
    (2, "A"),
    (1, "C"),
    (0, "D"),
]


@pytest.mark.parametrize("specification_met,grade", FINAL_TEST_DATA)
def test_final(specification_met: int, grade: str) -> None:
    calculator = GradeCalculator(7, 5, 1, specification_met)
    result_grade = calculator.calculateGrade()
    assert result_grade == grade


