from main.criterion import Criterion

class GradeCalculator:
    GRADES = ["A", "B", "C", "D", "F"]
    ASSIGNMENT_MINIMUMS = [7, 6, 5, 4]
    ACHIEVEMENT_MINIMUMS = [5, 4, 3, 2]

    def __init__(self, assignments: int, achievements: int):
        self.assignments = assignments
        self.achievements = achievements

    def calculateGrade(self) -> str:
        assignment_criterion = Criterion(self.ASSIGNMENT_MINIMUMS)
        assignment_level = assignment_criterion.get_level(self.assignments)

        achievement_criterion = Criterion(self.ACHIEVEMENT_MINIMUMS)
        achievement_level = achievement_criterion.get_level(self.achievements)

        final_grade_level = max(assignment_level, achievement_level)
        return self.GRADES[final_grade_level]
