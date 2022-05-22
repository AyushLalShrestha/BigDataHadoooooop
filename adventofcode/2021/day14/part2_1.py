
import copy
from collections import defaultdict
from string import ascii_uppercase

input_rules = {}

if __name__ == "__main__":
    with open("input", "r") as fh:
        line = fh.readline()
        while line:
            sequence, insertion_val = line.strip("\n").split("->")
            input_rules.update({sequence.strip(): insertion_val.strip()})
            line = fh.readline()
    # print(input_rules)

    # template = "NNCB"
    template = "PFVKOBSHPSPOOOCOOHBP"

    # Initialize sequence_count_map
    sequence_count_map = defaultdict(int)
    for char in ascii_uppercase:
        for seq_char in ascii_uppercase:
            sequence = f"{char}{seq_char}"
            if sequence in template:
                sequence_count_map[f"{char}{seq_char}"] += 1

    # debug
    print("Initial input count: ", sequence_count_map, "\n")

    # Now apply rules
    for _ in range(10):
        new_sequence_count_map = copy.deepcopy(sequence_count_map)
        # print("\n", dict(sequence_count_map))
        for sequence, count in sequence_count_map.items():
            if sequence in input_rules:
                insertion_val = input_rules[sequence]
                seq1 = f"{sequence[0]}{insertion_val}"
                seq2 = f"{insertion_val}{sequence[1]}"
                new_sequence_count_map[seq1] += count
                new_sequence_count_map[seq2] += count
                if new_sequence_count_map[sequence] > 0:
                    new_sequence_count_map[sequence] -= count
        sequence_count_map = copy.deepcopy(new_sequence_count_map)

    # count!!
    char_count_map = defaultdict(int)
    for seq, count in sequence_count_map.items():
        char_count_map[seq[0]] += count
        char_count_map[seq[1]] += count

    new_char_count_map = defaultdict(int)
    for char, count in char_count_map.items():
        if char == template[0]:
            new_char_count_map[char] += 1
            count -= 1
        if char == template[-1]:
            new_char_count_map[char] += 1
            count -= 1
        if count % 2 == 1:
            count += 1
        count = count//2
            
        new_char_count_map[char] += count

    # Print!!
    max_count = 0
    min_count = 218818969352921881896935292188189693529
    for char, count in new_char_count_map.items():
        if count > max_count:
            max_count = count
        if count < min_count:
            min_count = count
    print(max_count - min_count)