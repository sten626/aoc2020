import argparse
import re

CHILD_REGEX = re.compile(r'^(\d+) (.+) bags*$')

def init_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('target')
    return parser

def can_contain_type(bag_type, target_type, graph):
    if bag_type == target_type:
        return False

    if not graph[bag_type]:
        return False

    if target_type in graph[bag_type]:
        return True

    for child_type in graph[bag_type]:
        found = can_contain_type(child_type, target_type, graph)
        if found:
            return True

    return False

def count_bags_containing_target(target_type, graph):
    bags_containing_target = set()

    for bag_type in graph:
        if bag_type == target_type:
            continue

        if can_contain_type(bag_type, target_type, graph):
            bags_containing_target.add(bag_type)

    return len(bags_containing_target)

def count_total_bags_inside_target(target_type, graph):
    if not graph[target_type]:
        return 0

    count = 0
    children_dict = graph[target_type]

    for child_type, child_count in children_dict.items():
        count += child_count + child_count * count_total_bags_inside_target(child_type, graph)

    return count

def parse_rules(file):
    graph = {}

    with open(file) as f:
        for line in f:
            contain_split = line.strip().split(' contain ')
            node = contain_split[0][:-5]
            graph[node] = {}
            children = contain_split[1].strip('.').split(', ')
            for child in children:
                if child == 'no other bags':
                    continue

                match = CHILD_REGEX.match(child)
                amount = int(match.group(1))
                bag_type = match.group(2)
                graph[node][bag_type] = amount

    return graph

def main():
    parser = init_argparser()
    args = parser.parse_args()
    graph = parse_rules(args.file)
    total = count_total_bags_inside_target(args.target, graph)
    print(total)

if __name__ == "__main__":
    main()