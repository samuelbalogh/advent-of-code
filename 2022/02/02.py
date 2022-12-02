from typing import Text
from typing import List
from typing import Generator


def read_input_file(path: Text = 'input.txt') -> Generator:
    with open(path, 'r') as input_file:
        for line in input_file:
            yield line.strip().split()

RPS = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y',
    'X': 'C',
    'Y': 'A',
    'Z': 'B'
}


PAIRS = {'A': 'X', 'B': 'Y', 'C': 'Z'}


VALUES = {'X': 1, 'Y': 2, 'Z': 3}


def main():
    score = 0
    for opp, me in read_input_file():
        if RPS[opp] == me:
            score += VALUES[me]
        elif RPS[me] == opp:
            score += VALUES[me] + 6
        elif PAIRS[opp] == me:
            score += VALUES[me] + 3
    return score


def main_part_two():
    score = 0
    for opp, goal in read_input_file():
        if goal == 'X':
            mine = RPS[opp]
        elif goal == 'Y':
            mine = PAIRS[opp]
            score += 3
        elif goal == 'Z':
            mine = [key for key in RPS.keys() if RPS[key] == opp][0]
            score += 6
        score += VALUES[mine]
    return score


if __name__ == "__main__":
    print(main())
    print(main_part_two())
