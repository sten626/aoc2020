import argparse
import math
from functools import reduce

def init_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    return parser

def parse_busses(file):
    timestamp = 0
    busses = []

    with open(file) as f:
        for i, line in enumerate(f):
            if i == 0:
                timestamp = int(line)
            else:
                busses.extend(int(bus_id) if bus_id != 'x' else bus_id for bus_id in line.strip().split(','))

    return timestamp, busses

def get_bus_and_offsets_list(busses):
    return [(bus_id, i) for i, bus_id in enumerate(busses) if bus_id != 'x']

def get_bus_id_of_earliest_time(timestamp, busses):
    earliest_time = math.inf
    best_bus_id = None

    for bus_id in busses:
        time = math.ceil(timestamp / bus_id) * bus_id
        if time < earliest_time:
            earliest_time = time
            best_bus_id = bus_id

    return best_bus_id, earliest_time

def mul_inv(a, b):
    if b == 1:
        return 1

    b0 = b
    x0, x1 = 0, 1

    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0

    if x1 < 0:
        x1 += b0
    
    return x1

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)

    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p

    return sum % prod

argparser = init_argparser()
args = argparser.parse_args()
_, busses = parse_busses(args.file)

n, a = [], []

for i, bus in enumerate(busses):
    if bus == 'x':
        continue
    n.append(bus)
    a.append(-i % bus)

print(chinese_remainder(n, a))

