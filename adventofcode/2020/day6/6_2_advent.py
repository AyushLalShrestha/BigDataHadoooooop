import os


def read_from_file(filename):
    file_path = os.path.join(
        os.path.dirname(__file__), filename)

    with open(file_path) as fh:
        empty_count = 0
        rows = []
        row = []
        while True:
            line = fh.readline().strip()
            if not line:
                empty_count += 1
                if empty_count > 1:
                    break
                rows.append(row)
                row = []
            else:
                row.append(line)
                empty_count = 0

    return rows


def main():
    map_data = read_from_file("input.txt")
    count = 0
    for group_data in map_data:
        if len(group_data) == 1:
            count += len(group_data[0])
            continue

        common = set(group_data[0])
        for data in group_data:
            common = common.intersection(set(data))
        count += len(common)
    print(count)


if __name__ == "__main__":
    main()

