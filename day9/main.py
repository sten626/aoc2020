import argparse
import math

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

def find_invalid_number(numbers, preamble_size):
    for i in range(preamble_size, len(numbers)):
        the_number = numbers[i]
        if not is_valid(the_number, numbers[i-preamble_size:i]):
            return the_number
    
    raise RuntimeError('No invalid number found.')

def find_contiguous_seq_with_sum(numbers, target_sum):
    # Look for sequence between i and j.
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            seq = numbers[i:j]
            seq_sum = sum(seq)

            if seq_sum == target_sum:
                return seq
            if seq_sum > target_sum:
                break

    raise RuntimeError('No contiguous sequence found.')

def find_min_and_max_in_list(numbers):
    min = math.inf
    max = 0

    for number in numbers:
        if number < min:
            min = number
        
        if number > max:
            max = number

    return min, max

argparser = init_argparser()
args = argparser.parse_args()
numbers = parse_numbers(args.file)
invalid_number = find_invalid_number(numbers, args.preamble)
print('Invalid number is {}'.format(invalid_number))
seq = find_contiguous_seq_with_sum(numbers, invalid_number)
print('Sequence is {}'.format(seq))
min, max = find_min_and_max_in_list(seq)
print('Min: {}, Max: {}'.format(min, max))
print('Sum is {}'.format(min + max))
