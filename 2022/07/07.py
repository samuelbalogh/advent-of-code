from typing import Text
from typing import List
from typing import Generator
from copy import deepcopy
from collections import defaultdict, deque


def read_input_file(path: Text = 'test_input.txt') -> Generator:
    with open(path, 'r') as input_file:
        for line in input_file:
            yield line.strip()


def explore_file_system():
    file_system = defaultdict(dict)
    path = []
    for line in read_input_file():
        subtree = file_system
        if line.startswith('dir'):
            directory = line.split('dir')[1].strip()
            for step in path:
                subtree = subtree[step]
            subtree[directory] = defaultdict(dict)

        elif (filesize := line.split(' ')[0]).isdigit():
            for step in path[:-1]:
                subtree = subtree[step]
            if 'files' in subtree[path[-1]]:
                subtree[path[-1]]['files'] += int(filesize)
            else:
                subtree[path[-1]]['files'] = int(filesize)

        if line.startswith('$'):
            if '$ cd ' in line:
                target = line.split('$ cd ')[1]
                if target == '..':
                    path.pop()
                else:
                    path.append(target.strip())
    return file_system


def get_total_size_of_tree(tree, total=0):
    for key, value in tree.items():
        if key == 'files':
            total += value
        else:
            total = get_total_size_of_tree(value, total)
    return total


def main():
    tree = explore_file_system()

    stack = deque([ ('/', tree) ])

    total_sum = 0
    while stack:
        node, tree = stack.popleft()

        if (dir_size := get_total_size_of_tree(tree)) < 100_000:
            total_sum += dir_size

        for item in tree:
            if item != 'files':
                stack.append( (item, tree[item]) )

    print(total_sum)

def main_part_two():
    space_required = 30000000
    total_space_available = 70000000

    tree = explore_file_system()

    total_size_on_disk = get_total_size_of_tree(tree)
    unused_space = total_space_available - total_size_on_disk
    required_purge_size = space_required - unused_space

    stack = deque([ ('/', tree) ])
    smallest = total_size_on_disk
    while stack:
        node, tree = stack.popleft()

        dir_size = get_total_size_of_tree(tree)

        if dir_size > required_purge_size:
            if dir_size < smallest:
                smallest = dir_size

        for item in tree:
            if item != 'files':
                stack.append( (item, tree[item]) )
    return smallest


if __name__ == "__main__":
    main()
    print(main_part_two())
