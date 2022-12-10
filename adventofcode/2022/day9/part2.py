import os

current_dir = os.path.dirname(os.path.abspath(__file__))

def move(x, y, direction):
    if direction == "u":
        return [x, y + 1]
    if direction == "d":
        return [x, y-1]
    if direction == "l":
        return [x-1, y]
    if direction == "r":
        return [x+1, y]

def move_T_based_on_H(T, H):
    if T[0] + 2 == H[0] and T[1] == H[1]:
        return [T[0] + 1, T[1]]
    elif T[0] - 2 == H[0] and T[1] == H[1]:
        return [T[0] - 1, T[1]]
    elif T[0] == H[0] and T[1] + 2 == H[1]:
        return [T[0], T[1] + 1]
    elif T[0] == H[0] and T[1] - 2 == H[1]:
        return [T[0], T[1] - 1]
    elif not (H[0] == T[0] or H[1] == T[1]):
        # check if H and T touch each other i.e diagnol
        if not (abs(H[0] - T[0]) == 1 and abs(H[1] - T[1]) == 1):
            diff_X = H[0] - T[0]
            diff_Y = H[1] - T[1]
            move_X = 1
            if diff_X < 0:
                move_X = -1
            move_Y = 1
            if diff_Y < 0:
                move_Y = -1
            T[0] += move_X
            T[1] += move_Y
            return [T[0], T[1]]

    return [T[0], T[1]]

def main():
    # input_file_path = os.path.join(current_dir, "input.test")
    input_file_path = os.path.join(current_dir, "input")
    _input = open(input_file_path, "r").read()
    instructions = _input.split("\n")

    all_T_points = set()
    Ts = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], ]
    position_H = [0, 0]
    for instruction in instructions:
        instruction = instruction.split(" ")
        direction, steps = instruction[0].lower(), int(instruction[1])
        for i in range(steps):
            position_H = move(position_H[0], position_H[1], direction)
            Ts[0] = move_T_based_on_H(Ts[0], position_H)
            for i, t in enumerate(Ts[1:], 1):
                Ts[i] = move_T_based_on_H(Ts[i], Ts[i-1])
                if i == 8:
                    # all_T_points.add(Ts[i])
                    all_T_points.add((Ts[i][0], Ts[i][1]))

    print(all_T_points)
    print(len(all_T_points))

if __name__ == "__main__":
    main()
