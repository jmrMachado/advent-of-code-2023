from utils.reader import load_input
from advent_of_code_2023.day2_2 import get_powers


def test_success_example():
    data = load_input("inputs/day_two_part_1_example.txt")
    powers = get_powers(data)
    assert sum(powers) == 2286


def test_success_input():
    data = load_input("inputs/day_two.txt")
    powers = get_powers(data)
    assert sum(powers) == 77607
