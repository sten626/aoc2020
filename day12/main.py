import argparse
import re

INSTRUCTION_REGEX = re.compile(r'^([NSEWLRF])(\d+)$')
DIRECTIONS = ['N', 'E', 'S', 'W']

def init_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    return parser

def parse_instructions(file):
    instructions = []

    with open(file) as f:
        for line in f:
            match = INSTRUCTION_REGEX.match(line)
            inst = match.group(1)
            val = int(match.group(2))
            instructions.append((inst, val))
    
    return instructions

def process_instruction(instruction, ship_dir, ship_pos):
    inst, val = instruction
    x, y = ship_pos

    if inst == 'F':
        inst = ship_dir

    if inst == 'N':
        y += val
    elif inst == 'S':
        y -= val
    elif inst == 'E':
        x += val
    elif inst == 'W':
        x -= val
    elif inst == 'L':
        ship_dir = process_turn(ship_dir, -val)
    elif inst == 'R':
        ship_dir = process_turn(ship_dir, val)

    return ship_dir, (x, y)

def process_turn(ship_dir, degrees):
    cur_i = DIRECTIONS.index(ship_dir)
    increment = int(degrees / 360 * 4)
    new_i = (cur_i + increment) % 4
    return DIRECTIONS[new_i]

def get_manhattan_distance(ship_pos):
    return abs(ship_pos[0]) + abs(ship_pos[1])

argparser = init_argparser()
args = argparser.parse_args()
instructions = parse_instructions(args.file)
ship_dir = 'E'
ship_pos = 0, 0

for instruction in instructions:
    ship_dir, ship_pos = process_instruction(instruction, ship_dir, ship_pos)
    print(ship_dir, ship_pos)

manhattan_distance = get_manhattan_distance(ship_pos)
print('Manhattan distance is: {}'.format(manhattan_distance))