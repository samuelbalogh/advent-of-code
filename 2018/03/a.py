def read_file(path='input'):
    with open(path) as input_file:
        for line in input_file:
            yield line.strip()

def main():
    canvas = []
    size = 1000
    for i in range(size):
        canvas.append(size * [0])

    for line in read_file():
        for char in [',', ':', 'x', '#', '@']:
            line = line.replace(char, ' ')
        line = [int(i.strip()) for i in line.strip().split()]

        right, top, width, height = line[1], line[2], line[3], line[4]

        for row in range(top, top+height):
            for col in range(right, right+width):
                canvas[row][col] += 1

    return sum([1 for sublist in canvas for item in sublist if item > 1])


print(main())
