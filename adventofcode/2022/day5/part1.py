import os
from collections import defaultdict
import pprint

current_dir = os.path.dirname(os.path.abspath(__file__))


def main():
    input_file_path = os.path.join(current_dir, "input")
    _input = open(input_file_path, "r").read()
    input_lines = _input.split("\n")

    input_file_path = os.path.join(current_dir, "input-ins")
    _input = open(input_file_path, "r").read()
    input_ins_lines = _input.split("\n")

    # Parse input stack
    stacks = defaultdict(list)
    for line in input_lines[::-1]:
        i = 0
        while i < len(line):
            _next = line[i:i + 4]
            if _next.strip() == "":
                pass
            else:
                _next = _next.strip().lstrip("[").rstrip("]")
                if _next:
                    stacks[(i // 4) + 1].append(_next)
            i += 4

    # Parse intructions
    instructions = []
    for line in input_ins_lines:
        line = line.split()
        instructions.append([int(line[1]), int(line[3]), int(line[5])])

    # make the moves
    for moves, _from, _to in instructions:
        for i in range(moves):
            val = stacks[_from].pop()
            stacks[_to].append(val)

    # output
    output = ""
    for i, v in stacks.items():
        output += v[-1]
    print(output)

if __name__ == "__main__":
    main()
