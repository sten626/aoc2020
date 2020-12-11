import argparse

def init_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    return parser

accumulator = 0

def parse_program(file):
    program = []

    with open(file) as f:
        for line in f:
            split_line = line.strip().split(' ')
            program.append((split_line[0], int(split_line[1])))

    return program

def executeInstruction(program, cursor):
    line = program[cursor]
    inst = line[0]
    val = line[1]

    if inst == 'acc':
        global accumulator
        accumulator += val
        return cursor + 1
    if inst == 'jmp':
        return cursor + val
    if inst == 'nop':
        return cursor + 1

    raise RuntimeError('Invalid instruction')

def main():
    parser = init_argparser()
    args = parser.parse_args()
    program = parse_program(args.file)
    cursor = 0
    ran_insts = set()
    
    while True:
        if cursor in ran_insts:
            print('Accumulator is {}'.format(accumulator))
            break
        
        ran_insts.add(cursor)
        cursor = executeInstruction(program, cursor)

if __name__ == "__main__":
    main()