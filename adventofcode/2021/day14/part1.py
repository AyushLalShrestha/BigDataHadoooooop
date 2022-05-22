from collections import defaultdict


input_rules = {}

if __name__ == "__main__":
    with open("input", "r") as fh:
        line = fh.readline()
        while line:
            sequence, insertion_val = line.strip("\n").split("->")
            input_rules.update({sequence.strip(): insertion_val.strip()})
            line = fh.readline()

    # template = "NNCB"
    template = "PFVKOBSHPSPOOOCOOHBP"
    for _ in range(10):
        new_template = ""
        
        for i, char in enumerate(template[:-1]):
            seq = f"{char}{template[i+1]}"
            new_template += char
            if seq in input_rules:
                new_template += input_rules[seq]
        new_template += template[-1]
        template = new_template
    # print(template)
    
    char_to_count = defaultdict(int)
    for char in template:
        char_to_count[char] += 1
    
    max_count = 0
    min_count = 212312321231232123123
    for char, count in char_to_count.items():
        if count > max_count:
            max_count = count
        if count < min_count:
            min_count = count
    print(f"V Count's = {char_to_count['V']}, {char_to_count['V']}")
    print(f"P Count's = {char_to_count['P']}, {char_to_count['P']}")
    print(f"{max_count} - {min_count} = {max_count - min_count}")
        