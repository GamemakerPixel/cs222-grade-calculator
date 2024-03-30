from main.grade_calculator import GradeCalculator

NUMERIC_INPUT_REMINDER = "Invalid input, please enter an integer between {min} and {max}."

ASSIGNMENTS_PROMPT = "Enter the number of assignments completed:"
ACHIEVEMENTS_PROMPT = "Enter the number of achivements completed:"
MIDTERM_PROMPT = "Did you complete the midterm reflection?"
FINAL_PROMPT = "What criteria did you meet for the final?"
PROJECT_PROMPT = "What grade did you get for the {project_name} iteration {iteration_number}?"

ASSIGNMENTS_MAX = 7
ACHIEVEMENTS_MAX = 5

MIDTERM_MENU_OPTIONS = [
    "No",
    "Yes",
]

FINAL_MENU_OPTIONS = [
    "Neither",
    "Minimum",
    "Full",
]

PROJECT_GRADE_MENU_OPTIONS = [
    "F",
    "D",
    "C",
    "B",
    "A",
]

PROJECT_NAMES = [
    "first",
    "final",
]

PROJECT_ITERATION_COUNTS = [
    2,
    3,
]

GRADE_REPORT = "The final grade is {grade}."


def _get_valid_numeric_input(
        inclusive_min: int,
        inclusive_max: int
) -> int:
    while True:
        try:
            raw_input = int(input())
            if (raw_input < inclusive_min or raw_input > inclusive_max):
                raise ValueError
            return raw_input
        except ValueError:
            print(NUMERIC_INPUT_REMINDER.format(
                min=inclusive_min,
                max=inclusive_max
            ))
            continue


def _display_numeric_prompt(prompt: str, inclusive_min: int, inclusive_max: int) -> int:
    print(prompt + "\n")
    return _get_valid_numeric_input(inclusive_min, inclusive_max)


def _display_menu(prompt: str, options: list[str]) -> int:
    print(prompt)
    for index, option in enumerate(options):
        print(f"{index + 1}. {option}")

    return _get_valid_numeric_input(1, len(options)) - 1


def _display_project_prompts() -> list[int]:
    grades = []

    for project_name, interation_count in zip(
        PROJECT_NAMES, PROJECT_ITERATION_COUNTS
    ):
        for iteration_number in range(1, interation_count + 1):
            formatted_prompt = PROJECT_PROMPT.format(
                project_name=project_name,
                iteration_number=iteration_number
            )
            grade = _display_menu(formatted_prompt, PROJECT_GRADE_MENU_OPTIONS)
            grades.append(grade)

    return grades


def main():
    #calculator = GradeCalculator(
    #    _display_numeric_prompt(ASSIGNMENTS_PROMPT, 0, ASSIGNMENTS_MAX),
    #    _display_numeric_prompt(ACHIEVEMENTS_PROMPT, 0, ACHIEVEMENTS_MAX),
    #    _display_menu(MIDTERM_PROMPT, MIDTERM_MENU_OPTIONS),
    #    _display_menu(FINAL_PROMPT, FINAL_MENU_OPTIONS),
    #    _display_project_prompts(),
    #)

    #print(GRADE_REPORT.format(grade=calculator.calculateGrade()))
    print(_display_project_prompts())
    


if __name__ == "__main__":
    main()
