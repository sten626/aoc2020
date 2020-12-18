import argparse

def init_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('steps', type=int, nargs='*')
    return parser

def parse_map(file):
    map = []

    with open(file) as f:
        for line in f:
            map.append(line.strip())

    return map

def traverse(map, x_step, y_step):
    max_x = len(map[0])
    total_y = len(map)
    cur_x = x_step
    cur_y = y_step
    open = 0
    trees = 0

    while cur_y < total_y:
        if cur_x >= max_x:
            cur_x -= max_x

        cur = map[cur_y][cur_x]

        if cur == '.':
            open += 1
        elif cur == '#':
            trees += 1

        cur_x += x_step
        cur_y += y_step
    
    return open, trees

def main():
    parser = init_parser()
    args = parser.parse_args()
    map = parse_map(args.file)
    tree_product = 1

    while len(args.steps) >= 2:
        x_step = args.steps.pop(0)
        y_step = args.steps.pop(0)
        open, trees = traverse(map, x_step, y_step)
        print('{} open spaces and {} trees'.format(open, trees))
        tree_product *= trees

    print(tree_product)

if __name__ == "__main__":
    main()
