import os
import re
pattern = re.compile(r"(\d+)-(\d+) (\w):.*?(\w+)")

TREE = '#'
NONTREE = '.'


def read_from_file(filename):
    file_path = os.path.join(
        os.path.dirname(__file__), filename)
    results = []
    with open(file_path) as fh:
        rows = fh.read().split('\n')
        for r in rows:
            results.append(list(r))
    return results


def find_trees_count(map_data, horizontal, vertical):
    trees_count = 0
    x_coord, y_coord = 0, 0
    while True:
        x_coord = (x_coord + horizontal) % len(map_data[0])
        y_coord = y_coord + vertical
        if y_coord >= len(map_data):
            break
        val = map_data[y_coord][x_coord]
        if val == TREE:
            trees_count += 1
    return trees_count


def main():
    map_data = read_from_file("input.txt")
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    prod = 1
    for x, y in slopes:
        prod *= find_trees_count(map_data, x, y)
    print(prod)


if __name__ == "__main__":
    main()
    
 # ###### 2, 2+7    - 
