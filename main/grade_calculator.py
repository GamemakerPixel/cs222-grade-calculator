class GradeCalculator:
    GRADES = ["A", "B", "C", "D", "F"]
    ASSIGNMENT_MINIMUMS = [7, 6, 5, 4]

    def __init__(self, assignments: int):
        self.assignments = assignments

    def calculateGrade(self) -> str:
        for index, minimum in enumerate(self.ASSIGNMENT_MINIMUMS):
            if self.assignments >= minimum:
                return self.GRADES[index]
        return self.GRADES[-1]
