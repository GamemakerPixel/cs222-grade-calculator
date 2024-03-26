from main.criterion import Criterion
from main.mapped_criterion import MappedCriterion

class GradeCalculator:
    GRADES = ["A", "B", "C", "D", "F"]
    ASSIGNMENT_MINIMUMS = [7, 6, 5, 4]
    ACHIEVEMENT_MINIMUMS = [5, 4, 3, 2]
    MIDSEMESTER_MINIMUMS = [1]

    MIDSEMESTER_MAPPING = [0, 3]


    def __init__(self, assignments: int, achievements: int, midsemester: int):
        self.criteria_inputs = [
            assignments,
            achievements,
            midsemester,
        ]
        self.criteria = [
            Criterion(self.ASSIGNMENT_MINIMUMS),
            Criterion(self.ACHIEVEMENT_MINIMUMS),
            MappedCriterion(self.MIDSEMESTER_MINIMUMS, self.MIDSEMESTER_MAPPING),
        ]

    def calculateGrade(self) -> str:
        max_grade_level = 0
        for criterion_input, criterion in zip(self.criteria_inputs, self.criteria):
            grade_level = criterion.get_level(criterion_input)
            max_grade_level = max(max_grade_level, grade_level)

        return self.GRADES[max_grade_level]
