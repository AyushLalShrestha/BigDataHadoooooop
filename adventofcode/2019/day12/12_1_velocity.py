import copy


class Moon:
    def __init__(self, name, x_coord=0, y_coord=0, z_coord=0):
        self.name = name
        self.position = [x_coord, y_coord, z_coord]
        self.velocity = [0, 0, 0]

    def __str__(self):
        return "pos =%s, velo=%s" % (self.position, self.velocity)

"""
<x=-7, y=17, z=-11>
<x=9, y=12, z=5>
<x=-9, y=0, z=-4>
<x=4, y=6, z=0>
"""


class Univese:
    def __init__(self):
        self.moons = {
            "io": Moon("Io", -7, 17, -11),
            "europa": Moon("Europa", 9, 12, 5),
            "ganymade": Moon("Ganymede", -9, 0, -4),
            "callisto": Moon("Callisto", 4, 6, 0)
        }

    def simulate_moons_for_steps(self, steps=1000):
        for i in range(0, steps):
            current_moons = copy.deepcopy(self.moons)
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


if __name__ == "__main__":
    universe = Univese()
    universe.simulate_moons_for_steps(1000)
    # universe.show_positions()
    print(universe.find_total_energy())


""" After 10 steps,
pos=<x= 2, y= 1, z=-3>, vel=<x=-3, y=-2, z= 1>
pos=<x= 1, y=-8, z= 0>, vel=<x=-1, y= 1, z= 3>
pos=<x= 3, y=-6, z= 1>, vel=<x= 3, y= 2, z=-3>
pos=<x= 2, y= 0, z= 4>, vel=<x= 1, y=-1, z=-1>
"""
