from utils.reader import load_input
from utils.trebuchet import trebuchet
from advent_of_code_2023.day1_2 import map_str_2_number


def test_success_example():
    data = load_input("inputs/day_one_part_2_example.txt")
    data = map_str_2_number(data)
    numbers = trebuchet(data)
    assert sum(numbers) == 281


def test_success_input():
    data = load_input("inputs/day_one.txt")
    data = map_str_2_number(data)
    numbers = trebuchet(data)
    assert sum(numbers) == 55686
