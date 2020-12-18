import argparse
import re

MEM_COMMAND = re.compile(r'mem\[(\d+)\] = (\d+)')

def init_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    return parser

def run_program(file):
    mem = {}
    mask = ''
    with open(file) as f:
        for line in f:
            if line.startswith('mask'):
                mask = line.strip().split(' = ')[1]
                continue

            match = MEM_COMMAND.match(line.strip())
            address = int(match.group(1))
            value = int(match.group(2))
            masked = apply_mask(mask, value)
            mem[address] = masked

    return mem

def apply_mask(mask, value):
    or_mask = int(mask.replace('X', '0'), 2)
    and_mask = int(mask.replace('X', '1'), 2)
    return (value | or_mask) & and_mask

argparser = init_argparser()
args = argparser.parse_args()
mem = run_program(args.file)
print(sum(mem.values()))
