
def find_fuel(dist):
    return int(dist / 3) - 2


sum = 0
sum2 = 0
with open("/tmp/advent.input", "r") as fh:
    for line in fh:
        num = int(line.strip())
        sum += find_fuel(num)
        
        while num / 3 != 0:
            res = find_fuel(num)
            if res > 0:
                sum2 += res
                num = res
            else:
                break


print(sum2)
    

