import os

current_dir = os.path.dirname(os.path.abspath(__file__))


def main():
    input_file_path = os.path.join(current_dir, "input")
    _input = open(input_file_path, "r").read()
    lines = _input.split("\n")

    total = 0
    for line in lines:
        parts = line.strip().split(",")
        first_part = parts[0]
        second_part = parts[1]
        a1 = int(first_part.split("-")[0])
        a2 = int(first_part.split("-")[1])
        b1 = int(second_part.split("-")[0])
        b2 = int(second_part.split("-")[1])

        if a1 <= b1 <= a2 or a1 <= b2 <= a2:
            total += 1
        elif b1 <= a1 <= b2 or b1 <= a2 <= b2:
            total += 1

    print(total)


if __name__ == "__main__":
    main()
