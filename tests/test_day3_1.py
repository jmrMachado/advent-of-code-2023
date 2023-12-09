from utils.reader import load_input
from advent_of_code_2023.day3_1 import populate_matrix, get_part_numbers


def test_success_example():
    data = load_input("inputs/day_three_part_1_example.txt")
    matrix = populate_matrix(height=10, width=10, data=data)
    part_numbers = get_part_numbers(matrix=matrix)
    assert sum(part_numbers) == 4361


def test_success_input():
    data = load_input("inputs/day_three.txt")
    matrix = populate_matrix(height=140, width=140, data=data)
    part_numbers = get_part_numbers(matrix=matrix)
    assert sum(part_numbers) == 536576
