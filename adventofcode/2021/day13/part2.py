from collections import defaultdict


def transform_map_y(dot_coords, line_y):
    transformed = set()
    for x_coord, y_coord in dot_coords:
        if y_coord < line_y:
            transformed.add((x_coord, y_coord))
        elif y_coord == line_y:
            continue
        elif y_coord > line_y:
            diff = y_coord - line_y
            new_y_coord = line_y - diff
            transformed.add((x_coord, new_y_coord))
    return list(transformed)


def transform_map_x(dot_coords, line_x):
    transformed = set()
    for x_coord, y_coord in dot_coords:
        if x_coord < line_x:
            transformed.add((x_coord, y_coord))
        elif x_coord == line_x:
            continue
        elif x_coord > line_x:
            diff = x_coord - line_x
            new_x_coord = line_x - diff
            transformed.add((new_x_coord, y_coord))
    return list(transformed)

def visulize_map(dot_coords):
    max_x = 0
    max_y = 0 
    for x_coord, y_coord in dot_coords:
        if x_coord > max_x:
            max_x = x_coord
        if y_coord > max_y:
            max_y = y_coord
    
    for y in range(max_y+1):
        x_print = ""
        for x in range(max_x+1):
            if (x, y) in dot_coords:
                x_print += "# "
            else:
                x_print += ". "
        print(x_print)

if __name__ == "__main__":
    dot_coords = []
    with open("input", "r") as fh:
        line = fh.readline()
        while line:
            data = line.strip("\n")
            x_coord, y_coord = data.split(",", 1)
            x_coord = int(x_coord)
            y_coord = int(y_coord)
            dot_coords.append((x_coord, y_coord))
            line = fh.readline()
    
    
    transformed = transform_map_x(dot_coords, 655)
    transformed = transform_map_y(transformed, 447)
    transformed = transform_map_x(transformed, 327)
    transformed = transform_map_y(transformed, 223)
    transformed = transform_map_x(transformed, 163)
    transformed = transform_map_y(transformed, 111)
    transformed = transform_map_x(transformed, 81)
    transformed = transform_map_y(transformed, 55)
    transformed = transform_map_x(transformed, 40)
    transformed = transform_map_y(transformed, 27)
    transformed = transform_map_y(transformed, 13)
    transformed = transform_map_y(transformed, 6)

    print(len(transformed))
    visulize_map(transformed)
