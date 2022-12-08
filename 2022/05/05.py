from typing import Text
from typing import List
from typing import Generator
from collections import deque


def read_input_file(path: Text = 'input.txt') -> Generator:
    with open(path, 'r') as input_file:
        for line in input_file:
            yield line


def process_stacks():
    stacks: List[deque[str]] = [deque() for _ in range(10)]
    for line in read_input_file():
        if line.startswith(' 1'):
            return [deque([item.strip() for item in stack if item]) for stack in stacks]

        for index, item in enumerate(line.replace('    ', ' ').split(' ')):
            stacks[index].append(item)


def main():
    stacks = process_stacks()
    for line in read_input_file():
        if line.startswith('move'):
            quantity, origin, destination = [
                int(item.strip()) for item in line.split(' ') if item.strip().isdigit()
            ]
            for _ in range(quantity):
                item = stacks[origin-1].popleft()
                stacks[destination-1].appendleft(item)

    print("".join([stack.popleft().strip(']').strip('[') for stack in stacks if stack]))


def main_part_two():
    stacks = process_stacks()
    for line in read_input_file():
        if line.startswith('move'):
            quantity, origin, destination = [
                int(item.strip()) for item in line.split(' ') if item.strip().isdigit()
            ]
            popped = []
            for _ in range(quantity):
                popped.append(stacks[origin-1].popleft())

            for item in popped[::-1]:
                stacks[destination-1].appendleft(item)

    print("".join([stack.popleft().strip(']').strip('[') for stack in stacks if stack]))


if __name__ == "__main__":
    main()
    main_part_two()
