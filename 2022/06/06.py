from typing import Text
from typing import List
from typing import Generator


def read_input_file(path: Text = 'test_input.txt') -> Generator:
    with open(path, 'r') as input_file:
        return input_file.read()


def main():
    data = read_input_file()
    for index in range(len(data)):
        window = data[index:index+4]
        if len(set(window)) == 4:
            return index + 4


def main_part_two():
    data = read_input_file()
    for index in range(len(data)):
        window = data[index:index+14]
        if len(set(window)) == 14:
            return index + 14


if __name__ == "__main__":
    print(main())
    print(main_part_two())
