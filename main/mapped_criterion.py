from main.criterion import Criterion

class MappedCriterion(Criterion):
    def __init__(self, minimums: list[int], mapping: list[int]):
        super().__init__(minimums)
        self.mapping = mapping

    def get_level(self, value: int) -> int:
        unmapped_level = super().get_level(value)
        return self.mapping[unmapped_level]

    
