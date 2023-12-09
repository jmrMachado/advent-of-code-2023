from utils.reader import load_input
from advent_of_code_2023.day3_2 import populate_matrix, get_gear_ratios


def test_success_example():
    data = load_input("inputs/day_three_part_1_example.txt")
    matrix = populate_matrix(height=10, width=10, data=data)
    gear_ratios = get_gear_ratios(matrix=matrix)
    assert sum(gear_ratios) == 467835


def test_success_input():
    data = load_input("inputs/day_three.txt")
    matrix = populate_matrix(height=140, width=140, data=data)
    gear_ratios = get_gear_ratios(matrix=matrix)
    assert sum(gear_ratios) == 75741499
