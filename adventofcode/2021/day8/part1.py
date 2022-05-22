
from collections import defaultdict
import statistics 


numbers_to_digit = {
    0: ['a', 'b', 'c', 'e', 'f', 'g'],
    1: ['c', 'f'],
    2: ['a', 'c', 'd', 'e', 'g'],
    3: ['a', 'c', 'd', 'f', 'g'],
    4: ['b', 'c', 'd', 'f'],
    5: ['a', 'b', 'd', 'f', 'g'],
    6: ['a', 'b', 'd', 'e', 'f', 'g'],
    7: ['a', 'c', 'f'],
    8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    9: ['a', 'b', 'c', 'd', 'f', 'g'],
}
def main():
    number_to_len = {
        1: 2,
        4: 4,
        7: 3,
        8: 7
    }
    count = 0
    with open("input", "r") as fh:
        line = fh.readline()
        while line:
            data = line.strip("\n").split("|")
            output_vals = data[1]
            output_vals = output_vals.strip().split(' ')
            for val in output_vals:
                if len(val) in [2,4,3,7]:
                    count += 1
            line = fh.readline()
        print(count)

if __name__ == "__main__":
    main()