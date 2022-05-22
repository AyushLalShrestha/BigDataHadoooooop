import math
import time
from pprint import pprint

algo = "..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#"
input_file_name = "input.test"

algo = "#.#.##...###......#.##..#..##....#.#.##...#..###....##...#####.#...#.#.#...#..###..#...#......####..#.#..########.#.###......##.##...###.###..######.....####.#..#.#..##..###..####..#....####..######.###..###.........##.##.###......##...#####.######..#.....##..#..#...#.#...#..#..#.#..#..#.##..#####..##.###.####...#..#....##....####...#.#.#.#.#.###...##..#....##......####.##.###...#####..##..#.#...#..#.#..####.###..###..#..####....#.#.##.#..#...#.#...##...#..#.#.##...##..##.####..#...###.#...#####.######....."
input_file_name = "input"

class GridMap(object):
    def __init__(self, input):
        self.rows = len(input)
        self.columns = len(input[0])
        self.map = input
        # print(f"{self.rows} rows, {self.columns} columns")

    def find_point_value(self, x, y, step=1):
        default = "0" if step%2 == 0 else "1"
        adjacents = [
            (x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
            (x, y - 1), (x, y), (x, y + 1),
            (x + 1, y - 1), (x + 1, y), (x + 1, y + 1),
        ]
        value = ""
        
        for adj_x, adj_y in adjacents:
            if not (0 <= adj_x < self.rows):
                value += default
            elif not (0 <= adj_y < self.columns):
                value += default
            else:
                val = self.map[adj_x][adj_y]
                if val == ".":
                    value += "0"
                elif val == "#":
                    value += "1"
        return int(value, 2)

    def count_lit_points(self):
        count = 0
        for x in range(self.rows):
            for y in range(self.columns):
                if self.map[x][y] == "#":
                    count += 1
        return count

rows = []
with open(input_file_name, "r") as fh:
    line = fh.readline()
    while line:
        data = line.strip("\n")
        row = list([i for i in data])
        rows.append(row)
        line = fh.readline()
gridMap = GridMap(rows)

print(gridMap.count_lit_points())
for i in range(50):
    new_rows = []
    for x in range(-2, gridMap.rows + 2):
        new_row = []
        for y in range(-2, gridMap.columns + 2):
            val = gridMap.find_point_value(x, y, step=i)
            val = algo[val]
            new_row.append(val)
        new_rows.append(new_row)
    gridMap = GridMap(new_rows)
print(gridMap.count_lit_points())


# new_rows = []
# for row in gridMap.map[10:-10]:
#     new_row = []
#     for v in row[10:-10]:
#         new_row.append(v)
#     new_rows.append(new_row)
# newGridMap = GridMap(new_rows)

# print(gridMap.count_lit_points())
# for row in gridMap.map:
#     pprint("".join(row))
