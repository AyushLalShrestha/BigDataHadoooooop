
class Computer:
    def __init__(self, data):
        self.idx = 0
        self.relative_base = 0
        self.data = data
        self.done = False
        self.output = None
        self.inputs = []

    @staticmethod
    def parse_opcode(instruction):
        foprc = f"{instruction:05}"
        mode2, mode1, mode0 = foprc[:3]
        op = foprc[3:]

        return [int(mode0), int(mode1), int(mode2), int(op)]

    def get_params(self, mode1, mode2):
        return self.get_param(mode1, 1), self.get_param(mode2, 2)

    def get_param(self, mode, increment):
        val = self.data[self.idx + increment]
        if mode == 0:
            return self.data[val]
        if mode == 2:
            return self.data[val + self.relative_base]
        return val

    def get_output_address(self, mode, increment):
        val = self.data[self.idx + increment]
        if mode == 0:
            pass
        if mode == 2:
            val += self.relative_base
        return val

    def add(self, param1, param2):
        return param1 + param2

    def multiply(self, param1, param2):
        return param1 * param2

    def less_than(self, param1, param2):
        return 1 if param1 < param2 else 0

    def equals(self, param1, param2):
        return 1 if param1 == param2 else 0

    def jump_if_true(self, mode1, mode2):
        param1, param2 = self.get_params(mode1, mode2)
        return param2 if param1 != 0 else self.idx + 3

    def jump_if_false(self, mode1, mode2):
        param1, param2 = self.get_params(mode1, mode2)
        return param2 if param1 == 0 else self.idx + 3

    def calculate(self, input_val=None):
        if input_val is not None:
            self.inputs.append(input_val)
        while True:
            mode1, mode2, mode3, opcode = self.parse_opcode(self.data[self.idx])
            if opcode == 1:
                param1, param2 = self.get_params(mode1, mode2)
                out_address = self.get_output_address(mode3, 3)
                self.data[out_address] = self.add(param1, param2)
                self.idx += 4
            elif opcode == 2:
                param1, param2 = self.get_params(mode1, mode2)
                out_address = self.get_output_address(mode3, 3)
                self.data[out_address] = self.multiply(param1, param2)
                self.idx += 4
            elif opcode == 3:
                out_address = self.get_output_address(mode1, 1)
                self.data[out_address] = self.inputs.pop(0)
                self.idx += 2
            elif opcode == 4:
                self.output = self.get_param(mode1, 1)
                self.idx += 2
                return self.output
            elif opcode == 5:
                self.idx = self.jump_if_true(mode1, mode2)
            elif opcode == 6:
                self.idx = self.jump_if_false(mode1, mode2)
            elif opcode == 7:
                param1, param2 = self.get_params(mode1, mode2)
                out_address = self.get_output_address(mode3, 3)
                self.data[out_address] = self.less_than(param1, param2)
                self.idx += 4
            elif opcode == 8:
                param1, param2 = self.get_params(mode1, mode2)
                out_address = self.get_output_address(mode3, 3)
                self.data[out_address] = self.equals(param1, param2)
                self.idx += 4
            elif opcode == 9:
                self.relative_base += self.get_param(mode1, 1)
                self.idx += 2
            elif opcode == 99:
                self.done = True
                return None


def read_from_file(file_path="input.txt"):
    result = list()
    with open(file_path) as fh:
        lines = fh.read().split('\n')
        for line in lines:
            result.extend([int(num) for num in line.split(',')])
    seq = {}
    for i, j in enumerate(result):
        seq.update({i: j})
    return seq


if __name__ == "__main__":
    inputseq = read_from_file("/Users/ayushshrestha/my_projects/codeadvent2019/day9/input.txt")
    computer = Computer(inputseq)
    computer.calculate(2)
    print(computer.output)
