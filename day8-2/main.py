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

def executeInstruction(program, cursor, past_cursors, end):
    if cursor == end:
        return True
    if cursor in past_cursors:
        return False

    global accumulator
    new_past_cursors = set(past_cursors)
    new_past_cursors.add(cursor)
    line = program[cursor]
    inst = line[0]
    val = line[1]

    if inst == 'acc':
        accumulator += val
        cursor += 1
    elif inst == 'jmp':
        cursor += val
    elif inst == 'nop':
        cursor += 1
    else:
        raise RuntimeError('Invalid instruction')

    result = executeInstruction(program, cursor, new_past_cursors, end)

    if result:
        return result

    if inst == 'acc':
        accumulator -= val
        return False
    elif inst == 'jmp':
        # Try nop instead
        cursor = cursor - val + 1
    elif inst == 'nop':
        # Try jmp instead
        cursor = cursor - 1 + val

    return executeInstruction(program, cursor, new_past_cursors, end)

def main():
    parser = init_argparser()
    args = parser.parse_args()
    program = parse_program(args.file)
    
    executeInstruction(program, 0, set(), len(program))
    print('Accumulator is {}'.format(accumulator))
    
if __name__ == "__main__":
    main()