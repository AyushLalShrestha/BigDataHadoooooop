
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from int_code import Computer


def read_from_file(file_path="input.txt"):
    result = list()
    with open(file_path) as fh:
        lines = fh.read().split('\n')
        for line in lines:
            result.extend([int(num) for num in line.split(',')])
    return result


class TileDrawer:
    def __init__(self, data):
        self.computer = Computer(data)
        self.map = {}

    @staticmethod
    def parse_obj(code):
        return code

    def draw(self,):
        while not self.computer.done:
            x_axis = self.computer.calculate()
            if x_axis is None:
                break
            y_axis = self.computer.calculate()
            draw_obj_code = self.computer.calculate()
            obj = self.parse_obj(draw_obj_code)
            self.map.update({(x_axis, y_axis): obj})

    def count(self, obj_code):
        count = 0
        for co_ord, code in self.map.items():
            if code == obj_code:
                count += 1
        return count


inputseq = read_from_file("/Users/ayushshrestha/my_projects/codeadvent2019/day13/input.txt")
# inputseq = [1,2,3,6,5,4,99]

seq = {}
for i, j in enumerate(inputseq):
    seq.update({i: j})

tile_drawer = TileDrawer(seq)
tile_drawer.draw()
print(tile_drawer.count(2))
