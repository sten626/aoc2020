import argparse

def init_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    return parser

def parse_passes(file):
    passes = []

    with open(file) as f:
        for line in f:
            passes.append(line.strip())

    return passes

def process_passes(passes):
    # Return a dict of ID to (row, col)
    processed = {}

    for b_pass in passes:
        min_row = 0
        max_row = 127
        min_col = 0
        max_col = 7

        for letter in b_pass:
            if letter == 'F':
                max_row -= (max_row - min_row + 1) // 2
            elif letter == 'B':
                min_row += (max_row - min_row + 1) // 2
            elif letter == 'L':
                max_col -= (max_col - min_col + 1) // 2
            elif letter == 'R':
                min_col += (max_col - min_col + 1) // 2

        assert min_row == max_row
        assert min_col == max_col

        pass_id = min_row * 8 + min_col
        processed[pass_id] = (min_row, min_col)
        # print('row {}, column {}, seat ID {}.'.format(min_row, min_col, pass_id))

    return processed

def main():
    parser = init_argparser()
    args = parser.parse_args()
    passes = parse_passes(args.file)
    pass_info = process_passes(passes)
    sorted_ids = sorted(pass_info)
    missing_ids = []  # with IDs -1/+1 present

    for i, cur_id in enumerate(sorted_ids):
        if i == 0:
            continue

        if cur_id - 2 == sorted_ids[i - 1]:
            missing_ids.append(cur_id - 1)

    print(missing_ids)

if __name__ == "__main__":
    main()