

ALL_BASIN_POINTS = set()

def find_higher_adjacents(x, y, positions):
    total_rows = len(positions)
    total_columns = len(positions[0])
    higher_adjacents = []
    element = positions[x][y]
    possible_adjacents = 0

    up_x, up_y = x-1, y
    if 0 <= up_x < total_rows:
        possible_adjacents += 1
        val = positions[up_x][up_y]
        if val >= element:
            higher_adjacents.append((up_x, up_y))

    down_x, down_y = x+1, y
    if 0 <= down_x < total_rows:
        possible_adjacents += 1
        val = positions[down_x][down_y]
        if val > element:
            higher_adjacents.append((down_x, down_y))

    left_x, left_y = x, y-1
    if 0 <= left_y < total_columns:
        possible_adjacents += 1
        val = positions[left_x][left_y]
        if val > element:
            higher_adjacents.append((left_x, left_y))

    right_x, right_y = x, y+1
    if 0 <= right_y < total_columns:
        possible_adjacents += 1
        val = positions[right_x][right_y]
        if val > element:
            higher_adjacents.append((right_x, right_y))

    return possible_adjacents, higher_adjacents


def find_all_higher_adjacents(x, y, positions):
    count = 1
    ALL_BASIN_POINTS.add((x, y))
    _, higher_adjacents = find_higher_adjacents(x, y, positions)
    for adjacent in higher_adjacents:
        if positions[adjacent[0]][adjacent[1]] == 9:
            continue
        if adjacent in ALL_BASIN_POINTS:
            continue
        count += find_all_higher_adjacents(*adjacent, positions)
    return count


if __name__ == "__main__":
    positions = []
    with open("input", "r") as fh:
        line = fh.readline()
        while line:
            data = line.strip("\n")
            data = tuple([int(i) for i in data])
            positions.append(data)
            line = fh.readline()
    low_points = []
    for x, row in enumerate(positions):
        for y, element in enumerate(row):
            possible_adjacents, higher_adjacents = find_higher_adjacents(x, y, positions)
            if len(higher_adjacents) == possible_adjacents:
                low_points.append((x, y))

    # print(low_points)
    one = 0
    two = 0
    three = 0
    for low_point in low_points:
        count = 0
        count += find_all_higher_adjacents(*low_point, positions)
        if count > one:
            three = two
            two = one
            one = count
        elif count > two:
            three = two
            two = count
        elif count > three:
            three = count
    print(one, two, three, one*two*three)

