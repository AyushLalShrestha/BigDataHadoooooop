import os
import json

current_dir = os.path.dirname(os.path.abspath(__file__))

def compare_lists(l1, l2):
    """compares list l1 with list l2"""
    itr = min([len(l1), len(l2)])
    for i in range(itr):
        v1 = l1[i]
        v2 = l2[i]
        c = compare(v1, v2)
        if c is None:
            continue
        return c

    if len(l1) == len(l2):
        return None
    return len(l1) < len(l2)


def compare(v1, v2):
    """Compares the values v1 and v2

    Returns:
        bool, None: True if v1 & v2 are in order,
            False if v1 & v2 are not in order,
            None if order cannot be determined
    """
    if isinstance(v1, int) and isinstance(v2, int):
        # if both the values are int
        if v1 == v2:
            return None
        return v1 < v2
    elif isinstance(v1, list) and isinstance(v2, list):
        # compare lists
        return compare_lists(v1, v2)
    else:
        # if one is int and another is list
        if isinstance(v1, int):
            v1 = [v1, ]
        elif isinstance(v2, int):
            v2 = [v2, ]
        return compare_lists(v1, v2)

def main(pairs):
    right_ordered = []
    for i, pair in enumerate(pairs, 1):
        p1, p2 = pair.split("\n")
        p1 = json.loads(p1)
        p2 = json.loads(p2)
        c = compare(p1, p2)
        if c is True:
            right_ordered.append(i)
    print(sum(right_ordered))


if __name__ == "__main__":
    input_file_path = os.path.join(current_dir, "input")
    # input_file_path = os.path.join(current_dir, "input.test")
    _input = open(input_file_path, "r").read()
    pairs = _input.split("\n\n")

    main(pairs)
