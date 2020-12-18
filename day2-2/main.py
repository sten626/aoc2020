import argparse
import re

LINE_REGEX = re.compile('(\d+)-(\d+)\s([a-z]):\s(\w+)')

def init_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    return parser

def parse_line(line):
    match = LINE_REGEX.match(line)
    min_occurances = int(match.group(1))
    max_occurances = int(match.group(2))
    target_letter = match.group(3)
    password = match.group(4)

    return min_occurances, max_occurances, target_letter, password

def validate_line(line):
    min, max, target_letter, password = parse_line(line)
    occurances = len(password.split(target_letter)) - 1

    return min <= occurances <= max

def validate_line2(line):
    pos1, pos2, target_letter, password = parse_line(line)
    found = 0

    if password[pos1 - 1] == target_letter:
        found += 1
    if password[pos2 - 1] == target_letter:
        found += 1

    return found == 1

def main():
    parser = init_parser()
    args = parser.parse_args()
    filename = args.file
    
    valid_passwords = 0
    invalid_passwords = 0

    with open(filename) as f:
        for line in f:
            valid = validate_line2(line)

            if valid:
                valid_passwords += 1
            else:
                invalid_passwords += 1

    print('{} valid passwords'.format(valid_passwords))
    print('{} invalid passwords'.format(invalid_passwords))

if __name__ == "__main__":
    main()
