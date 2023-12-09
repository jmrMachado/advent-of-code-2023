def game_number(game):
    return int(game.split(":")[0].split(" ")[1])


def game_check(game):
    cube_set = game.split(": ")[1].split(";")
    for entry in cube_set:
        draft = entry.split(", ")
        for cube in draft:
            amount, color = cube.split()
            if color == "red" and int(amount) > 12:
                return False
            if color == "green" and int(amount) > 13:
                return False
            if color == "blue" and int(amount) > 14:
                return False
    return True


def get_possible_games(data):
    possible_games = []
    for game in data:
        if game_check(game):
            possible_games.append(game_number(game))
    return possible_games
