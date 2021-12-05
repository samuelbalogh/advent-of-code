from typing import Text
from typing import List
from typing import Generator


def read_input_file(path: Text) -> Generator:
    with open(path, 'r') as input_file:
        for line in input_file:
            yield line.strip()


def main():
    x, y = 0, 0
    instructions = {
        'forward': lambda value, x, y: (x, y+value),
        'down': lambda value, x, y: (x-value, y),
        'up': lambda value, x, y: (x+value, y)
    }
    for instruction in read_input_file('input.txt'):
        direction, value = instruction.split(' ')
        x, y = instructions[direction](int(value), x, y)

    print(x * y)



def main_part_two():
    x, y, aim = 0, 0,0 
    instructions = {
        'forward': lambda value, x, y, aim: (x + value, y + (aim*value), aim),
        'down': lambda value, x, y, aim: (x, y, aim-value),
        'up': lambda value, x, y, aim: (x, y, aim+value)
    }
    for instruction in read_input_file('input.txt'):
        direction, value = instruction.split(' ')
        x, y, aim = instructions[direction](int(value), x, y, aim)

        print(x, y, aim)

    print(x * y)




if __name__ == "__main__":
    # main()
    main_part_two()
