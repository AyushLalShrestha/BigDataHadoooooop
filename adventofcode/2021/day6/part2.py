
from collections import defaultdict

def main():
    with open("input", "r") as fh:
        line = fh.readline()
        
        lantern_list = line.strip("\n").split(",")
        lantern_list = [int(l) for l in lantern_list]
        age_to_count = defaultdict(int)
        for l in lantern_list:
            age_to_count[l] += 1
        
        for i in range(256):
            new_age_to_count = defaultdict(int)
            for age, count in age_to_count.items():
                if age == 0:
                    new_age_to_count[6] += 1*count
                    new_age_to_count[8] += 1*count
                else:
                    new_age_to_count[age-1] += 1*count
            age_to_count = new_age_to_count
        # print(lantern_list)
        print(age_to_count)
        count = 0
        for a, c in age_to_count.items():
            count += c
        print(count)

if __name__ == "__main__":
    main()