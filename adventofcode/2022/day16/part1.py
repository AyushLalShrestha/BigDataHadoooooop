
from functools import lru_cache
import argparse
import os
from copy import deepcopy

current_dir = os.path.dirname(os.path.abspath(__file__))

valves = {}

@lru_cache
def find_max(current_node, flowing, minutes):
    """
    From multiple alternatives of what to do next, choose the one that is the most rewarding!

    Args:
        current_node (str): The current valve we are at
        flowing (tuple[str]): Valves that are aleady opened
        minutes (int): The minute we are currently at

    Returns:
        int: Best value from all the alternatives
    """
    neighbours = valves[current_node][0]
    rate = valves[current_node][1]
    total = sum([valves[name][1] for name in flowing])

    # If last minute
    if minutes == 29:
        return total

    candidates = []

    # Possibility 1
    if rate > 0 and current_node not in flowing:
        flowing2 = flowing + tuple([current_node,])
        flowing2 = tuple(sorted(flowing2))
        max_output = find_max(current_node, flowing2, minutes + 1)
        candidates.append(max_output)

    # Possibility 2
    for neighbour in neighbours:
        max_output = find_max(neighbour, flowing, minutes + 1)
        candidates.append(max_output)

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
    flowing = tuple()
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
