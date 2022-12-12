import os

current_dir = os.path.dirname(os.path.abspath(__file__))

def get_next_possible_points(x, y, grid, traversed):
    """Return valid neighbouring points if not already in traversed"""
    val = grid[x][y]
    next_points = []
    points = [
        [x - 1, y],
        [x + 1, y],
        [x, y - 1],
        [x, y + 1],
    ]
    for i, j in points:
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
            next_val = grid[i][j]

            if val == "S":
                val = "a"
            if next_val == "S":
                continue
            elif next_val == "E":
                if val == "z" or val == "y":
                    next_points.append([i, j])
            else:
                if ord(next_val) - ord(val) <= 1 and [i, j] not in traversed:
                    next_points.append([i, j])
    return next_points


def main(input_lines):
    grid = []
    start_positions = []
    end = None

    # Parse the input, form a grid. Note the starting points.
    for i, row in enumerate(input_lines):
        grid_row = []
        row = row.strip()
        for j, elem in enumerate(row):
            if elem == "S":
                start_positions.append([i, j])
            if elem == "a":
                start_positions.append([i, j])
            if elem == "E":
                end = [i, j]
            grid_row.append(elem)
        grid.append(grid_row)

    # paths that led to the destination
    paths = []

    # For each "a", start the traversal, find the paths that lead to destination
    for start in start_positions:
        possible_paths = [[start,],]
        traversed = [start,]
        while possible_paths:
            next_possible_paths = []
            for possible_path in possible_paths:
                last_point = possible_path[-1]
                next_points = get_next_possible_points(
                    last_point[0],
                    last_point[1],
                    grid,
                    possible_path
                )
                for next_point in next_points:
                    if next_point in traversed:
                        continue
                    next_possible_path = possible_path + [next_point,]
                    if next_point == end:
                        paths.append(next_possible_path)
                    else:
                        next_possible_paths.append(next_possible_path)
                        traversed.append(next_point)
            possible_paths = next_possible_paths

    # Print the path with minimum hops
    print(min([len(p) - 1 for p in paths]))


if __name__ == "__main__":
    # input_file_path = os.path.join(current_dir, "input.test")
    input_file_path = os.path.join(current_dir, "input")
    _input = open(input_file_path, "r").read()
    input_lines = _input.split("\n")

    main(input_lines)
