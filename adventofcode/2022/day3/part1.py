import os

current_dir = os.path.dirname(os.path.abspath(__file__))

alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
    badges = []

    input_file_path = os.path.join(current_dir, "input")
    with open(input_file_path, "r") as fh:
        line = fh.readline()
        while line:
            line = line.strip()
            line_len = len(line)
            first = line[0: line_len // 2]
            second = line[line_len // 2:]

            for ch in first:
                if ch in second:
                    badges.append(ch)
                    break

            line = fh.readline()

    print(sum([alphabets.index(ch) + 1 for ch in badges]))


if __name__ == "__main__":
    main()
