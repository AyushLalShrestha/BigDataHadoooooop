
import argparse
from copy import deepcopy
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

history = {}
valves = {}


def find_max(current_node, flowing, minutes):
    """
    From multiple alternatives of what to do next, choose the one that is the most rewarding!

    Args:
        path (List[str]): The path so far
        flowing (set[str]): Valves that are aleady opened
        minutes (int): The minute we are currently at

    Returns:
        int: Best alternative that gets the best value
    """
    # Check Cache
    minutes_data = history.get(minutes, {})
    if minutes_data.get(current_node):
        current_node_data = minutes_data[current_node]
        for f, t in current_node_data:
            if f == flowing:
                return t

    neighbours = valves[current_node][0]
    rate = valves[current_node][1]
    total = sum([valves[name][1] for name in flowing])

    # If last minute
    if minutes == 29:
        return total

    candidates = []

    # Possibility 1
    if rate > 0 and current_node not in flowing:
        flowing2 = deepcopy(flowing)
        flowing2.add(current_node)
        max_output = find_max(current_node, flowing2, minutes + 1)
        candidates.append(max_output)

    # Possibility 2
    for neighbour in neighbours:
        flowing2 = deepcopy(flowing)
        max_output = find_max(neighbour, flowing2, minutes + 1)
        candidates.append(max_output)

    # Cache it
    minutes_data = history.get(minutes, {})
    current_node_data = minutes_data.get(current_node, [])
    current_node_data.append((flowing, total + max(candidates)))
    minutes_data[current_node] = current_node_data
    history[minutes] = minutes_data

    return total + max(candidates) if candidates else total


def main(input_lines, start):
    global valves

    # Parse the input
    for line in input_lines:
        name = line.split("Valve ")[1].split(" ")[0]
        rate = int(line.split("rate=")[1].split(";")[0])
        try:
            leads_to = line.split("lead to valves ")[1].split(",")
            leads_to = tuple([l.strip() for l in leads_to])
        except:
            leads_to = tuple([line.split("leads to valve ")[1].strip()])

        valves[name] = (leads_to, rate)

    # Find the path (possibility) with maximum output
    flowing = set()
    _max = find_max(start, flowing, 0)
    print(_max)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()

    test = False
    if args.test:
        test = True

    input_file_path = os.path.join(current_dir, "input.test") if test else os.path.join(current_dir, "input")
    _input = open(input_file_path, "r").read()
    input_lines = _input.split("\n")

    start = "AA" if test else "BT"
    main(input_lines, start)
