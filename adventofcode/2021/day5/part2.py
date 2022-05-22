
from collections import defaultdict

def find_slope(x1, y1, x2, y2):
    m = (y2 - y1)/(x2 - x1)
    b = y1 - m * x1
    return m, b

def main():
    with open("input", "r") as fh:
        co_ord_count = defaultdict(int)
        line = fh.readline()
        while line:
            line = line.strip("\n")
            start_co_ord, end_co_ord = line.split("->", 2)
            x1, y1 = start_co_ord.strip().split(',')
            x2, y2 = end_co_ord.strip().split(',')
            x1 = int(x1)
            x2 = int(x2)
            y1 = int(y1)
            y2 = int(y2)
            
            if x1 == x2:
                if y1 < y2:
                    for y in range(y1, y2+1):
                        co_ord_count[(x1, y)] += 1
                if y2 < y1:
                    for y in range(y2, y1+1):
                        co_ord_count[(x1, y)] += 1
            elif x1 < x2:
                m, b = find_slope(x1, y1, x2, y2)
                for x in range(x1, x2+1):
                    y = m*x + b
                    co_ord_count[(x, y)] += 1
            elif x2 < x1:
                m, b = find_slope(x1, y1, x2, y2)
                for x in range(x2, x1+1):
                    y = m*x + b
                    co_ord_count[(x, y)] += 1
            line = fh.readline()
        count = 0
        for co_ord, c in co_ord_count.items():
            if c >= 2:
                count += 1
        print(count)
            

if __name__ == "__main__":
    main()