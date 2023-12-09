from utils.trebuchet import trebuchet
from utils.reader import load_input


def test_success_example():
    data = load_input("inputs/day_one_part_1_example.txt")
    numbers = trebuchet(data)
    assert sum(numbers) == 142


def test_success_input():
    data = load_input("inputs/day_one.txt")
    numbers = trebuchet(data)
    assert sum(numbers) == 55029
