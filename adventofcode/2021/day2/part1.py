
x = 0
y = 0
with open('day2.input', 'r') as fh:
    command = fh.readline()
    while command:
        direction, magnitude = command.split(' ')
        # if line and line.isnumeric():
        if direction == 'forward':
            x += int(magnitude)
        elif direction == 'up':
            y -= int(magnitude)
        elif direction == 'down':
            y += int(magnitude)
        command = fh.readline()
print(x*y)