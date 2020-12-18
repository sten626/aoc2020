import argparse
import re

def init_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    return parser

def main():
    parser = init_parser()
    args = parser.parse_args()
    filename = args.file
    line_regex = re.compile('(\d+)-(\d+)\s([a-z]):\s(\w+)')
    valid_passwords = 0
    invalid_passwords = 0

    with open(filename) as f:
        for line in f:
            match = line_regex.match(line)
            min_occurances = int(match.group(1))
            max_occurances = int(match.group(2))
            target_letter = match.group(3)
            password = match.group(4)
            occurances = len(password.split(target_letter)) - 1

            if min_occurances <= occurances <= max_occurances:
                valid_passwords += 1
            else:
                invalid_passwords += 1

    print('{} valid passwords'.format(valid_passwords))
    print('{} invalid passwords'.format(invalid_passwords))

if __name__ == "__main__":
    main()
