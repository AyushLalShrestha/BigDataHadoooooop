
from pprint import pprint

input = [
    [0, 1, 2, 3, 4],
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 6],
    [3, 4, 5, 6, 7],
    [4, 5, 6, 7, 8],
]

mul_factor = 5

map = []
for _ in range(25):
    map.append([0] * 25)

rows = 5
for j in range(mul_factor):
    for x_coord, row in enumerate(input):
        for y_coord, elem in enumerate(row):
            val = elem + j * 1
            val = val if val <= 9 else val % 9
            map[x_coord][y_coord + len(row) * j] = val
            
for j in range(mul_factor):
    for x_coord, row in enumerate(map[0:rows]):
        for y_coord, elem in enumerate(row):
            val = elem + j * 1
            val = val if val <= 9 else val % 9
            map[x_coord +  rows * j][y_coord] = val
pprint(map)