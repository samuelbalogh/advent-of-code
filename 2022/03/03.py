from typing import Text
from typing import List
from typing import Generator

from string import ascii_lowercase as abc
from string import ascii_uppercase as ABC

PRIORITIES = abc + ABC


def read_input_file(path: Text = 'input.txt') -> Generator:
    with open(path, 'r') as input_file:
        for line in input_file:
            yield line.strip()


def main():
    sum_of_priorities = 0
    for rucksack in read_input_file():
        first_compartment, second_compartment = (
            set(rucksack[:len(rucksack)//2]), set(rucksack[len(rucksack)//2:])
        )
        common = first_compartment.intersection(second_compartment).pop()
        value = PRIORITIES.index(common) + 1
        sum_of_priorities += value
    return sum_of_priorities


def main_part_two():
    def calc_badge_value(current_group: List[str]) -> int:
        common = set.intersection(*[set(line) for line in current_group]).pop()
        value = PRIORITIES.index(common) + 1
        return value

    sum_of_priorities = 0
    current_group = []
    for rucksack in read_input_file():
        if len(current_group) < 3:
            current_group.append(rucksack)
        else:
            sum_of_priorities += calc_badge_value(current_group)
            current_group = [rucksack]
    return sum_of_priorities + calc_badge_value(current_group)


if __name__ == "__main__":
    print(main())
    print(main_part_two())
