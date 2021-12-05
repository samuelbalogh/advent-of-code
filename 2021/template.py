from typing import Text
from typing import List
from typing import Generator


def read_input_file(path: Text) -> Generator:
    with open(path, 'r') as input_file:
        for line in input_file:
            yield int(line.strip())


def main():
    pass

def main_part_two():
    pass


if __name__ == "__main__":
    main()
    main_part_two()
