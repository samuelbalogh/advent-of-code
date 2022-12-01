from typing import Text
from typing import List
from typing import Generator


def read_input_file(path: Text = "input.txt") -> Generator:
    with open(path, 'r') as input_file:
        for line in input_file:
            yield int(line.strip()) if line.strip() else ''


def main() -> int:
    elves: List[int] = []
    cal_for_current_elf = 0
    for line in read_input_file():
        if not line: 
            elves.append(cal_for_current_elf)
            cal_for_current_elf = 0
            continue
        cal_for_current_elf += int(line)
    elves.append(cal_for_current_elf)
    return max(elves)

def main_part_two():
    elves: List[int] = []
    cal_for_current_elf = 0
    for line in read_input_file():
        if not line: 
            elves.append(cal_for_current_elf)
            cal_for_current_elf = 0
            continue
        cal_for_current_elf += int(line)
    elves.append(cal_for_current_elf)
    return sum(sorted(elves)[-3:])


if __name__ == "__main__":
    assert main() == 68802
    assert main_part_two() == 205370
