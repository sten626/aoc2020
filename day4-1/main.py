import argparse

REQUIRED_FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

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
        if not REQUIRED_FIELDS.difference(passport):
            num_valid += 1

    return num_valid

def main():
    parser = init_argparser()
    args = parser.parse_args()
    passports = parse_passports(args.file)
    num_valid = validate_passports(passports)
    print('{} valid passports'.format(num_valid))

if __name__ == "__main__":
    main()
