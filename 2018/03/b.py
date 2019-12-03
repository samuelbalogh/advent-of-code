def read_file(path="input"):
    with open(path) as input_file:
        for line in input_file:
            yield line.strip()


def main():
    canvas = []
    size = 1000

    for i in range(size):
        canvas.append(size * [0])

    squares = []

    for line in read_file():
        for char in [",", ":", "x", "#", "@"]:
            line = line.replace(char, " ")
        line = [int(i.strip()) for i in line.strip().split()]

        id_, right, top, width, height = line[0], line[1], line[2], line[3], line[4]

        squares.append([id_, right, top, width, height])

        for row in range(top, top + height):
            for col in range(right, right + width):
                canvas[row][col] += 1

    for square in squares:
        id_, right, top, width, height = (
            square[0],
            square[1],
            square[2],
            square[3],
            square[4],
        )
        only_ones = True
        for row in range(top, top + height):
            for col in range(right, right + width):
                if canvas[row][col] != 1:
                    only_ones = False
        if only_ones:
            return id_


print(main())
