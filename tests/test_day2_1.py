from utils.reader import load_input
from advent_of_code_2023.day2_1 import get_possible_games


def test_success_example():
    data = load_input("inputs/day_two_part_1_example.txt")
    possible_games = get_possible_games(data)
    assert sum(possible_games) == 8


def test_success_input():
    data = load_input("inputs/day_two.txt")
    possible_games = get_possible_games(data)
    assert sum(possible_games) == 2679
