import os
import re
pattern = re.compile(r"(\d+)-(\d+) (\w):.*?(\w+)")

FIELDS = [
    "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"
]


def read_from_file(filename):
    file_path = os.path.join(
        os.path.dirname(__file__), filename)
    results = []
    with open(file_path) as fh:
        empty_count = 0
        rows = []
        row = ""
        while True:
            line = fh.readline().strip()
            if not line:
                empty_count += 1
                if empty_count > 1:
                    break
                rows.append(row)
                row = ""
            else:
                row += " " + line
                empty_count = 0
        
    results = []
    for row in rows:
        row_obj = {}
        for i in row.split(' '):
            kv = i.split(':')
            if kv[0] and kv[1]:
                row_obj.update({kv[0].strip(): kv[1].strip()})
        results.append(row_obj)
    return results


def main():
    map_data = read_from_file("input.txt")
    valid = 0
    for row in map_data:
        is_present = [field in row for field in FIELDS]
        if all(is_present):
            valid += 1
    print(valid)

if __name__ == "__main__":
    main()

