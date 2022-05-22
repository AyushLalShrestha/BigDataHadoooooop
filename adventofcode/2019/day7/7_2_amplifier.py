#!/usr/local/bin/python3

import itertools
import copy
from collections import defaultdict

PM = 0
IM = 1


def parse_opcode(number):
    foprc = f"{number:05}"
    tp, sp, fp = foprc[:3]
    op = foprc[3:]

    return int(op), [int(fp), int(sp), int(tp)]


max_thrust_output = 0
max_phase_setting = list()

# inputseq = [3,8,1001,8,10,8,105,1,0,0,21,42,67,84,97,118,199,280,361,442,99999,3,9,101,4,9,9,102,5,9,9,101,2,9,9,1002,9,2,9,4,9,99,3,9,101,5,9,9,102,5,9,9,1001,9,5,9,102,3,9,9,1001,9,2,9,4,9,99,3,9,1001,9,5,9,1002,9,2,9,1001,9,5,9,4,9,99,3,9,1001,9,5,9,1002,9,3,9,4,9,99,3,9,102,4,9,9,101,4,9,9,102,2,9,9,101,3,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,99]
inputseq = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]


phase_settings = list(itertools.permutations([5, 6, 7, 8, 9]))
for phase_setting in phase_settings:
    phase_pass_value = 0
    thrust_out = 0
    lst = copy.deepcopy(inputseq)
    pointer = 0

    loopon = True
    while loopon:
        for i, phase in enumerate(phase_setting):
            inputs = [phase, phase_pass_value]
            while True:
                opcode, modes = parse_opcode(lst[pointer])
                if opcode == 99:
                    loopon = False
                    break
                elif opcode == 1:
                    o1 = lst[lst[pointer + 1]] if modes[0] == PM else lst[pointer + 1]
                    o2 = lst[lst[pointer + 2]] if modes[1] == PM else lst[pointer + 2]
                    op = lst[pointer + 3]
                    lst[op] = o1 + o2
                    pointer += 4
                elif opcode == 2:
                    o1 = lst[lst[pointer + 1]] if modes[0] == PM else lst[pointer + 1]
                    o2 = lst[lst[pointer + 2]] if modes[1] == PM else lst[pointer + 2]
                    op = lst[pointer + 3]
                    lst[op] = o1 * o2
                    pointer += 4
                elif opcode == 3:
                    op = lst[pointer + 1]
                    lst[op] = inputs.pop(0)
                    pointer += 2
                elif opcode == 4:
                    op = lst[pointer + 1] if modes[0] == PM else pointer + 1
                    pointer += 2
                    # print(f"Outputting: {lst[op]}")
                    phase_pass_value = lst[op]
                    if i == 4:
                        thrust_out = lst[op]
                    break
                elif opcode == 5:
                    o1 = lst[lst[pointer + 1]] if modes[0] == PM else lst[pointer + 1]
                    o2 = lst[lst[pointer + 2]] if modes[1] == PM else lst[pointer + 2]
                    pointer = o2 if o1 != 0 else pointer + 3
                elif opcode == 6:
                    o1 = lst[lst[pointer + 1]] if modes[0] == PM else lst[pointer + 1]
                    o2 = lst[lst[pointer + 2]] if modes[1] == PM else lst[pointer + 2]
                    pointer = o2 if o1 == 0 else pointer + 3
                elif opcode == 7:
                    o1 = lst[lst[pointer + 1]] if modes[0] == PM else lst[pointer + 1]
                    o2 = lst[lst[pointer + 2]] if modes[1] == PM else lst[pointer + 2]
                    op = lst[pointer + 3]
                    lst[op] = 1 if o1 < o2 else 0
                    pointer += 4
                elif opcode == 8:
                    o1 = lst[lst[pointer + 1]] if modes[0] == PM else lst[pointer + 1]
                    o2 = lst[lst[pointer + 2]] if modes[1] == PM else lst[pointer + 2]
                    op = lst[pointer + 3]
                    lst[op] = 1 if o1 == o2 else 0
                    pointer += 4

            if not loopon:
                break

    if thrust_out > max_thrust_output:
        max_thrust_output = thrust_out
        max_phase_setting = phase_setting

print(max_thrust_output)
print(max_phase_setting)