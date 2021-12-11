from typing import Text
from typing import Dict
from typing import List
from typing import Generator

from collections import defaultdict


def read_input_file(path: Text) -> Generator:
    with open(path, 'r') as input_file:
        for line in input_file:
            yield [int(n) for n in line.strip().split(',')]


def main():
    fish_stack = list(read_input_file('input.txt'))[0]
    remaining_days = 80
    while remaining_days > 0:
        fish_stack = produce_offsprings(fish_stack)
        fish_stack = decrease_counters(fish_stack)
        remaining_days -= 1
        if remaining_days % 10 == 1:
            print(remaining_days)
    print(len(fish_stack))


def decrease_counters(fish: List[int]) -> List[int]:
    return [(i-1) if i > 0 else 6 for i in fish]


def produce_offsprings(fish: List[int]) -> List[int]:
    counter = 0
    while counter < len(fish):
        fish_counter = fish[counter]
        if fish_counter == 0:
            fish.append(9)
        counter += 1
    return fish


def main_part_two():
    fish_counters_to_fish_counts_map: Dict[int, int] = defaultdict(int)
    fish_stack = list(read_input_file('input.txt'))[0]
    for fish in fish_stack:
        fish_counters_to_fish_counts_map[fish] += 1

    def produce_offsprings(fish_counters: Dict[int, int]) -> Dict[int, int]:
        if 0 in fish_counters:
            fish_counters[7] += fish_counters[0]
        return fish_counters

    def decrease_counters(fish_counters: Dict[int, int]) -> Dict[int, int]:
        counters = defaultdict(int)
        for key, value in fish_counters.items():
            counters[(key-1) if key else 8]= value
        return counters

    remaining_days = 256
    while remaining_days > 0:
        fish_counters_to_fish_counts_map = produce_offsprings(fish_counters_to_fish_counts_map)
        fish_counters_to_fish_counts_map = decrease_counters(fish_counters_to_fish_counts_map)
        remaining_days -= 1
    print(sum(fish_counters_to_fish_counts_map.values()))


if __name__ == "__main__":
    # main()
    main_part_two()
