from typing import Text
from typing import List
from typing import Generator


def read_input_file(path: Text = 'input.txt') -> Generator:
    with open(path, 'r') as input_file:
        for line in input_file:
            yield [[int(i) for i in elf.split('-')] for elf in line.strip().split(',')]


def fully_contains(segment1: List[int], segment2: List[int]) -> bool:
    return (
        (segment1[0] >= segment2[0] and segment1[1] <= segment2[1]) or
        (segment2[0] >= segment1[0] and segment2[1] <= segment1[1])
    )


def overlaps(segment1: List[int], segment2: List[int]) -> bool:
    return (
        (segment1[1] >= segment2[0] and segment1[0] <= segment2[0]) or
        (segment2[1] >= segment1[0] and segment2[0] <= segment1[0])
    )


def main():
    count = 0
    for first_elf, second_elf in read_input_file():
        if fully_contains(first_elf, second_elf):
            count += 1
    return count

def main_part_two():
    count = 0
    for first_elf, second_elf in read_input_file():
        if overlaps(first_elf, second_elf):
            count += 1
    return count


if __name__ == "__main__":
    main()
    assert main_part_two() == 933, main_part_two()
