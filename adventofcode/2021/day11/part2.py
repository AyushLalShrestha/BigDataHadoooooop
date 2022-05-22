class GridMap(object):
    def __init__(self, input):
        self.rows = len(input)
        self.columns = len(input[0])
        self.map = input

    def find_adjacent_points(self, x, y):
        adjacents = [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1),
            (x + 1, y + 1),
            (x + 1, y - 1),
            (x - 1, y + 1),
            (x - 1, y - 1),
        ]
        valid_adjacents = []
        for adj_x, adj_y in adjacents:
            if not (0 <= adj_x < self.rows):
                continue
            if not (0 <= adj_y < self.columns):
                continue
            valid_adjacents.append((adj_x, adj_y))
        return valid_adjacents

    def increase_a_point(self, x, y):
        val = self.map[x][y]

        if (x, y) in self.flashed:
            # Already checked & increased adjacents for this point
            return

        if val < 10:
            # increase the value of the point
            self.map[x][y] = val + 1

        # If the value is now 10, increase adjacents
        if self.map[x][y] == 10:
            self.flashed.append((x, y))
            adjacent_points = self.find_adjacent_points(x, y)
            for adj_x, adj_y in adjacent_points:
                self.increase_a_point(adj_x, adj_y)

    def move_a_step(self,):
        # Increase all co-ords values by one and check flashes
        self.flashed = []
        for i, row in enumerate(self.map):
            for j, val in enumerate(row):
                self.map[i][j] = val + 1

        for i, row in enumerate(self.map):
            for j, val in enumerate(row):
                if val > 9 and (i, j) not in self.flashed:
                    self.increase_a_point(i, j)

        for i, row in enumerate(self.map):
            for j, column in enumerate(row):
                if column > 9:
                    self.map[i][j] = 0
                    # flashes += 1
        flash_num = len(self.flashed)
        self.flashed = []
        return flash_num


if __name__ == "__main__":
    rows = []
    with open("input", "r") as fh:
        line = fh.readline()
        while line:
            data = line.strip("\n")
            row = list([int(i) for i in data])
            rows.append(row)
            line = fh.readline()
    gridMap = GridMap(rows)

    total_flashes = 0
    step = 1
    while True:
        flashes = gridMap.move_a_step()
        total_flashes += flashes
        if flashes == gridMap.rows * gridMap.columns:
            print(step)
            break
        if step == 100:
            print(total_flashes)
        step += 1

