
num_increased = 0
prev_sum = 0

window = [None, None, None]
with open('day1.input', 'r') as fh:
    line = fh.readline()
    while line:
        if all(window):
            if sum(window) > prev_sum:
                num_increased += 1
            prev_sum = sum(window)
        window[0] = window[1]
        window[1] = window[2]
        window[2] = int(line)
        line = fh.readline()
print(num_increased)