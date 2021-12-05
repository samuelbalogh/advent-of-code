from typing import Text
from typing import List
from typing import Generator
from typing import Callable


def read_input_file(path: Text) -> Generator:
    with open(path, 'r') as input_file:
        for line in input_file:
            yield line.strip()


def main():
    bit_sums = None
    array_length = 0
    for line in read_input_file('input.txt'):
        if not bit_sums:
            bit_sums = [0] * len(line)

        array_length += 1
        for index, item in enumerate(line):
            bit_sums[index] += int(item)

    gamma = ''
    epsilon = ''
    for item in bit_sums:
        most_common = int(item > array_length//2)
        least_common = int(not most_common)
        gamma += str(most_common)
        epsilon += str(least_common)

    print(int(gamma, 2) * int(epsilon, 2))


def find_most_common_bits(dataset: List[Text]) -> List[int]:
    bit_sums = None
    array_length = 0
    for line in dataset:
        if not bit_sums:
            bit_sums = [0] * len(line)

        array_length += 1
        for index, item in enumerate(line):
            bit_sums[index] += int(item)

    most_common_bits = [0] * len(line)
    for index, item in enumerate(bit_sums):
        most_common = int(item > array_length//2)
        if item == array_length//2:
            most_common_bits[index] = None
            continue

        most_common_bits[index] = most_common

    return most_common_bits


def main_part_two():
    dataset = [line for line in read_input_file('test_input.txt')]
    most_common_bit_map = find_most_common_bits(dataset)
    breakpoint()
    res = filter_lines(dataset, filter_for_o2, most_common_bit_map)
    
    

def filter_lines(dataset, filter_func, most_common_bit_map):
    for index in range(int(dataset[0])):
        most_common_bit_map = find_most_common_bits(dataset)
        most_common_bit = most_common_bit_map[index]
        dataset = filter_current_lines(dataset, index, most_common_bit, filter_func=filter_func)
        if len(dataset) == 1:
            return dataset[0]


def filter_current_lines(lines: List[Text], index: int, most_common_bit: int, filter_func: Callable):
    filtered_lines = lines[:]
    for line in lines:
        if filter_func(int(line[index]), most_common_bit):
            filtered_lines.remove(line)
    return filtered_lines


def filter_for_o2(bit: int, most_common_bit: int):
    if bit == most_common_bit:
        return False
    if most_common_bit is None and bit == 1:
        return False
    else:
        return True

def filter_for_co2(bit: int, most_common_bit: int):
    if most_common_bit == bit:
        return True
    if most_common_bit is None and bit == 1:
        return True
    return False


if __name__ == "__main__":
    main_part_two()
