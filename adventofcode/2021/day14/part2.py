import copy
from collections import defaultdict

input_rules = {}

if __name__ == "__main__":
    with open("input", "r") as fh:
        line = fh.readline()
        while line:
            sequence, insertion_val = line.strip("\n").split("->")
            input_rules.update({sequence.strip(): insertion_val.strip()})
            line = fh.readline()

    template = "PFVKOBSHPSPOOOCOOHBP"  # "NNCB"

    # Initialize sequence_count_map
    sequence_count_map = defaultdict(int)
    for i, char in enumerate(template[:-1]):
        seq = f"{char}{template[i+1]}"
        sequence_count_map[seq] += 1

    # Now apply rules
    for _ in range(40):
        new_sequence_count_map = copy.deepcopy(sequence_count_map)
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
        char_count_map[seq[-1]] += count

    # filter count
    final_char_count_map = defaultdict(int)
    for char, count in char_count_map.items():
        if char == template[0]:
            final_char_count_map[char] += 1
            count -= 1
        if char == template[-1]:
            final_char_count_map[char] += 1
            count -= 1
        final_char_count_map[char] += count // 2

    # Print!!
    max_count = 0
    min_count = 218818969352921881896935292188189693529
    for char, count in final_char_count_map.items():
        if count > max_count:
            max_count = count

        if count < min_count:
            min_count = count

    print(f"{max_count} - {min_count} = {max_count - min_count}")
