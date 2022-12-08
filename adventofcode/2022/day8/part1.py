import os

current_dir = os.path.dirname(os.path.abspath(__file__))


def main():
    input_file_path = os.path.join(current_dir, "input.test")
    # input_file_path = os.path.join(current_dir, "input")
    _input = open(input_file_path, "r").read()
    rows = _input.split("\n")

    total_visible = 0
    for i, row in enumerate(rows):
        for j, elem in enumerate(row):
            if i == 0 or i == len(rows) - 1 or j == 0 or j == len(rows[0]) - 1:
                total_visible += 1
                continue

            # Up
            if 0 <= i - 1 < len(rows):
                val = rows[i - 1][j]
                if val < elem:
                    points_to_edge = [r[j] for r in rows[:i]][::-1]
                    if all([p < elem for p in points_to_edge]):
                        total_visible += 1
                        continue

            # Down
            if 0 <= i + 1 < len(rows):
                val = rows[i + 1][j]
                if val < elem:
                    points_to_edge = [r[j] for r in rows[i + 1 :]]
                    if all([p < elem for p in points_to_edge]):
                        total_visible += 1
                        continue

            # left
            if 0 <= j - 1 < len(rows[0]):
                val = row[j - 1]
                if val < elem:
                    points_to_edge = row[:j][::-1]
                    if all([p < elem for p in points_to_edge]):
                        total_visible += 1
                        continue

            # right
            if 0 <= j + 1 < len(rows[0]):
                val = row[j + 1]
                if val < elem:
                    points_to_edge = row[j + 1 :]
                    if all([p < elem for p in points_to_edge]):
                        total_visible += 1
                        continue

    print(total_visible)


if __name__ == "__main__":
    main()
