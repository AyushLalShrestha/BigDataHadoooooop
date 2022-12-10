import os

current_dir = os.path.dirname(os.path.abspath(__file__))


def main():
    input_file_path = os.path.join(current_dir, "input")
    _input = open(input_file_path, "r").read()
    input_lines = _input.split("\n")

    x = 1
    cycle = 1
    total = 0
    next_cycle = 20

    for line in input_lines:
        ins = line.strip().split(" ")

        if ins[0] == "noop":
            cycle += 1
            if cycle == next_cycle:
                total += x * cycle
                next_cycle += 40

        elif ins[0] == "addx":
            val = int(ins[1])

            # 1st part of addx
            cycle += 1
            if cycle == next_cycle:
                total += x * cycle
                next_cycle += 40

            # 2nd part of addx
            cycle += 1
            x += val
            if cycle == next_cycle:
                total += x * cycle
                next_cycle += 40

    print(total)


if __name__ == "__main__":
    main()
