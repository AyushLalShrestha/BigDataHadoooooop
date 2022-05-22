
from collections import defaultdict
import statistics 

def main():
    with open("input", "r") as fh:
        line = fh.readline()
        positions = line.strip("\n").split(",")
        positions = [int(l) for l in positions]
        
        best_position = 100000000000000
        best_fuel = 100000000000000
        max_position = max(positions)
        min_positions = min(positions)
        for p in range(min_positions, max_position+1):
            fuel_sum = 0
            for i in positions:
                distance = abs(i-p)
                tmp = 0
                for j in range(1, distance+1):
                    fuel_sum += j
                    tmp += j
            if fuel_sum < best_fuel:
                best_fuel = fuel_sum
                best_position = p
        print(best_position, best_fuel)
                
                


if __name__ == "__main__":
    main()