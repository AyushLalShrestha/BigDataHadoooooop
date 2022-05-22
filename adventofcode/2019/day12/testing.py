import copy


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

<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>

<x=-7, y=17, z=-11>
<x=9, y=12, z=5>
<x=-9, y=0, z=-4>
<x=4, y=6, z=0>
"""


class Univese:
    def __init__(self):
        self.moons = {
            "io": Moon("Io", -8, -10, 0),
            "europa": Moon("Europa", 5, 5, 10),
            "ganymade": Moon("Ganymede", 2, -7, 3),
            "callisto": Moon("Callisto", 9, -8, -3)
        }
        # self.moons = {
        #     "io": Moon("Io", -1, 0, 2),
        #     "europa": Moon("Europa", 2, -10, -7),
        #     "ganymade": Moon("Ganymede", 4, -8, 8),
        #     "callisto": Moon("Callisto", 3, 5, -1)
        # }
        self.states = dict()

    def simulate_moons_for_steps(self):
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

            if self.is_state_repeating():
                unit_steps = self.find_repeat_difference()
                print(unit_steps)
                break

    def is_state_repeating(self):
        state = []
        for name, moon in self.moons.items():
            state.append(moon.position)
            state.append(moon.velocity)
        state = "".join([str(v) for v in state])
        print(len(self.states))
        if state in self.states.keys():
            return True
        return False

    def find_repeat_difference(self):
        state = []
        for name, moon in self.moons.items():
            state.append(moon.position)
            state.append(moon.velocity)
        state = "".join([str(v) for v in state])
        previous_step_number = self.states[state]
        current_state_number = len(self.states.keys()) + 1
        return current_state_number - previous_step_number

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

    def find_total_energy(self):
        total_energy = 0
        for name, moon in self.moons.items():
            pe = sum([abs(p) for p in moon.position])
            ke = sum([abs(v) for v in moon.velocity])
            total_energy += pe * ke
        return total_energy

    def save_current_state(self):
        state = []
        for name, moon in self.moons.items():
            state.append(moon.position)
            state.append(moon.velocity)
        state = "".join([str(v) for v in state])
        self.states[state] = len(self.states.keys()) + 1


if __name__ == "__main__":
    universe = Univese()
    universe.simulate_moons_for_steps()
    # universe.show_positions()
    # part 1: print(universe.find_total_energy())
