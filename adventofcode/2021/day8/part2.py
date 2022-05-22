from itertools import permutations
from collections import defaultdict

unique_len_to_number = {2: 1, 4: 4, 3: 7, 7: 8}
"""
 0000
1    2
1    2
 3333
4    5
4    5
 6666

"""
number_to_positions = {
    1: {2, 5},
    2: {0, 2, 3, 4, 6},
    3: {0, 2, 3, 5, 6},
    4: {1, 2, 3, 5},
    5: {0, 1, 3, 5, 6},
    6: {0, 1, 3, 4, 5, 6},
    7: {0, 2, 5},
    8: {0, 1, 2, 3, 4, 5, 6},
    9: {0, 1, 2, 3, 5, 6},
}


def satisfies_permutation(p, number_to_perm):
    if p == "deafgbc":
        print(p)
        print(number_to_perm)
    for number, perms in number_to_perm.items():
        for perm in perms:
            num_positions = number_to_positions[number]
            positions = {p.index(c) for c in perm}
            if p == "deafgbc":
                print(number, num_positions, positions)
            if num_positions != positions:
                return False
    return True


def find_code_to_number(inp, out):
    code_to_number = {}
    all_vars = inp + out
    number_to_perm = defaultdict(list)
    for var in all_vars:
        length = len(var)
        sorted_var = "".join(sorted(var))
        if length in unique_len_to_number:
            number = unique_len_to_number[length]
            number_to_perm[number].append(sorted_var)
        elif length == 5:
            # possibly 2 5
            # if has letter from 4, it's 2
            number_to_perm[2].append(sorted_var)
            number_to_perm[5].append(sorted_var)
        elif length == 6:
            # possibly 0, 9 or 6
            number_to_perm[0].append(sorted_var)
            number_to_perm[6].append(sorted_var)
            number_to_perm[9].append(sorted_var)

    for perm in permutations("abcdefg"):
        p = "".join(perm)
        success = satisfies_permutation(p, number_to_perm)
        if success:
            print(p)


def main():
    with open("input.test", "r") as fh:
        line = fh.readline()
        while line:
            data = line.strip("\n").split("|")
            input_vals = data[0]
            input_vals = input_vals.strip().split(" ")
            output_vals = data[1]
            output_vals = output_vals.strip().split(" ")
            find_code_to_number(input_vals, output_vals)

            line = fh.readline()


if __name__ == "__main__":
    main()
