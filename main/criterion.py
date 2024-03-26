class Criterion:
    def __init__(self, minimums: list[int]):
        self.minimums = minimums

    def get_level(self, value: int) -> int:
        for level, minimum in enumerate(self.minimums):
            if value >= minimum:
                return level
        return len(self.minimums)
