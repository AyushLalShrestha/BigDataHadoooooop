
from collections import defaultdict
import os

current_dir = os.path.dirname(os.path.abspath(__file__))


def main(input_lines):
    cave = defaultdict(lambda: ".")
    max_height = 0
    for line in input_lines:
        points = line.split("->")
        points = [p.strip(" ").split(",") for p in points]
        points = [(int(p[0]), int(p[1])) for p in points]
        for i in range(len(points) - 1):
            ps = []
            p1 = points[i]
            p2 = points[i + 1]

            if p1[0] == p2[0]:
                _range = [p1[1], p2[1]] if p1[1] < p2[1] else [p2[1], p1[1]]
                for y in range(_range[0], _range[1] + 1):
                    ps.append((p1[0], y))
            elif p1[1] == p2[1]:
                _range = [p1[0], p2[0]] if p1[0] < p2[0] else [p2[0], p1[0]]
                for x in range(_range[0], _range[1] + 1):
                    ps.append((x, p1[1]))
            for p in ps:
                cave[p] = "#"
                if p[1] > max_height:
                    max_height = p[1]

    sand_no = 0
    while True:
        p = (500, -1)
        while True:
            if p[1] > max_height:
                return sand_no
            if cave[(p[0], p[1] + 1)] == ".":
                p = (p[0], p[1] + 1)
            elif cave[(p[0] - 1, p[1] + 1)] == ".":
                p = (p[0] - 1, p[1] + 1)
            elif cave[(p[0] + 1, p[1] + 1)] == ".":
                p = (p[0] + 1, p[1] + 1)
            else:
                # Rest on this point
                cave[p] = "o"
                sand_no += 1
                break


if __name__ == "__main__":
    input_file_path = os.path.join(current_dir, "input")
    input_file_path = os.path.join(current_dir, "input.test")
    _input = open(input_file_path, "r").read()
    input_lines = _input.split("\n")

    res = main(input_lines)
    print(res)
