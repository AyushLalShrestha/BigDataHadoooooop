
num_increased = 0
prev_num = None
with open('part1.input', 'r') as fh:
    line = fh.readline()
    prev_num = int(line)
    while line:
        # if line and line.isnumeric():
        if prev_num < int(line):
            num_increased += 1
        prev_num = int(line)
        line = fh.readline()
print(num_increased)