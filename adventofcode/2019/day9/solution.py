def compute_str(program_str, verbose=False):
    program_str = program_str + ',0' * 1000  # Add additional memory
    program = program_str.split(',')
    program = [int(opcode) for opcode in program]
    return compute(program, verbose=verbose)

# Returns opcode_str; paramter modes; and number to increment instruction_pointer by
def parse_first(int_value):
    map_opcode_to_param_num = {'99': 0, '01': 3, '02': 3, '03': 1, '04': 1, '05': 2, '06': 2, '07': 3, '08': 3, '09': 1}
    max_value_str_len = max(map_opcode_to_param_num.values()) + 2  # Two len opcode

    value_str = str(int_value)
    value_str = value_str.zfill(max_value_str_len)  # Pad with leading zeros

    opcode_str = value_str[-2:]

    parameter_modes = value_str[:-2]

    if opcode_str not in map_opcode_to_param_num.keys():
        print(f'ERROR - invalid opcode: {opcode_str}')

    parameter_mode_map = {'0': 'position', '1': 'immediate', '2': 'relative'}
    parameter_modes = [parameter_mode_map[parameter_mode] for parameter_mode in parameter_modes]
    parameter_modes = [] if opcode_str == '99' else parameter_modes[-map_opcode_to_param_num[opcode_str]:]  # Reduce to correct num of param modes for opcode
    parameter_modes = parameter_modes[::-1]  # Reverse mode order

    instruction_pointer_increment = map_opcode_to_param_num[opcode_str] + 1

    return opcode_str, parameter_modes, instruction_pointer_increment


def compute(program, verbose=False):
    program = list(program)

    instruction_pointer = 0
    relative_base = 0

    while instruction_pointer < len(program):
        int_value = program[instruction_pointer]
        opcode_str, parameter_modes, instruction_pointer_increment = parse_first(int_value)
        if verbose:
            print(f'Processing: {opcode_str}')

        if opcode_str == '99':
            print('Exiting (99 code)...')
            return program

        elif opcode_str == '01':
            # Add
            param_mode_1, param_mode_2, param_mode_3 = parameter_modes

            parameter_1 = program[instruction_pointer + 1]
            if param_mode_1 == 'position':
                operand_1 = program[parameter_1]
            elif param_mode_1 == 'immediate':
                operand_1 = parameter_1
            elif param_mode_1 == 'relative':
                operand_1 = program[relative_base + parameter_1]
            else:
                print(f'ERROR - invalid parameter mode: {parameter_1}')

            parameter_2 = program[instruction_pointer + 2]
            if param_mode_2 == 'position':
                operand_2 = program[parameter_2]
            elif param_mode_2 == 'immediate':
                operand_2 = parameter_2
            elif param_mode_2 == 'relative':
                operand_2 = program[relative_base + parameter_2]
            else:
                print(f'ERROR - invalid parameter mode: {param_mode_2}')

            parameter_3 = program[instruction_pointer + 3]
            if param_mode_3 == 'position':  # Note: since writing to memory, cannot be immediate
                output_address = parameter_3
            elif param_mode_3 == 'relative':
                output_address = relative_base + parameter_3
            else:
                print('ERROR - immediate mode for writing to memory')

            # Perform op
            result = operand_1 + operand_2
            program[output_address] = result
            instruction_pointer += instruction_pointer_increment


        elif opcode_str == '02':
            # Multiply
            param_mode_1, param_mode_2, param_mode_3 = parameter_modes

            parameter_1 = program[instruction_pointer + 1]
            if param_mode_1 == 'position':
                operand_1 = program[parameter_1]
            elif param_mode_1 == 'immediate':
                operand_1 = parameter_1
            elif param_mode_1 == 'relative':
                operand_1 = program[relative_base + parameter_1]
            else:
                print(f'ERROR - invalid parameter mode: {parameter_1}')

            parameter_2 = program[instruction_pointer + 2]
            if param_mode_2 == 'position':
                operand_2 = program[parameter_2]
            elif param_mode_2 == 'immediate':
                operand_2 = parameter_2
            elif param_mode_2 == 'relative':
                operand_2 = program[relative_base + parameter_2]
            else:
                print(f'ERROR - invalid parameter mode: {param_mode_2}')

            parameter_3 = program[instruction_pointer + 3]
            if param_mode_3 == 'position':  # Note: since writing to memory, cannot be immediate
                output_address = parameter_3
            elif param_mode_3 == 'relative':
                output_address = relative_base + parameter_3
            else:
                print('ERROR - immediate mode while writing to memory')

            # Perform op
            result = operand_1 * operand_2
            program[output_address] = result
            instruction_pointer += instruction_pointer_increment

        elif opcode_str == '03':
            # Input
            param_mode_1 = parameter_modes[0]

            parameter_1 = program[instruction_pointer + 1]
            if param_mode_1 == 'position':
                output_address = parameter_1
            elif param_mode_1 == 'relative':
                output_address = relative_base + parameter_1
            else:
                print('ERROR - immediate mode while writing to memory')

            user_input = None
            # Keep looping while user_input is None
            while user_input is None:
                user_input = (yield 'input')
            if verbose:
                print(f'Input Received: {user_input}')

            program[output_address] = user_input
            instruction_pointer += instruction_pointer_increment

        elif opcode_str == '04':
            # Output
            param_mode_1 = parameter_modes[0]
            parameter_1 = program[instruction_pointer + 1]
            read_address = parameter_1

            if param_mode_1 == 'position':
                output = program[read_address]
            elif param_mode_1 == 'immediate':
                output = read_address
            elif param_mode_1 == 'relative':
                output = program[relative_base + read_address]
            else:
                print(f'ERROR - invalid parameter mode: {param_mode_1}')

            if verbose:
                print(f'Output: {output}')
            yield output
            instruction_pointer += instruction_pointer_increment

        elif opcode_str == '05':
            # Jump if True
            param_mode_1, param_mode_2 = parameter_modes
            parameter_1 = program[instruction_pointer + 1]
            parameter_2 = program[instruction_pointer + 2]

            if param_mode_1 == 'position':
                operand_1 = program[parameter_1]
            elif param_mode_1 == 'immediate':
                operand_1 = parameter_1
            elif param_mode_1 == 'relative':
                operand_1 = program[relative_base + parameter_1]
            else:
                print(f'ERROR - invalid parameter mode: {param_mode_1}')

            if param_mode_2 == 'position':
                operand_2 = program[parameter_2]
            elif param_mode_2 == 'immediate':
                operand_2 = parameter_2
            elif param_mode_2 == 'relative':
                operand_2 = program[relative_base + parameter_2]
            else:
                print(f'ERROR - invalid parameter mode: {param_mode_2}')

            if operand_1 != 0:
                instruction_pointer = operand_2
            else:
                instruction_pointer += instruction_pointer_increment

        elif opcode_str == '06':
            # Jump if False
            param_mode_1, param_mode_2 = parameter_modes
            parameter_1 = program[instruction_pointer + 1]
            parameter_2 = program[instruction_pointer + 2]

            if param_mode_1 == 'position':
                operand_1 = program[parameter_1]
            elif param_mode_1 == 'immediate':
                operand_1 = parameter_1
            elif param_mode_1 == 'relative':
                operand_1 = program[relative_base + parameter_1]
            else:
                print(f'ERROR - invalid parameter mode: {param_mode_1}')

            if param_mode_2 == 'position':
                operand_2 = program[parameter_2]
            elif param_mode_2 == 'immediate':
                operand_2 = parameter_2
            elif param_mode_2 == 'relative':
                operand_2 = program[relative_base + parameter_2]
            else:
                print(f'ERROR - invalid parameter mode: {param_mode_2}')

            if operand_1 == 0:
                instruction_pointer = operand_2
            else:
                instruction_pointer += instruction_pointer_increment

        elif opcode_str == '07':
            # Less than
            param_mode_1, param_mode_2, param_mode_3 = parameter_modes
            parameter_1 = program[instruction_pointer + 1]
            parameter_2 = program[instruction_pointer + 2]

            if param_mode_1 == 'position':
                operand_1 = program[parameter_1]
            elif param_mode_1 == 'immediate':
                operand_1 = parameter_1
            elif param_mode_1 == 'relative':
                operand_1 = program[relative_base + parameter_1]
            else:
                print(f'ERROR - invalid parameter mode: {param_mode_1}')

            if param_mode_2 == 'position':
                operand_2 = program[parameter_2]
            elif param_mode_2 == 'immediate':
                operand_2 = parameter_2
            elif param_mode_2 == 'relative':
                operand_2 = program[relative_base + parameter_2]
            else:
                print(f'ERROR - invalid parameter mode: {param_mode_2}')

            parameter_3 = program[instruction_pointer + 3]
            output_address = parameter_3
            if param_mode_3 == 'position':
                program[output_address] = 1 if operand_1 < operand_2 else 0
            elif param_mode_3 == 'relative':
                program[relative_base + output_address] = 1 if operand_1 < operand_2 else 0
            else:
                print('ERROR - immediate mode while writing to memory')

            instruction_pointer += instruction_pointer_increment

        elif opcode_str == '08':
            # Equals
            param_mode_1, param_mode_2, param_mode_3 = parameter_modes
            parameter_1 = program[instruction_pointer + 1]
            parameter_2 = program[instruction_pointer + 2]

            if param_mode_1 == 'position':
                operand_1 = program[parameter_1]
            elif param_mode_1 == 'immediate':
                operand_1 = parameter_1
            elif param_mode_1 == 'relative':
                operand_1 = program[relative_base + parameter_1]
            else:
                print(f'ERROR - invalid parameter mode: {param_mode_1}')

            if param_mode_2 == 'position':
                operand_2 = program[parameter_2]
            elif param_mode_2 == 'immediate':
                operand_2 = parameter_2
            elif param_mode_2 == 'relative':
                operand_2 = program[relative_base + parameter_2]
            else:
                print(f'ERROR - invalid parameter mode: {param_mode_2}')

            parameter_3 = program[instruction_pointer + 3]
            output_address = parameter_3

            if param_mode_3 == 'position':
                program[output_address] = 1 if operand_1 == operand_2 else 0
            elif param_mode_3 == 'relative':
                program[relative_base + output_address] = 1 if operand_1 == operand_2 else 0
            else:
                print('ERROR - immediate mode while writing to memory')

            instruction_pointer += instruction_pointer_increment

        elif opcode_str == '09':
            # Relative base offset instruction
            param_mode_1 = parameter_modes[0]

            parameter_1 = program[instruction_pointer + 1]
            if param_mode_1 == 'position':
                operand_1 = program[parameter_1]
            elif param_mode_1 == 'immediate':
                operand_1 = parameter_1
            elif param_mode_1 == 'relative':
                operand_1 = program[relative_base + parameter_1]
            else:
                print(f'ERROR - invalid parameter mode: {param_mode_1}')

            relative_base = relative_base + operand_1
            instruction_pointer += instruction_pointer_increment

        else:
            print('ERROR - invalid opcode')
            return

    print('End of program without 99 code')
    return

puzzle_input = '1102,34463338,34463338,63,1007,63,34463338,63,1005,63,53,1101,0,3,1000,109,988,209,12,9,1000,209,6,209,3,203,0,1008,1000,1,63,1005,63,65,1008,1000,2,63,1005,63,902,1008,1000,0,63,1005,63,58,4,25,104,0,99,4,0,104,0,99,4,17,104,0,99,0,0,1102,32,1,1019,1101,0,500,1023,1101,0,636,1025,1102,36,1,1010,1101,0,29,1013,1102,864,1,1029,1102,21,1,1000,1102,1,507,1022,1102,1,28,1011,1102,38,1,1008,1101,0,35,1004,1101,25,0,1018,1102,24,1,1005,1102,30,1,1009,1102,1,869,1028,1101,0,37,1007,1102,1,23,1017,1102,1,20,1015,1102,1,22,1003,1101,0,39,1001,1102,1,31,1012,1101,701,0,1026,1101,0,641,1024,1101,0,34,1016,1102,1,0,1020,1102,698,1,1027,1102,33,1,1002,1102,26,1,1006,1101,0,1,1021,1101,0,27,1014,109,12,21101,40,0,0,1008,1012,40,63,1005,63,203,4,187,1105,1,207,1001,64,1,64,1002,64,2,64,109,-11,1207,7,37,63,1005,63,223,1105,1,229,4,213,1001,64,1,64,1002,64,2,64,109,14,1206,5,247,4,235,1001,64,1,64,1105,1,247,1002,64,2,64,109,-2,1207,-4,31,63,1005,63,269,4,253,1001,64,1,64,1105,1,269,1002,64,2,64,109,-6,1208,-5,35,63,1005,63,289,1001,64,1,64,1106,0,291,4,275,1002,64,2,64,109,9,21108,41,39,-1,1005,1015,311,1001,64,1,64,1105,1,313,4,297,1002,64,2,64,109,-5,2101,0,-9,63,1008,63,33,63,1005,63,339,4,319,1001,64,1,64,1106,0,339,1002,64,2,64,1205,10,351,4,343,1106,0,355,1001,64,1,64,1002,64,2,64,109,-18,2108,35,9,63,1005,63,375,1001,64,1,64,1105,1,377,4,361,1002,64,2,64,109,18,1205,9,389,1105,1,395,4,383,1001,64,1,64,1002,64,2,64,109,7,21107,42,41,-8,1005,1010,415,1001,64,1,64,1106,0,417,4,401,1002,64,2,64,109,-12,2102,1,0,63,1008,63,29,63,1005,63,437,1106,0,443,4,423,1001,64,1,64,1002,64,2,64,109,3,1208,0,30,63,1005,63,461,4,449,1105,1,465,1001,64,1,64,1002,64,2,64,109,5,1202,-5,1,63,1008,63,31,63,1005,63,489,1001,64,1,64,1106,0,491,4,471,1002,64,2,64,109,15,2105,1,-6,1001,64,1,64,1106,0,509,4,497,1002,64,2,64,109,-10,1206,2,525,1001,64,1,64,1106,0,527,4,515,1002,64,2,64,109,-18,1202,0,1,63,1008,63,39,63,1005,63,553,4,533,1001,64,1,64,1106,0,553,1002,64,2,64,109,1,2107,21,1,63,1005,63,571,4,559,1105,1,575,1001,64,1,64,1002,64,2,64,109,7,2102,1,-8,63,1008,63,39,63,1005,63,601,4,581,1001,64,1,64,1105,1,601,1002,64,2,64,109,2,1201,-7,0,63,1008,63,35,63,1005,63,623,4,607,1106,0,627,1001,64,1,64,1002,64,2,64,109,20,2105,1,-7,4,633,1106,0,645,1001,64,1,64,1002,64,2,64,109,-16,21107,43,44,-4,1005,1011,663,4,651,1105,1,667,1001,64,1,64,1002,64,2,64,109,-11,2107,36,0,63,1005,63,687,1001,64,1,64,1106,0,689,4,673,1002,64,2,64,109,19,2106,0,4,1106,0,707,4,695,1001,64,1,64,1002,64,2,64,109,-14,21108,44,44,6,1005,1015,725,4,713,1105,1,729,1001,64,1,64,1002,64,2,64,109,1,1201,-6,0,63,1008,63,36,63,1005,63,749,1106,0,755,4,735,1001,64,1,64,1002,64,2,64,109,-1,21101,45,0,10,1008,1019,42,63,1005,63,775,1105,1,781,4,761,1001,64,1,64,1002,64,2,64,109,16,21102,46,1,-7,1008,1018,44,63,1005,63,801,1105,1,807,4,787,1001,64,1,64,1002,64,2,64,109,-3,21102,47,1,-4,1008,1018,47,63,1005,63,833,4,813,1001,64,1,64,1105,1,833,1002,64,2,64,109,-14,2108,38,0,63,1005,63,851,4,839,1105,1,855,1001,64,1,64,1002,64,2,64,109,17,2106,0,3,4,861,1106,0,873,1001,64,1,64,1002,64,2,64,109,-31,2101,0,10,63,1008,63,36,63,1005,63,897,1001,64,1,64,1106,0,899,4,879,4,64,99,21101,0,27,1,21101,0,913,0,1106,0,920,21201,1,53612,1,204,1,99,109,3,1207,-2,3,63,1005,63,962,21201,-2,-1,1,21102,940,1,0,1106,0,920,21202,1,1,-1,21201,-2,-3,1,21101,955,0,0,1106,0,920,22201,1,-1,-2,1105,1,966,21201,-2,0,-2,109,-3,2106,0,0'
# puzzle_input = '109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99'


if __name__ == '__main__':
    print('Solution to Part 1')
    run = compute_str(puzzle_input)
    next(run)
    print(run.send(1))

    print('Solution to Part 2')
    run = compute_str(puzzle_input)
    next(run)
    print(run.send(2))