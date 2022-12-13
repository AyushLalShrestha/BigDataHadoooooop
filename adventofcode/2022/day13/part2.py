from functools import cmp_to_key
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
        # if both the values are integer
        if v1 == v2:
            return None
        return v1 < v2
    elif isinstance(v1, list) and isinstance(v2, list):
        # compare lists
        return compare_lists(v1, v2)
    else:
        # if one is int & another is list
        if isinstance(v1, int):
            v1 = [v1, ]
        elif isinstance(v2, int):
            v2 = [v2, ]
        return compare_lists(v1, v2)


def compare_l(l1, l2):
    return 1 if compare(l1, l2) is True else -1

def main(lst):
    lst.sort(key=cmp_to_key(lambda x, y: compare_l(x, y)))
    i1 = i2 = 0
    for idx, elem in enumerate(lst[::-1], 1):
        if elem == [[2]]:
            i1 = idx
        elif elem == [[6]]:
            i2 = idx
    print(i1 * i2)


if __name__ == "__main__":
    input_file_path = os.path.join(current_dir, "input2")
    # input_file_path = os.path.join(current_dir, "input2.test")
    _input = open(input_file_path, "r").read()
    _input = _input.replace("\n\n", "\n")
    lst = _input.split("\n")
    lst = [json.loads(line) for line in lst]

    main(lst)
