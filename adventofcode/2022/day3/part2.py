import os

current_dir = os.path.dirname(os.path.abspath(__file__))
alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():
    badges = []

    input_file_path = os.path.join(current_dir, "input")
    with open(input_file_path, "r") as fh:
        line = fh.readline()
        count = 0
        batch = []

        while line:
            line = line.strip()
            batch.append(line)

            if count == 2:
                for ch in batch[0]:
                    if ch in batch[1] and ch in batch[2]:
                        badges.append(ch)
                        break
                batch = []
                count = 0
            else:
                count += 1
            line = fh.readline()

    print(sum([alphabets.index(ch) + 1 for ch in badges]))


if __name__ == "__main__":
    main()
