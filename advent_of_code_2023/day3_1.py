from utils.matrix import Matrix
from utils.reader import load_input
import re

NOT_SYMBOL_LIST = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]


def populate_matrix(height: int, width: int, data: list):
    matrix = Matrix(height, width)
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            matrix.set_value(i, j, char)
    return matrix


def get_part_numbers(matrix: Matrix):
    part_numbers = []
    for i in range(matrix.rows):
        line = matrix.get_row(i)
        for m in re.finditer(r"\d{1,3}", line):
            start, end, is_valid = m.start(), m.end(), False
            for j in range(start - 1, end + 1):
                if (
                    i > 0
                    and 0 <= j < matrix.cols
                    and matrix.get_value(i - 1, j) not in NOT_SYMBOL_LIST
                ):
                    is_valid = True
                    break

                if (
                    i < matrix.rows - 1
                    and 0 <= j < matrix.cols
                    and matrix.get_value(i + 1, j) not in NOT_SYMBOL_LIST
                ):
                    is_valid = True
                    break

            if start > 0 and line[start - 1] not in NOT_SYMBOL_LIST:
                is_valid = True

            if end < matrix.rows and line[end] not in NOT_SYMBOL_LIST:
                is_valid = True

            if is_valid:
                part_numbers.append(int(m.group(0)))
    return part_numbers


data = load_input("inputs/day_three_part_1_example.txt")
matrix = populate_matrix(height=10, width=10, data=data)
part_numbers = get_part_numbers(matrix=matrix)
print(sum(part_numbers))
