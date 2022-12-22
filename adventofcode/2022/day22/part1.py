import argparse
import os
import re

current_dir = os.path.dirname(os.path.abspath(__file__))

pattern = r"\d+[A-Za-z]"

TURN_MAP = {
    "L": {"L": "D", "R": "U"},
    "R": {"R": "D", "L": "U"},
    "U": {"L": "L", "R": "R"},
    "D": {"L": "R", "R": "L"},
}


def get_next(p, d, lines):
    p1, p2 = p[0], p[1]

    elem = None
    while elem not in [".", "#"]:
        s = lines[p1]
        if d == "D":
            p1 = p1 + 1 if 0 <= p1 + 1 < len(lines) else 0
        elif d == "U":
            p1 = p1 - 1 if 0 <= p1 - 1 < len(lines) else len(lines) - 1
        elif d == "R":
            p2 = p2 + 1 if 0 <= p2 + 1 < len(s) else 0
        elif d == "L":
            p2 = p2 - 1 if 0 <= p2 - 1 < len(s) else len(s) - 1

        s2 = lines[p1]
        try:
            elem = s2[p2]
            if elem == " ":
                continue
            return elem, p1, p2
        except Exception:
            continue


def main(input_lines):
    ins_line = input_lines[-1]
    lines = input_lines[:-2]

    # Find instructions
    ins = []
    matches = re.findall(pattern, ins_line)
    for match in matches:
        digit, letter = match[:-1], match[-1].strip()
        ins.append((int(digit), letter))

    d = "R"
    p = (0, 0)
    e, *p = get_next(p, d, lines)

    # start the iteration
    for steps, next_d in ins:
        for _ in range(steps):
            e, *np = get_next(p, d, lines)
            if e == "#":
                d = TURN_MAP[d][next_d]
                break
            else:
                p = np
        else:
            d = TURN_MAP[d][next_d]

    # This is for the last number in the instruction
    for _ in range(11):
        e, p1, p2 = get_next(p, d, lines)
        if e == "#":
            break
        p = [p1, p2]

    # Print the result
    res = 1000 * (p[0] + 1) + 4 * (p[1] + 1) + "RDLU".index(d)
    print(res)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()

    test = False
    if args.test:
        test = True

    input_file_path = (
        os.path.join(current_dir, "input.test")
        if test
        else os.path.join(current_dir, "input")
    )
    _input = open(input_file_path, "r").read()
    input_lines = _input.split("\n")
    main(input_lines)
