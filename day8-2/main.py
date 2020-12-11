import argparse

def init_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    return parser

def parse_program(file):
    program = []

    with open(file) as f:
        for line in f:
            split_line = line.strip().split(' ')
            program.append((split_line[0], int(split_line[1])))

    return program

def executeInstruction(inst, val, cursor, accumulator):
    if inst == 'acc':
        accumulator += val
        cursor += 1
    elif inst == 'jmp':
        cursor += val
    elif inst == 'nop':
        cursor += 1
    else:
        raise RuntimeError('Invalid instruction')

    return cursor, accumulator

program = parse_program('input.txt')
cursor = 0
accumulator = 0
seen_cursors = set()
maybe_bad_cursor_and_accums = []

while True:
    # Main loop. Halt when hit infinite loop.
    if cursor in seen_cursors:
        break

    seen_cursors.add(cursor)
    inst, val = program[cursor]

    if inst in {'jmp', 'nop'}:
        maybe_bad_cursor_and_accums.append((cursor, accumulator))

    cursor, accumulator = executeInstruction(inst, val, cursor, accumulator)

target_cursor = len(program)

while maybe_bad_cursor_and_accums:
    seen_cursors = set()
    cursor, accumulator = maybe_bad_cursor_and_accums.pop()
    inst, val = program[cursor]

    if inst == 'jmp':
        inst = 'nop'
    else:
        inst = 'jmp'

    seen_cursors.add(cursor)
    cursor, accumulator = executeInstruction(inst, val, cursor, accumulator)
    success = False
    
    while True:
        if cursor == target_cursor:
            success = True
            break
        if cursor in seen_cursors:
            break

        seen_cursors.add(cursor)
        inst, val = program[cursor]
        cursor, accumulator = executeInstruction(inst, val, cursor, accumulator)

    if success:
        print('Accumulator is {}'.format(accumulator))
        break
