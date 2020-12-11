import argparse

def total_sum(all_answers):
    total = 0

    for answers in all_answers:
        total += len(answers)

    return total

def init_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    return parser

def parse_group_answers(file):
    answers = []

    with open(file) as f:
        first_answer = None
        group = set()

        for line in f:
            line = line.strip()
            if line == '':
                # New group
                answers.append(group)
                group = set()
                first_answer = None
                continue

            if first_answer is None:
                first_answer = line
                group.update(line)
            else:
                group.intersection_update(line)

        answers.append(group)

    return answers

def main():
    parser = init_argparser()
    args = parser.parse_args()
    answers = parse_group_answers(args.file)
    total = total_sum(answers)
    print(total)

if __name__ == "__main__":
    main()