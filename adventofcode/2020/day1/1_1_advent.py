import os

def read_from_file(filename):
    file_path = os.path.join(
        os.path.dirname(__file__), filename)
    result = list()
    with open(file_path) as fh:
        lines = fh.read().split('\n')
        for line in lines:
            result.extend([int(num) for num in line.split(',')])
    return result

def main():
    x, y, z = 0, 0, 0
    inputs = read_from_file('input.txt')
    for i in inputs:
        for j in inputs:
            for k in inputs:
                if i == j or i == k or j == k:
                    continue
                if i + j + k == 2020:
                    x = i
                    y = j
                    z = k 
                    break
            if x and y and z:
                break
        if x and y and z:
            break
    print(x, y, z, x+y+z)

if __name__ == "__main__":
    main()