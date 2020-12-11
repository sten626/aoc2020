import argparse

def init_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('preamble', type=int)
    return parser

def parse_numbers(file):
    numbers = []

    with open(file) as f:
        for line in f:
            numbers.append(int(line))

    return numbers

def is_valid(number, prev_numbers):
    for i in range(len(prev_numbers)):
        if prev_numbers[i] >= number:
            continue
        for j in range(i + 1, len(prev_numbers)):
            if prev_numbers[i] + prev_numbers[j] == number:
                return True

    return False

argparser = init_argparser()
args = argparser.parse_args()
numbers = parse_numbers(args.file)
preamble_size = args.preamble

for i in range(preamble_size, len(numbers)):
    the_number = numbers[i]
    if not is_valid(the_number, numbers[i-preamble_size:i]):
        print('{} is the first invalid number'.format(the_number))
        break
else:
    print('failed')