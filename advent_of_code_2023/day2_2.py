from math import prod
from utils.reader import load_input


def get_fewest_cube_counts(game):
    fewest_cube_counts = {"red": 0, "green": 0, "blue": 0}
    cube_set = game.split(": ")[1].split(";")
    for entry in cube_set:
        draft = entry.split(", ")
        for cube in draft:
            amount, color = cube.split()
            fewest_cube_counts[color] = max(int(amount), fewest_cube_counts[color])

    return list(fewest_cube_counts.values())


def get_powers(data):
    powers = []
    for game in data:
        powers.append(prod(get_fewest_cube_counts(game)))
    return powers
