import re

NUMBERS = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def numerify(line, order=0):
    if order == -1:
        line = line[::-1]

    copy_str = line
    for index, letter in enumerate(line):
        for value, key in enumerate(NUMBERS):
            if order == -1:
                key = key[::-1]

            is_number_str = line[index : index + len(key)]
            if is_number_str in key and len(is_number_str) >= 3:
                copy_str = copy_str.replace(key, str(value))
    if order == -1:
        copy_str = copy_str[::-1]

    return copy_str


def map_str_2_number(data):
    mapped_lines = []
    for item in data:
        copy_str = f"{numerify(item, 0)}{numerify(item, -1)}"
        mapped_lines.append(copy_str)
    return mapped_lines
