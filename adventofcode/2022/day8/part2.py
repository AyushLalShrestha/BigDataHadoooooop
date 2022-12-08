import math
import os

current_dir = os.path.dirname(os.path.abspath(__file__))


def main():
    input_file_path = os.path.join(current_dir, "input.test")
    input_file_path = os.path.join(current_dir, "input")
    _input = open(input_file_path, "r").read()
    rows = _input.split("\n")

    max_scenic_score = 0
    for i, row in enumerate(rows):
        for j, elem in enumerate(row):
            if i == 0 or i == len(rows) - 1 or j == 0 or j == len(rows[0]) - 1:
                continue

            scenic_score_up = (
                scenic_score_down
            ) = scenic_score_left = scenic_score_right = 0

            # Up
            if 0 <= i - 1 < len(rows):
                points_to_edge = [r[j] for r in rows[:i]][::-1]
                for p in points_to_edge:
                    scenic_score_up += 1
                    if p >= elem:
                        break

            # Down
            if 0 <= i + 1 < len(rows):
                points_to_edge = [r[j] for r in rows[i + 1 :]]
                for p in points_to_edge:
                    scenic_score_down += 1
                    if p >= elem:
                        break

            # left
            if 0 <= j - 1 < len(rows[0]):
                points_to_edge = row[:j][::-1]
                for p in points_to_edge:
                    scenic_score_left += 1
                    if p >= elem:
                        break

            # right
            if 0 <= j + 1 < len(rows[0]):
                points_to_edge = row[j + 1 :]
                for p in points_to_edge:
                    scenic_score_right += 1
                    if p >= elem:
                        break

            scenic_score = math.prod(
                [
                    scenic_score_up,
                    scenic_score_down,
                    scenic_score_left,
                    scenic_score_right,
                ]
            )
            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score
    print(max_scenic_score)


if __name__ == "__main__":
    main()
