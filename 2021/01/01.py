from typing import Text
from typing import List
from typing import Generator


def read_input_file(path: Text) -> Generator:
    with open(path, 'r') as input_file:
        for line in input_file:
            yield int(line.strip())


def main():
    measurements_larger_than_the_previous = 0
    prev = None
    for line in read_input_file('./input.txt'):
        if prev is None:
            prev = line
            continue
        if line > prev:
            measurements_larger_than_the_previous += 1
        prev = line
    print(measurements_larger_than_the_previous)


class WindowFilling(Exception):
    pass


def main_part_two():
    increases = 0
    window = [None, None, None]

    for line in read_input_file('./input.txt'):
        try:
            for index, item in enumerate(window):
                if item is None:
                    window[index] = line
                    raise WindowFilling
        except WindowFilling:
            if all(window):
                previous_measurement_window_sum = sum(window)
            continue

        def slide(window: List, next_line: int) -> List[int]:
            new_window = [0, 0, 0]
            new_window[0] = window[1]
            new_window[1] = window[2]
            new_window[2] = line
            return new_window

        window = slide(window, next_line=line)

        current_measurement_window_sum = sum(window)

        if current_measurement_window_sum > previous_measurement_window_sum:
            increases += 1

        previous_measurement_window_sum = current_measurement_window_sum

    print(increases)


if __name__ == "__main__":
    main_part_two()
