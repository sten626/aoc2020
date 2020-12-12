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

def process_instruction(instruction, ship_pos, waypoint):
    inst, val = instruction
    # x, y = ship_pos

    if inst == 'F':
        x, y = ship_pos
        x += waypoint[0] * val
        y += waypoint[1] * val
        ship_pos = x, y
    elif inst == 'N':
        # y += val
        x, y = waypoint
        y += val
        waypoint = x, y
    elif inst == 'S':
        # y -= val
        x, y = waypoint
        y -= val
        waypoint = x, y
    elif inst == 'E':
        # x += val
        x, y = waypoint
        x += val
        waypoint = x, y
    elif inst == 'W':
        # x -= val
        x, y = waypoint
        x -= val
        waypoint = x, y
    elif inst == 'L':
        waypoint = process_turn(waypoint, -val)
    elif inst == 'R':
        waypoint = process_turn(waypoint, val)

    return ship_pos, waypoint

def process_turn(waypoint, degrees):
    x, y = waypoint

    if abs(degrees) == 180:
        return -x, -y
    if degrees == 90 or degrees == -270:
        # 2, 1 -> 1, -2
        return y, -x
    if degrees == -90 or degrees == 270:
        # 2, 1 -> -1, 2
        return -y, x

    raise RuntimeError('Other degrees {}'.format(degrees))

def get_manhattan_distance(ship_pos):
    return abs(ship_pos[0]) + abs(ship_pos[1])

argparser = init_argparser()
args = argparser.parse_args()
instructions = parse_instructions(args.file)
# ship_dir = 'E'
ship_pos = 0, 0
waypoint = 10, 1

for instruction in instructions:
    ship_pos, waypoint = process_instruction(instruction, ship_pos, waypoint)

manhattan_distance = get_manhattan_distance(ship_pos)
print('Manhattan distance is: {}'.format(manhattan_distance))