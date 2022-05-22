
x = 0
y = 0
aim = 0
with open('day2.input', 'r') as fh:
    command = fh.readline()
    while command:
        direction, magnitude = command.split(' ')
        # if line and line.isnumeric():
        if direction == 'forward':
            x += int(magnitude)
            y += (int(magnitude) * aim)
        elif direction == 'up':
            aim -= int(magnitude)
        elif direction == 'down':
            aim += int(magnitude)
        command = fh.readline()
print(x*y)