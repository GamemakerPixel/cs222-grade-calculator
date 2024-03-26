from main.criterion import Criterion

def test_get_level():
    criterion_minimums = [90, 80, 70, 60, 50, 40, 30, 20, 10]
    criterion = Criterion(criterion_minimums)
    level_met = criterion.get_level(55)
    assert level_met == 4
