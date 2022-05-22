
file = "/Users/ayushshrestha/my_projects/codeadvent2019/day6/orbit"

def read_from_file(file_path):
    result = {}
    with open(file_path, "r") as fh:
        lines = fh.read().split('\n')
        for line in lines:
            orbited, orbiting = line.split(')')
            result.update({orbiting: orbited})
    return result


orbiting_to_orbited = read_from_file(file)

orbiters = set()
for k, v in orbiting_to_orbited.items():
    orbiters.add(k)

total = 0
for orbiter in orbiters:
    while True:
        if orbiting_to_orbited.get(orbiter):
            total += 1
            orbiter = orbiting_to_orbited[orbiter]
        else:
            break
print(total)





