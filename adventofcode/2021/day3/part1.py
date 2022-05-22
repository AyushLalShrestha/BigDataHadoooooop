

track = None

with open('day3.input', 'r') as fh:
    power_value = fh.readline()
    track = [[0, 0] for _ in power_value]
    while power_value:
        # values = power_value.split()
        for i, v in enumerate(power_value):
            if not v.isdigit():
                continue
            if int(v) == 0:
                track[i][0] += 1
            elif int(v) == 1:
                track[i][1] += 1
        power_value = fh.readline()

gamma = ""
epsilon = ""

for i, v in track:
    if i > v:
        gamma += "0"
        epsilon += "1"
    elif i < v:
        gamma += "1"
        epsilon += "0"

print(gamma)
print(epsilon)