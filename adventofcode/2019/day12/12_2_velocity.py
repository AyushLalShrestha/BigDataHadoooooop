import copy
from math import gcd
from collections import defaultdict


def find_lcm(numbers):
    print(numbers)
    lcm = numbers[0]
    for i in numbers[1:]:
        lcm = (lcm * i) / gcd(int(lcm), i)
    return lcm


class Moon:
    def __init__(self, name, x_coord=0, y_coord=0, z_coord=0):
        self.name = name
        self.position = [x_coord, y_coord, z_coord]
        self.velocity = [0, 0, 0]

    def __str__(self):
        return "pos =%s, velo=%s" % (self.position, self.velocity)

"""
<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>

<x=-7, y=17, z=-11>
<x=9, y=12, z=5>
<x=-9, y=0, z=-4>
<x=4, y=6, z=0>
"""


class Univese:
    def __init__(self):
        # self.moons = {
        #     "io": Moon("Io", -7, 17, -11),
        #     "europa": Moon("Europa", 9, 12, 5),
        #     "ganymade": Moon("Ganymede", -9, 0, -4),
        #     "callisto": Moon("Callisto", 4, 6, 0)
        # }
        self.moons = {
            "io": Moon("Io", -1, 0, 2),
            "europa": Moon("Europa", 2, -10, -7),
            "ganymade": Moon("Ganymede", 4, -8, 8),
            "callisto": Moon("Callisto", 3, 5, -1)
        }
        self.states = defaultdict(list)
        self.repeated = defaultdict(bool)

    def save_current_state(self):
        for name, moon in self.moons.items():
            if self.repeated[name] is not False:
                continue
            moons_position = ''
            for position in moon.position:
                moons_position += str(position)
            self.states[name].append(moons_position)

    def check_repeat_states(self):
        for name, moon in self.moons.items():
            if self.repeated[name] is not False:
                continue
            moons_position = ''
            for position in moon.position:
                moons_position += str(position)
            moons_states = self.states[name]
            if moons_position in moons_states:
                self.repeated[name] = len(moons_states) - moons_states.index(moons_position) - 1

    def halt(self):
        for name, moon in self.moons.items():
            if self.repeated[name] is False:
                return False
        return True

    def simulate_moons_for_steps(self):
        self.count = 0
        while True:
            current_moons = copy.deepcopy(self.moons)
            self.save_current_state()
            for name, __ in current_moons.items():
                x_pull = y_pull = z_pull = 0
                for moon_name, moon_obj in current_moons.items():
                    a = b = c = 0
                    if name == moon_name:
                        continue
                    a, b, c = self.transform_moon(
                        self.moons[name], moon_obj)
                    x_pull += a
                    y_pull += b
                    z_pull += c

                self.moons[name].velocity[0] += x_pull
                self.moons[name].velocity[1] += y_pull
                self.moons[name].velocity[2] += z_pull

                self.moons[name].position[0] += self.moons[name].velocity[0]
                self.moons[name].position[1] += self.moons[name].velocity[1]
                self.moons[name].position[2] += self.moons[name].velocity[2]
            self.count += 1
            self.check_repeat_states()
            print("- - - - - - - ")
            for i, v in self.states.items():
                print(f"{i} = {v}")
            print(self.repeated)
            print("- - - - - - - ")
            if self.halt():
                break

    def transform_moon(self, moon, other_moon):
        x_pull = 0
        y_pull = 0
        z_pull = 0

        if moon.position[0] < other_moon.position[0]:
            x_pull = 1
        elif moon.position[0] > other_moon.position[0]:
            x_pull = -1

        if moon.position[1] < other_moon.position[1]:
            y_pull = 1
        elif moon.position[1] > other_moon.position[1]:
            y_pull = -1

        if moon.position[2] < other_moon.position[2]:
            z_pull = 1
        elif moon.position[2] > other_moon.position[2]:
            z_pull = -1

        return [x_pull, y_pull, z_pull]

    def show_positions(self,):
        for name, moon in self.moons.items():
            print("%s => %s" % (name, moon))

    def find_minimum_repeat(self):
        numbers = []
        for i, v in self.repeated.items():
            numbers.append(v)
        return find_lcm(numbers)


if __name__ == "__main__":
    universe = Univese()
    universe.simulate_moons_for_steps()
    print(universe.repeated)
    # print(universe.find_minimum_repeat())
    universe.show_positions()
    print(universe.count)