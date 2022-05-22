#!/usr/local/bin/python3

import operator

path = "/Users/ayushshrestha/my_projects/codeadvent2019/input"

ops = {1: operator.add, 2: operator.mul}


def read_from_file(file_path):
    with open(file_path, "r") as fh:
        return [int(num) for num in fh.read().split(",")]


def convert_list(lst, n):
    opcode = lst[n]
    if opcode == 99:
        return False
    pointer_1 = lst[n + 1]
    pointer_2 = lst[n + 2]
    output_pointer = lst[n + 3]

    value_1 = lst[pointer_1]
    value_2 = lst[pointer_2]
    if ops.get(opcode):
        lst[output_pointer] = ops[opcode](value_1, value_2)
        return True
    else:
        return False


intseq = read_from_file(path)
# print(intseq)
intseq = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,5,23,1,23,9,27,2,27,6,31,1,31,6,35,2,35,9,39,1,6,39,43,2,10,43,47,1,47,9,51,1,51,6,55,1,55,6,59,2,59,10,63,1,6,63,67,2,6,67,71,1,71,5,75,2,13,75,79,1,10,79,83,1,5,83,87,2,87,10,91,1,5,91,95,2,95,6,99,1,99,6,103,2,103,6,107,2,107,9,111,1,111,5,115,1,115,6,119,2,6,119,123,1,5,123,127,1,127,13,131,1,2,131,135,1,135,10,0,99,2,14,0,0]

for i in range(0, 100):
    for j in range(0, 100):
        counter = 0
        intseq = read_from_file(path)
        intseq[1] = i
        intseq[2] = j
        while True:
            res = convert_list(intseq, counter)
            if res is True:
                counter += 4
            else:
                print(intseq)
                break
        if intseq[0] == 19690720:
            print(i)
            print(j)
            import sys
            sys.exit(0)
        
