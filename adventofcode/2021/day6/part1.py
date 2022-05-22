
from collections import defaultdict

def main():
    with open("input.test", "r") as fh:
        line = fh.readline()
        
        positions = line.strip("\n").split(",")
        positions = [int(l) for l in positions]
        
        total = 0
        for position in positions:
            total += position
        print(total/len(positions))

if __name__ == "__main__":
    main()