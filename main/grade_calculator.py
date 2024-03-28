from main.criteria import Criteria


class GradeCalculator:
    GRADES = ["A", "B", "C", "D", "F"]
    CRITERIA_MINIMUMS = [
        [7, 5, 1, 2, [1, 1, 1, 1, 4]],
        [6, 4, 1, 2, [0, 0, 0, 0, 3]],
        [5, 3, 1, 1, [0, 0, 0, 0, 2]],
        [4, 2, 0, 0, [0, 0, 0, 0, 1]],
    ]

    def __init__(
            self,
            assignments: int,
            achievements: int,
            midsemester: int,
            final: int
    ):
        self.criteria_inputs = [
            assignments,
            achievements,
            midsemester,
            final,
        ]

    def calculateGrade(self) -> str:
        non_project_minimums = [self.CRITERIA_MINIMUMS[index][:-1] for index in range(len(self.CRITERIA_MINIMUMS))]
        non_project_criteria = Criteria(non_project_minimums)

        return self.GRADES[non_project_criteria.get_maximized_level(self.criteria_inputs)]
