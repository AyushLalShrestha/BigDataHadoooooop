import math


class GridMap(object):
    def __init__(self, input):
        self.rows = len(input)
        self.columns = len(input[0])
        self.map = input
        self.dijkstra_map = []
        for _ in range(self.rows):
            self.dijkstra_map.append([math.inf] * self.columns)
        self.dijkstra_map[0][0] = 0

    def get_adjacent_points(self, x, y):
        adjacents = [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1)
            # (x + 1, y + 1), (x + 1, y - 1), (x - 1, y + 1), (x - 1, y - 1),
        ]
        valid_adjacents = []
        for adj_x, adj_y in adjacents:
            if not (0 <= adj_x < self.rows):
                continue
            if not (0 <= adj_y < self.columns):
                continue
            valid_adjacents.append((adj_x, adj_y))
        return valid_adjacents

    def get_shortest_adjacent(self, adjacents):
        shortest = adjacents[0]
        for adj_x, adj_y in adjacents:
            if (
                self.dijkstra_map[adj_x][adj_y]
                < self.dijkstra_map[shortest[0]][shortest[1]]
            ):
                shortest = (adj_x, adj_y)
        return shortest

    def run_dijkstra(self,):
        visited = set()
        next_to_visit = set()
        next_to_visit.add((0, 0))

        while next_to_visit:
            point = self.get_shortest_adjacent(list(next_to_visit))
            next_to_visit.remove(point)
            if point in visited:
                continue
            visited.add(point)
            current_distance = self.dijkstra_map[point[0]][point[1]]
            adjacents = self.get_adjacent_points(*point)
            for adj in adjacents:
                hop_distance = self.map[adj[0]][adj[1]]
                net_distance = self.dijkstra_map[adj[0]][adj[1]]
                # if point == (0, 0):
                #     print(adj, hop_distance, current_distance, net_distance)
                if hop_distance + current_distance < net_distance:
                    self.dijkstra_map[adj[0]][adj[1]] = hop_distance + current_distance
                next_to_visit.add(adj)


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
    
    gridMap.run_dijkstra()
    print(gridMap.dijkstra_map[-1][-1])
    # print(len(gridMap.sptSet))

