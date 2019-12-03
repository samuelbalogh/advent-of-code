def read_file(path="input"):
    with open(path) as input_file:
        for line in input_file:
            yield line


def main():
    last_summa = 0
    been_there = set()
    values = [int(line) for line in read_file()]
    while True:
        for value in values:
            new_summa = last_summa + value
            last_summa = new_summa
            if new_summa in been_there:
                return new_summa
            been_there.add(new_summa)


print(main())
