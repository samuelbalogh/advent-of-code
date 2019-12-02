import random

def read_file(path='input'):
    with open(path) as input_file:
        return input_file.read()


def are_opposites(a, b):
    return (a.islower() and b.isupper()) or (a.isupper() and b.islower())


def will_react(a, b):
    return True if (are_opposites(a, b) and a.lower() == b.lower()) else False


def can_further_react(segment):
    for i, item in enumerate(segment[:-1]):
        if will_react(segment[i], segment[i+1]):
            return True
    return False


def react_segment(segment):
    if not can_further_react(segment):
        return segment
    for index, item in enumerate(segment):
        a, b = segment[index:index+2]
        if will_react(a, b):
            return react_segment(segment[:index] + segment[index+2:])


def slice_up(segment, length_of_slices=100):
    length = len(segment)
    if length <= length_of_slices:
        return [segment]
    slices = []
    for i in range(0, length, length_of_slices):
        slice_ = segment[i:i+length_of_slices]
        slices.append(slice_)

    return slices

def main():
    segment = read_file().strip()

    while can_further_react(segment):
        slices = slice_up(segment, length_of_slices=random.randint(70, 140))
        new_slices = []
        for slc in slices:
            new_slice = react_segment(slc)
            new_slices.append(new_slice)
        segment = ''.join(new_slices)


    print(len(segment))
    return segment



print(main())
