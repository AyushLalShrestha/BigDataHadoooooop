import os
import re

EYE_COLORS = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def read_from_file(filename):
    file_path = os.path.join(os.path.dirname(__file__), filename)
    with open(file_path) as fh:
        empty_count = 0
        rows = []
        row = {}
        while True:
            line = fh.readline().strip()
            if not line:
                empty_count += 1
                if empty_count > 1:
                    break
                rows.append(row)
                row = {}
            else:
                kv = line.split(' ')
                for k in kv:
                    v = k.split(':')
                    if v[0] and v[1]:
                        row.update({v[0].strip(): v[1].strip()})
                empty_count = 0
        
    return rows

def is_valid_birthyear(byr):
    if len(byr) != 4:
        return False
    return 1920 <= int(byr) <= 2002

def is_valid_issueyear(iyr):
    if len(iyr) != 4:
        return False
    return 2010 <= int(iyr) <= 2020

def is_valid_expiryyear(eyr):
    if len(eyr) != 4:
        return False
    return 2020 <= int(eyr) <= 2030

def is_valid_height(hgt):
    if not (hgt and len(hgt) > 2):
        return False
    
    metric = hgt[-2:]
    hgt = int(hgt[:-2])
    if metric == 'cm':
        return 150 <= hgt <= 193
    elif metric == 'in':
        return 59 <= hgt <= 76
    else:
        return False

def is_valid_haircolor(hcl):
    if re.match(r'^\#[0-9a-f]{6}$', hcl) is None:
        return False
    return True

def is_valid_eyecolor(ecl):
    return ecl in EYE_COLORS

def is_valid_passportid(pid):
    if re.match(r'^\d{9}$', pid) is None:
        return False
    return True

def main():
    map_data = read_from_file("input.txt")
    valid = 0
    for row in map_data:
        if not is_valid_birthyear(row.get('byr', '3000')):
            continue
        if not is_valid_issueyear(row.get('iyr', '3000')):
            continue
        if not is_valid_expiryyear(row.get('eyr', '3000')):
            continue

        hgt = row.get('hgt', '10000in')
        if not is_valid_height(hgt):
            continue
        
        hcl = row.get('hcl', '000')
        if not is_valid_haircolor(hcl):
            continue
        
        if not is_valid_eyecolor(row.get('ecl', 'ABC')):
            continue
        
        pid = row.get('pid', '__')
        if not is_valid_passportid(pid):
            continue

        valid += 1

    print(valid)

if __name__ == "__main__":
    main()

