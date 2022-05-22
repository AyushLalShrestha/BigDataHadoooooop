
from collections import defaultdict
import time

class Path(object):
    def __init__(self, traversed,):
        self.traversed = traversed

    def __str__(self):
        return str(self.traversed)

    def hop_already_hopped(self, source, destination):
        return f"{source}{destination}" in "".join(self.traversed)

class CaveMap(object):
    def __init__(self,):
        self.adjacent_map = defaultdict(set)

    def add_adjacent(self, point_a, point_b):
        self.adjacent_map[point_a].add(point_b)
        self.adjacent_map[point_b].add(point_a)
        

def get_next_destinations(path, caveMap):
    source = path.traversed[-1]
    possible_detinations = caveMap.adjacent_map[source]
    destinations = []
    for destination in possible_detinations:
        if destinations == "start":
            continue
        if destination.islower() and destination in path.traversed:
            continue
        if path.hop_already_hopped(path.traversed[-1], destination):
            continue
        destinations.append(destination)
    return destinations


if __name__ == "__main__":
    caveMap = CaveMap()
    rows = []
    with open("input", "r") as fh:
        line = fh.readline()
        while line:
            data = line.strip("\n")
            point_a, point_b = data.split("-")
            caveMap.add_adjacent(point_a, point_b)
            line = fh.readline()

    final_paths = []
    all_paths = [Path(["start"])]

    step = 1
    while all_paths:
        print(f"Step: {step} - - - - - ")
        step += 1
        new_all_paths = []
        for path in all_paths:
            if path.traversed[-1] == "end":
                final_paths.append(path)
                continue
            next_dests = get_next_destinations(path, caveMap)
            for dest in next_dests:
                new_path = Path(path.traversed + [dest,])
                print(new_path.traversed)
                new_all_paths.append(new_path)
        print("- - - - - - - - - - ")
        all_paths = new_all_paths
        # time.sleep(2)
    print(len(final_paths))
