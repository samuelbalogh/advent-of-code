from helpers import read_input

## PART 1

def main():
    summa = 0
    for line in read_input('01/input.txt'):
        num = int(line) // 3 - 2
        summa += num
    return summa

## PART 2

def main2():
    summa = 0
    for line in read_input('01/input.txt'):
        fuel = int(line)
        while fuel > 0:
            fuel = max(int(fuel) // 3 - 2, 0)
            summa += fuel
    return summa


if __name__ == "__main__":
    print(main2())
