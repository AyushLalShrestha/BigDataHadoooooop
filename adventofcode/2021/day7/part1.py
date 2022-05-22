
from collections import defaultdict
import statistics 

def main():
    with open("input", "r") as fh:
        line = fh.readline()
        
        positions = line.strip("\n").split(",")
        positions = [int(l) for l in positions]
        median_position = int(statistics.median(positions))
        
        total_fuel = 0
        for i in positions:
            total_fuel += abs(i-median_position)
        print(total_fuel)


if __name__ == "__main__":
    main()