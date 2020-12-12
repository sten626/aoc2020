import argparse

def init_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    return parser

def parse_layout(file):
    layout = []

    with open(file) as f:
        for line in f:
            layout.append(line.strip())
    
    return layout

def no_adjacent_occupied_seats(layout, row_i, col_i):
    min_row = max(row_i - 1, 0)
    max_row = min(row_i + 1, len(layout) - 1)
    min_col = max(col_i - 1, 0)
    max_col = min(col_i + 1, len(layout[0]) - 1)

    for row_j in range(min_row, max_row + 1):
        for col_j in range(min_col, max_col + 1):
            if row_j == row_i and col_j == col_i:
                continue

            if layout[row_j][col_j] == '#':
                return False

    return True

def four_adjacent_seats_are_occupied(layout, row_i, col_i):
    min_row = max(row_i - 1, 0)
    max_row = min(row_i + 1, len(layout) - 1)
    min_col = max(col_i - 1, 0)
    max_col = min(col_i + 1, len(layout[0]) - 1)
    occupied = 0

    for row_j in range(min_row, max_row + 1):
        for col_j in range(min_col, max_col + 1):
            if row_j == row_i and col_j == col_i:
                continue

            if layout[row_j][col_j] == '#':
                occupied += 1

    return occupied >= 4

def num_occupied_seats_in_sight(layout, row, col):
    count = 0

    # Up
    for i in range(row - 1, -1, -1):
        if layout[i][col] == '.':
            continue
        if layout[i][col] == '#':
            count += 1
        break
    
    # Down
    for i in range(row + 1, len(layout)):
        if layout[i][col] == '.':
            continue
        if layout[i][col] == '#':
            count += 1
        break

    # Left
    for i in range(col - 1, -1, -1):
        if layout[row][i] == '.':
            continue
        if layout[row][i] == '#':
            count += 1
        break

    # Right
    for i in range(col + 1, len(layout[row])):
        if layout[row][i] == '.':
            continue
        if layout[row][i] == '#':
            count += 1
        break

    # Up+Left
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if layout[i][j] == '.':
            i -= 1
            j -= 1
            continue
        if layout[i][j] == '#':
            count += 1
        break

    # Up+Right
    i = row - 1
    j = col + 1
    while i >= 0 and j < len(layout[row]):
        if layout[i][j] == '.':
            i -= 1
            j += 1
            continue
        if layout[i][j] == '#':
            count += 1
        break

    # Down+Left
    i = row + 1
    j = col - 1
    while i < len(layout) and j >= 0:
        if layout[i][j] == '.':
            i += 1
            j -= 1
            continue
        if layout[i][j] == '#':
            count += 1
        break

    # Down+Right
    i = row + 1
    j = col + 1
    while i < len(layout) and j < len(layout[row]):
        if layout[i][j] == '.':
            i += 1
            j += 1
            continue
        if layout[i][j] == '#':
            count += 1
        break

    return count

def apply_rules(layout):
    new_layout = []
    had_changes = False

    for row_i in range(len(layout)):
        column = layout[row_i]
        new_column = []
        for col_i in range(len(column)):
            seat = column[col_i]

            if seat == 'L':
                if num_occupied_seats_in_sight(layout, row_i, col_i) == 0:
                    new_column.append('#')
                    had_changes = True
                else:
                    new_column.append('L')
            elif seat == '#':
                if num_occupied_seats_in_sight(layout, row_i, col_i) >= 5:
                    new_column.append('L')
                    had_changes = True
                else:
                    new_column.append('#')
            else:
                new_column.append(seat)

        new_layout.append(new_column)

    return new_layout, had_changes

def count_occupied_seats(layout):
    total = 0

    for row in layout:
        for seat in row:
            if seat == '#':
                total += 1

    return total

argparser = init_argparser()
args = argparser.parse_args()
layout = parse_layout(args.file)

while True:
    layout, had_changes = apply_rules(layout)

    if not had_changes:
        break

total_occupied = count_occupied_seats(layout)
print('{} occupied seats'.format(total_occupied))
