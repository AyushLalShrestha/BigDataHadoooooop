
import math
from collections import defaultdict
import os

current_dir = os.path.dirname(os.path.abspath(__file__))


def main(input_lines):
    # Map to store all sensor points & their MH Distance 
    sensor_mh_map = {}
    min_x, max_x = math.inf, -math.inf
    for line in input_lines:
        parts = line.split(":")
        x1 = int(parts[0].split("x=")[1].split(",")[0])
        y1 = int(parts[0].split("y=")[1])

        x2 = int(parts[1].split("x=")[1].split(",")[0])
        y2 = int(parts[1].split("y=")[1])

        mh_distance = abs(x2 - x1) + abs(y2 - y1)
        if x1 - mh_distance < min_x:
            min_x = x1 - mh_distance
        if x1 + mh_distance > max_x:
            max_x = x1 + mh_distance
        sensor_mh_map[(x1, y1)] = (x2, y2, mh_distance)

    y = 2000000
    # y = 10
    count = 0
    for x in range(min_x, max_x + 1):
        for p, v in sensor_mh_map.items():
            x1, y1 = p[0], p[1]
            bx, by, mh_distance = v[0], v[1], v[2]
            distance = abs(x - x1) + abs(y - y1)
            if distance <= mh_distance and (x, y) != (bx, by):
                count += 1
                break
    print(count)

if __name__ == "__main__":
    input_file_path = os.path.join(current_dir, "input")
    # input_file_path = os.path.join(current_dir, "input.test")
    _input = open(input_file_path, "r").read()
    input_lines = _input.split("\n")

    main(input_lines)
