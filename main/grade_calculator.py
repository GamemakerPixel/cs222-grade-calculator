from main.criterion import Criterion

class GradeCalculator:
    GRADES = ["A", "B", "C", "D", "F"]
    ASSIGNMENT_MINIMUMS = [7, 6, 5, 4]

    def __init__(self, assignments: int):
        self.assignments = assignments

    def calculateGrade(self) -> str:
        assignment_criterion = Criterion(self.ASSIGNMENT_MINIMUMS)
        assignment_level = assignment_criterion.get_level(self.assignments)
        return self.GRADES[assignment_level]
