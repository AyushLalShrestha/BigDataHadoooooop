
import os
from pprint import pprint

current_dir = os.path.dirname(os.path.abspath(__file__))
count = 2022

rocks = [
["####"],

[
".#.",
"###",
".#."
],

[
"..#",
"..#",
"###"
],

[
"#",
"#",
"#",
"#"
],

[
"##",
"##"
]

]

WIDTH = 7

def print_grid(grid):
    for row in grid[::-1]:
        print("".join(row))

def get_starting_points(rock_no, start_x, start_y):
    coords = []
    rock = rocks[rock_no]
    for i in range(len(rock)):
        row_coords = []
        for j in range(len(rock[0])):
            row_coords.append( (start_x + j, start_y + i) )
        coords.append(row_coords)
    return coords

def move(co_ords, direction):
    direction_map = {
        "<": (-1, 0),
        ">": (1, 0),
        "d": (0, -1),
        "u": (0, 1)
    }
    vector = direction_map[direction]
    final_coords = []
    for row in co_ords:
        row_coords = []
        for i, j in row:
            x, y = i + vector[0], j + vector[1]
            if 0 <= x < WIDTH:
                row_coords.append((x, y))
            else:
                return co_ords

        final_coords.append(row_coords)
    return final_coords


def does_intersect(rock_number, co_ords, grid):
    rock = rocks[rock_number]
    for i, row in enumerate(co_ords):
        for j, p in enumerate(row):
            if p[1] < 0:
                return True

            if len(grid) <= p[1]:
                return False

            v = rock[::-1][i][j]
            if v == "#" and grid[p[1]][p[0]] == "#":
                return True
    return False

def rest_rock_at_grid(rock_number, co_ords, grid):
    rock = rocks[rock_number]
    for i, row in enumerate(co_ords):
        for j, p in enumerate(row):
            if p[1] - len(grid) >= 0:
                for _ in range(p[1] - len(grid) + 1):
                    grid.append( ['.', '.', '.', '.', '.', '.', '.'] )

            v = rock[::-1][i][j]
            if v == "#":
                grid[p[1]][p[0]] = v

def main(input_line):
    rock_count = 0
    ins_ptr = -1
    grid = []
    while rock_count < count:
        rock_number = rock_count % 5
        start_x = 2
        start_y = len(grid) + 3
        co_ords = get_starting_points(rock_number, start_x, start_y)
        while True:
            ins_ptr += 1
            ins = input_line[ins_ptr % len(input_line)]

            # move "<" or ">"
            next_co_ords = move(co_ords, ins)
            if not does_intersect(rock_number, next_co_ords, grid):
                co_ords = next_co_ords

            # move down
            next_co_ords = move(co_ords, "d")
            if does_intersect(rock_number, next_co_ords, grid):
                # rest the shape in the grid at co_ords
                rest_rock_at_grid(rock_number, co_ords, grid)
                break
            co_ords = next_co_ords
        rock_count += 1

    print_grid(grid)
    print(len(grid))

if __name__ == "__main__":
    input_file_path = os.path.join(current_dir, "input")
    # input_file_path = os.path.join(current_dir, "input.test")
    _input = open(input_file_path, "r").read().strip()

    main(_input)
