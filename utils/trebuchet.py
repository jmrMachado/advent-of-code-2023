def get_numbers(line):
    digits = []
    for c in line:
        if c.isdigit():
            digits.append(c)

    if len(digits) == 1:
        return int(f"{digits[0]}{digits[0]}")
    return int(f"{digits[0]}{digits[-1]}")


def trebuchet(data):
    numbers = []
    for line in data:
        numbers.append(get_numbers(line))
    return numbers
