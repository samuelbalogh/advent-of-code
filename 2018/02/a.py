def read_file(path="input"):
    with open(path) as input_file:
        for line in input_file:
            yield line


def main():
    twice = 0
    thrice = 0
    for line in read_file():
        frequency = set({letter: line.count(letter) for letter in line}.values())
        if 2 in frequency:
            twice += 1
        if 3 in frequency:
            thrice += 1
    return twice * thrice


print(main())
