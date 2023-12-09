from utils.matrix import Matrix
from utils.reader import load_input
from collections import defaultdict
from math import prod
import re

NUMBERS_LIST = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def populate_matrix(height: int, width: int, data: list):
    matrix = Matrix(height, width)
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            matrix.set_value(i, j, char)
    return matrix


def get_gear_ratios(matrix: Matrix):
    all_adjacent_numbers = get_all_adjacent_numbers(matrix=matrix)
    gear_numbers = []
    for gear, numbers in all_adjacent_numbers.items():
        if len(numbers) == 2:
            gear_numbers.append(prod(numbers))
    return gear_numbers


def get_all_adjacent_numbers(matrix: Matrix):
    all_adjacent_numbers = defaultdict(list)
    for i in range(matrix.rows):
        line = matrix.get_row(i)
        for m in re.finditer(r"\d{1,3}", line):
            start, end, is_valid = m.start(), m.end(), False
            for j in range(start - 1, end + 1):
                if i > 0 and 0 <= j < matrix.cols and matrix.get_value(i - 1, j) == "*":
                    is_valid = i - 1, j
                    break

                if (
                    i < matrix.rows - 1
                    and 0 <= j < matrix.cols
                    and matrix.get_value(i + 1, j) == "*"
                ):
                    is_valid = i + 1, j
                    break

            if start > 0 and line[start - 1] == "*":
                is_valid = i, start - 1

            if end < matrix.rows and line[end] == "*":
                is_valid = i, end

            if is_valid:
                all_adjacent_numbers[is_valid].append(int(m.group(0)))

    return all_adjacent_numbers


data = load_input("inputs/day_three_part_1_example.txt")
matrix = populate_matrix(height=10, width=10, data=data)
gear_ratios = get_gear_ratios(matrix=matrix)
print(sum(gear_ratios))
