class Criteria:
    def __init__(self, criteria_minimums: list[list[int]]):
        self.criteria_minimums = criteria_minimums

    def _meets_minimums(self, inputs: list[int], minimums: list[int]) -> bool:
        for input, minimum in zip(inputs, minimums):
            if input < minimum:
                return False
        return True

    def get_maximized_level(self, inputs: list[int]) -> int:
        for index, level_minimums in enumerate(self.criteria_minimums):
            if self._meets_minimums(inputs, level_minimums):
                return index
        return len(self.criteria_minimums)



