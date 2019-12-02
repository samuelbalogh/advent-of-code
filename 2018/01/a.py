


def read_file(path='input'):
    with open(path) as input_file:
        for line in input_file:
            yield line

def main():
    return sum(int(line) for line in read_file())

print(main())
