
file = "/Users/ayushshrestha/my_projects/codeadvent2019/day6/orbit"

def read_from_file(file_path):
    result = {}
    with open(file_path, "r") as fh:
        lines = fh.read().split('\n')
        for line in lines:
            orbited, orbiting = line.split(')')
            result.update({orbiting: orbited})
    return result


def moves_required(orbiting, to_orbited):
    moves = 0
    orbited = orbiting_to_orbited.get(orbiting)
    while orbited != to_orbited:
        moves += 1
        orbited = orbiting_to_orbited.get(orbiting)
        orbiting = orbited
    return moves - 1

def find_parent_orbits(orbiter):
    parents = []

    parent = orbiting_to_orbited.get(orbiter)
    while parent:
        parent = orbiting_to_orbited.get(orbiter)
        if parent:
            parents.append(parent)
            orbiter = parent
    return parents


orbiting_to_orbited = read_from_file(file)
orbiters = set(list(map(lambda k: k, orbiting_to_orbited)))

you_parents = find_parent_orbits('YOU')
san_parents = find_parent_orbits('SAN')

intersection = None
for i in you_parents:
    for j in san_parents:
        if i == j:
            intersection = i
            break
        if intersection:
            break

if intersection:
    total_moves = moves_required("YOU", intersection) \
                  + moves_required("SAN", intersection)

    print(total_moves)