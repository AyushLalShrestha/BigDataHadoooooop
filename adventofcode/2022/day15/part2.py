
import os

current_dir = os.path.dirname(os.path.abspath(__file__))


def main(input_lines):
    sensor_mh_map = {}

    # Record the position of all sensor, and it's MH Distance
    for line in input_lines:
        parts = line.split(":")
        x1 = int(parts[0].split("x=")[1].split(",")[0])
        y1 = int(parts[0].split("y=")[1])

        x2 = int(parts[1].split("x=")[1].split(",")[0])
        y2 = int(parts[1].split("y=")[1])

        mh_distance = abs(x2 - x1) + abs(y2 - y1)
        sensor_mh_map[(x1, y1)] = mh_distance

    _max = 4000000
    # _max = 20
    py = 0

    while 0 <= py <= _max:
        px = 0
        while 0 <= px <= _max:
            for s, mh in sensor_mh_map.items():
                sx = s[0]
                sy = s[1]
                distance = abs(sx - px) + abs(sy - py)
                if distance <= mh:
                    # calculate next px to jump to
                    px = mh - abs(py - sy) + sx
                    break
            else:
                print(px, py)
                print(px * _max + py)
                return
            px += 1
        py += 1


if __name__ == "__main__":
    input_file_path = os.path.join(current_dir, "input")
    # input_file_path = os.path.join(current_dir, "input.test")
    _input = open(input_file_path, "r").read()
    input_lines = _input.split("\n")

    main(input_lines)
