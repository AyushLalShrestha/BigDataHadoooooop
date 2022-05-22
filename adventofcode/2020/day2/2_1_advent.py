import os
import re
pattern = re.compile(r"(\d+)-(\d+) (\w):.*?(\w+)")

def read_from_file(filename):
    file_path = os.path.join(
        os.path.dirname(__file__), filename)
    with open(file_path) as fh:
        results = fh.read().split('\n')
    return results

def main():
    result = read_from_file("input.txt")
    valid = 0
    for row in result:
        res = pattern.match(row)
        min_occ = int(res.group(1))
        max_occ = int(res.group(2))
        character = res.group(3)
        word = res.group(4)
        count = word.count(character)
        if (word[min_occ-1] == character) ^ (word[max_occ-1] == character):
            # if min_occ <= count <= max_occ:
            valid += 1
    print(valid)


if __name__ == "__main__":
    main()