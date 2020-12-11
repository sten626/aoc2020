import argparse
import re

HAIR_COLOR_REGEX = re.compile(r'^#[0-9a-f]{6}$')
HEIGHT_REGEX = re.compile(r'^(\d+)(cm|in)$')
PASSPORT_ID_REGEX = re.compile(r'^\d{9}$')
REQUIRED_FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
VALID_EYE_COLORS = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
YEAR_REGEX = re.compile(r'^\d{4}$')

def init_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    return parser

def parse_passports(file):
    passports = []

    with open(file) as f:
        passport = {}

        for line in f:
            line = line.strip()
            
            if line == '':
                # Blank line, start new passport
                passports.append(passport)
                passport = {}
                continue

            fields = line.split(' ')
            for field in fields:
                key_value = field.split(':')
                passport[key_value[0]] = key_value[1]

        if passport:
            passports.append(passport)

    return passports

def validate_passports(passports):
    num_valid = 0

    for passport in passports:
        if REQUIRED_FIELDS.difference(passport):
            continue
        if not validate_byr(passport['byr']):
            continue
        if not validate_iyr(passport['iyr']):
            continue
        if not validate_eyr(passport['eyr']):
            continue
        if not validate_hgt(passport['hgt']):
            continue
        if not validate_hcl(passport['hcl']):
            continue
        if not validate_ecl(passport['ecl']):
            continue
        if not validate_pid(passport['pid']):
            continue
        
        num_valid += 1

    return num_valid

def validate_byr(year):
    return validate_year(year, 1920, 2002)

def validate_ecl(eye_color):
    return eye_color in VALID_EYE_COLORS

def validate_eyr(year):
    return validate_year(year, 2020, 2030)

def validate_hcl(hair_color):
    if HAIR_COLOR_REGEX.match(hair_color):
        return True
    
    return False

def validate_hgt(height):
    match = HEIGHT_REGEX.match(height)

    if not match:
        return False

    value = match.group(1)
    units = match.group(2)

    if units == 'cm':
        return validate_int(value, 150, 193)
    if units == 'in':
        return validate_int(value, 59, 76)

    raise RuntimeError('Impossible error when validating height?')

def validate_iyr(year):
    return validate_year(year, 2010, 2020)

def validate_int(number, min, max):
    number = int(number)
    return min <= number <= max

def validate_pid(pid):
    if PASSPORT_ID_REGEX.match(pid):
        return True

    return False

def validate_year(year, min, max):
    return YEAR_REGEX.match(year) and validate_int(year, min, max)

def main():
    parser = init_argparser()
    args = parser.parse_args()
    passports = parse_passports(args.file)
    num_valid = validate_passports(passports)
    print('{} valid passports'.format(num_valid))

if __name__ == "__main__":
    main()
