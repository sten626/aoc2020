import argparse
from collections import defaultdict

def init_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    return parser

def parse_adapters(file):
    adapters = []

    with open(file) as f:
        for line in f:
            adapters.append(int(line))
    
    return sorted(adapters)

def chain_adapters(adapters):
    current_jolts = 0
    jolt_diffs = defaultdict(int)

    for adapter in adapters:
        diff = adapter - current_jolts
        if 1 <= diff <= 3:
            current_jolts = adapter
            jolt_diffs[diff] += 1

    current_jolts += 3
    jolt_diffs[3] += 1

    return current_jolts, jolt_diffs

def one_jolt_times_three_jolts(jolt_diffs):
    return jolt_diffs[1] * jolt_diffs[3]

def build_graph(sorted_adapters):
    graph = {
        0: set()
    }

    for i, adapter in enumerate(sorted_adapters):
        if 1 <= adapter <= 3:
            graph[0].add(adapter)

        graph[adapter] = set()

        for j in range(i + 1, len(sorted_adapters)):
            next_adapter = sorted_adapters[j]
            if 1 <= next_adapter - adapter <= 3:
                graph[adapter].add(next_adapter)
            else:
                break
    
    return graph

memoized_paths = {}

def count_paths(graph, cur_adapter):
    try:
        return memoized_paths[cur_adapter]
    except KeyError:
        pass

    if len(graph[cur_adapter]) == 0:
        # End of path
        return 1

    count = 0

    for child_adapter in graph[cur_adapter]:
        count += count_paths(graph, child_adapter)

    memoized_paths[cur_adapter] = count
    return count

argparser = init_argparser()
args = argparser.parse_args()
adapters = parse_adapters(args.file)
graph = build_graph(adapters)
total_paths = count_paths(graph, 0)
print('{} total paths.'.format(total_paths))
