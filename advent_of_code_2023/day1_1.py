from utils.reader import load_input
from utils.trebuchet import trebuchet

data = load_input("inputs/day_one_part_1_example.txt")
print(sum(trebuchet(data)))
