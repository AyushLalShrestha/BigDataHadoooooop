
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from int_code import Computer


class Painter:
    def __init__(self, data):
        self.computer = Computer(data)
        self.position = (0, 0)
        self.map = {(0, 0): '.'}
        self.direction = "up"

    @staticmethod
    def turn_90_left(direction):
        if direction == "up":
            return "left"
        elif direction == "left":
            return "down"
        elif direction == "down":
            return "right"
        elif direction == "right":
            return "up"

    @staticmethod
    def turn_90_right(direction):
        if direction == "up":
            return "right"
        elif direction == "right":
            return "down"
        elif direction == "down":
            return "left"
        elif direction == "left":
            return "up"

    @staticmethod
    def get_next_position(pos, direction):
        if direction == 'up':
            return pos[0], pos[1] + 1
        elif direction == 'down':
            return pos[0], pos[1] - 1
        elif direction == 'left':
            return pos[0] - 1, pos[1]
        elif direction == 'right':
            return pos[0] + 1, pos[1]

    def paint(self):
        while not self.computer.done:
            input = 0 if self.map.get(self.position, '.') == '.' else 1
            color = self.computer.calculate(input)
            self.map[self.position] = "." if color == 0 else "*"

            direction = self.computer.calculate()
            if direction == 0:
                self.direction = self.turn_90_left(self.direction)
            else:
                self.direction = self.turn_90_right(self.direction)
            self.position = self.get_next_position(self.position, self.direction)


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
    inputseq = read_from_file("/Users/ayushshrestha/my_projects/codeadvent2019/day11/input.txt")
    # inputseq = [3,8,1005,8,318,1106,0,11,0,0,0,104,1,104,0,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,102,1,8,29,1006,0,99,1006,0,81,1006,0,29,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,1001,8,0,59,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,1,10,4,10,102,1,8,82,1,1103,3,10,2,104,14,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,102,1,8,111,1,108,2,10,2,1101,7,10,1,1,8,10,1,1009,5,10,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,102,1,8,149,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,101,0,8,172,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,1001,8,0,193,1006,0,39,2,103,4,10,2,1103,20,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,102,1,8,227,1,1106,8,10,2,109,15,10,2,106,14,10,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,1,10,4,10,101,0,8,261,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,102,1,8,283,1,1109,9,10,2,1109,5,10,2,1,2,10,1006,0,79,101,1,9,9,1007,9,1087,10,1005,10,15,99,109,640,104,0,104,1,21101,936333124392,0,1,21101,0,335,0,1106,0,439,21102,1,824663880596,1,21102,346,1,0,1105,1,439,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21102,1,179519553539,1,21101,393,0,0,1106,0,439,21102,46266515623,1,1,21101,0,404,0,1106,0,439,3,10,104,0,104,0,3,10,104,0,104,0,21101,0,983925826324,1,21101,0,427,0,1106,0,439,21101,988220642048,0,1,21102,1,438,0,1105,1,439,99,109,2,21201,-1,0,1,21102,1,40,2,21101,0,470,3,21101,460,0,0,1106,0,503,109,-2,2105,1,0,0,1,0,0,1,109,2,3,10,204,-1,1001,465,466,481,4,0,1001,465,1,465,108,4,465,10,1006,10,497,1101,0,0,465,109,-2,2106,0,0,0,109,4,2102,1,-1,502,1207,-3,0,10,1006,10,520,21101,0,0,-3,22102,1,-3,1,21202,-2,1,2,21102,1,1,3,21102,1,539,0,1105,1,544,109,-4,2106,0,0,109,5,1207,-3,1,10,1006,10,567,2207,-4,-2,10,1006,10,567,21202,-4,1,-4,1106,0,635,21202,-4,1,1,21201,-3,-1,2,21202,-2,2,3,21102,1,586,0,1105,1,544,21202,1,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,605,21101,0,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,627,21202,-1,1,1,21102,1,627,0,105,1,502,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2106,0,0]
    painter = Painter(inputseq)
    painter.paint()
    print(painter.computer.output)