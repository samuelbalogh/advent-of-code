from itertools import count
from collections import deque
from copy import deepcopy


def count_lit_pixels(screen):
    return sum(
        [
            1 if elem == "#" else 0
            for elem in [elem for sublist in screen for elem in sublist]
        ]
    )


def rect(columns, rows, screen):
    for row_index in range(len(screen[:rows])):
        screen[row_index] = ["#"] * columns + screen[row_index][columns:]


def rotate_row(row, shift_by, screen):
    d = deque(screen[row][:])
    d.rotate(shift_by)
    screen[row] = list(d)


def rotate_column(column, shift_by, screen):
    column_to_shift = [row[column] for row in screen][:]
    d = deque(column_to_shift)
    d.rotate(shift_by)
    shifted_column = list(d)
    index = 0
    new_row = [" "] * len(screen[0])
    for item in shifted_column:
        new_row[:column] = screen[index][:][:column][:]
        new_row[column] = item
        new_row[column + 1 :] = screen[index][:][column + 1 :][:]
        screen[index] = new_row[:]
        index += 1


def lcd_display(width, height, commands):
    screen = [[" "] * width] * height
    with open(commands, "r") as data:
        for _ in count():
            try:
                line = next(data)
                if "rect" in line:
                    columns = int(line.strip("rect ").split("x")[0])
                    rows = int(line.strip("rect ").split("x")[1])
                    rect(columns, rows, screen)
                elif "rotate row y" in line:
                    row = int(line.strip("rotate row y= \n").split(" by ")[0])
                    shift_by = int(line.strip("rotate row y= \n").split(" by ")[1])
                    rotate_row(row, shift_by, screen)
                elif "rotate column x" in line:
                    column, shift_by = [
                        int(i) for i in line.strip("rotate column x= \n").split(" by ")
                    ]
                    rotate_column(column, shift_by, screen)
            except StopIteration:
                for row in screen:
                    print(row)
                return screen


screen = lcd_display(50, 6, "input")
print(count_lit_pixels(screen))
