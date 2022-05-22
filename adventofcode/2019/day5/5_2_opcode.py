#!/usr/local/bin/python3

PM = 0
IM = 1


def parse_opcode(number):
    foprc = f"{number:05}"
    tp, sp, fp = foprc[:3]
    op = foprc[3:]

    return int(op), [int(fp), int(sp), int(tp)]


def add(lst, pointer, modes):
    o1 = lst[lst[pointer + 1]] if modes[0] == PM else lst[pointer + 1]
    o2 = lst[lst[pointer + 2]] if modes[1] == PM else lst[pointer + 2]
    op = lst[pointer + 3]

    lst[op] = o1 + o2
    return pointer + 4


def multiply(lst, pointer, modes):
    o1 = lst[lst[pointer + 1]] if modes[0] == PM else lst[pointer + 1]
    o2 = lst[lst[pointer + 2]] if modes[1] == PM else lst[pointer + 2]
    op = lst[pointer + 3]

    lst[op] = o1 * o2
    return pointer + 4


def place_to_address(lst, pointer, modes):
    op = lst[pointer + 1]

    num = int(input("Enter your input: "))
    lst[op] = num
    return pointer + 2


def output_number(lst, pointer, modes):
    op = lst[pointer + 1] if modes[0] == PM else pointer + 1
    print("Outputing: {}".format(lst[op]))
    return pointer + 2


def point_if_non_zero(lst, pointer, modes):
    o1 = lst[lst[pointer + 1]] if modes[0] == PM else lst[pointer + 1]
    o2 = lst[lst[pointer + 2]] if modes[1] == PM else lst[pointer + 2]

    if o1 != 0:
        return o2
    else:
        return pointer + 3


def point_if_zero(lst, pointer, modes):
    o1 = lst[lst[pointer + 1]] if modes[0] == PM else lst[pointer + 1]
    o2 = lst[lst[pointer + 2]] if modes[1] == PM else lst[pointer + 2]

    if o1 == 0:
        return o2
    else:
        return pointer + 3


def first_less_than_second(lst, pointer, modes):
    o1 = lst[lst[pointer + 1]] if modes[0] == PM else lst[pointer + 1]
    o2 = lst[lst[pointer + 2]] if modes[1] == PM else lst[pointer + 2]
    op = lst[pointer + 3]

    if o1 < o2:
        lst[op] = 1
    else:
        lst[op] = 0
    return pointer + 4


def first_equals_second(lst, pointer, modes):
    o1 = lst[lst[pointer + 1]] if modes[0] == PM else lst[pointer + 1]
    o2 = lst[lst[pointer + 2]] if modes[1] == PM else lst[pointer + 2]
    op = lst[pointer + 3]

    if o1 == o2:
        lst[op] = 1
    else:
        lst[op] = 0
    return pointer + 4


OPCODE_TO_FUNC = {
    1: add,
    2: multiply,
    3: place_to_address,
    4: output_number,
    5: point_if_zero,
    6: point_if_non_zero,
    7: first_less_than_second,
    8: first_equals_second
}


if __name__ == "__main__":
    test = False
    testseq = [
        3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
        1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
        999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99
    ]
    runseq = [3,225,1,225,6,6,1100,1,238,225,104,0,1,191,196,224,1001,224,-85,224,4,224,1002,223,8,223,1001,224,4,224,1,223,224,223,1101,45,50,225,1102,61,82,225,101,44,39,224,101,-105,224,224,4,224,102,8,223,223,101,5,224,224,1,224,223,223,102,14,187,224,101,-784,224,224,4,224,102,8,223,223,101,7,224,224,1,224,223,223,1001,184,31,224,1001,224,-118,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1102,91,18,225,2,35,110,224,101,-810,224,224,4,224,102,8,223,223,101,3,224,224,1,223,224,223,1101,76,71,224,1001,224,-147,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,1101,7,16,225,1102,71,76,224,101,-5396,224,224,4,224,1002,223,8,223,101,5,224,224,1,224,223,223,1101,72,87,225,1101,56,77,225,1102,70,31,225,1102,29,15,225,1002,158,14,224,1001,224,-224,224,4,224,102,8,223,223,101,1,224,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1007,226,226,224,1002,223,2,223,1006,224,329,1001,223,1,223,8,226,677,224,1002,223,2,223,1005,224,344,1001,223,1,223,107,226,677,224,1002,223,2,223,1006,224,359,1001,223,1,223,8,677,677,224,1002,223,2,223,1005,224,374,1001,223,1,223,1108,226,226,224,1002,223,2,223,1005,224,389,1001,223,1,223,7,677,226,224,1002,223,2,223,1005,224,404,101,1,223,223,7,226,226,224,102,2,223,223,1006,224,419,1001,223,1,223,1108,226,677,224,102,2,223,223,1005,224,434,1001,223,1,223,1107,226,226,224,1002,223,2,223,1006,224,449,1001,223,1,223,1007,677,677,224,102,2,223,223,1006,224,464,1001,223,1,223,107,226,226,224,1002,223,2,223,1005,224,479,101,1,223,223,1107,677,226,224,1002,223,2,223,1005,224,494,1001,223,1,223,1008,677,677,224,102,2,223,223,1005,224,509,101,1,223,223,107,677,677,224,102,2,223,223,1005,224,524,1001,223,1,223,1108,677,226,224,1002,223,2,223,1005,224,539,1001,223,1,223,7,226,677,224,102,2,223,223,1006,224,554,1001,223,1,223,8,677,226,224,1002,223,2,223,1006,224,569,101,1,223,223,108,226,226,224,1002,223,2,223,1006,224,584,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,599,101,1,223,223,1008,226,226,224,102,2,223,223,1005,224,614,1001,223,1,223,1007,226,677,224,1002,223,2,223,1006,224,629,1001,223,1,223,108,677,226,224,102,2,223,223,1005,224,644,101,1,223,223,1008,226,677,224,1002,223,2,223,1005,224,659,101,1,223,223,108,677,677,224,1002,223,2,223,1006,224,674,1001,223,1,223,4,223,99,226]

    inputseq = testseq if test else runseq
    POINTER = 0
    while True:
        opcode, modess = parse_opcode(inputseq[POINTER])
        if opcode == 99:
            break
        func = OPCODE_TO_FUNC.get(opcode)
        if not func:
            print(f"ERROR: No function for opcode: {opcode}")
        POINTER = func(inputseq, POINTER, modess)
        if not POINTER:
            break
