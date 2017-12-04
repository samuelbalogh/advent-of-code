class CircularList(list):
    def __getitem__(self, index):
        return list.__getitem__(self, index) if index < len(self) else list.__getitem__(self, index % len(self))

def get_sum(sequence):
    summa = 0
    for index, digit in enumerate(sequence):
        if digit == sequence[index+len(sequence)//2]:
            summa += int(digit)
    return summa

with open('input.txt', 'r') as input_file:
    sequence = CircularList(input_file.read().strip())

print(get_sum(sequence))
