
import os
current_dir = os.path.dirname(os.path.abspath(__file__))


def main():
    input_file_path = os.path.join(current_dir, "input")
    _input = open(input_file_path, "r").read()
    input_lines = _input.split("\n")

    cycle = 0
    x = 1
    sprite_position = 1
    output = []

    for line in input_lines:
        ins = line.strip().split(" ")

        if ins[0] == "noop":
            if cycle % 40 in [sprite_position - 1, sprite_position, sprite_position + 1]:
                output.append("#")
            else:
                output.append(".")
            cycle += 1

        elif ins[0] == "addx":
            val = int(ins[1])

            # 1st part of addx
            if cycle % 40 in [sprite_position - 1, sprite_position, sprite_position + 1]:
                output.append("#")
            else:
                output.append(".")
            cycle += 1

            # 2nd part of addx
            if cycle % 40 in [sprite_position - 1, sprite_position, sprite_position + 1]:
                output.append("#")
            else:
                output.append(".")

            cycle += 1
            x += val
            sprite_position = x

    # Print Output
    stream = ""
    for i, c in enumerate(output):
        if i > 0 and i % 40 == 0:
            print(stream)
            stream = ""
        stream += f"{c}{c}{c}"
    print(stream)

if __name__ == "__main__":
    main()
