from collections import defaultdict

from helpers import read_input, read_chars

wire1, wire2 = [list(read_chars(line)) for line in read_input("03/input.txt")]

test_wire1 = ["R8", "U5", "L5", "D3"]
test_wire2 = ["U7", "R6", "D4", "L4"]

test_wire3 = ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"]
test_wire4 = ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"]

test_wire5 = [
    "R98",
    "U47",
    "R26",
    "D63",
    "R33",
    "U87",
    "L62",
    "D20",
    "R33",
    "U53",
    "R51",
]
test_wire6 = ["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"]

OPS = {"R": "x + 1, y", "L": "x - 1, y", "D": "x, y - 1", "U": "x, y + 1"}


WIRE_PATHS = defaultdict(dict)


def get_all_coordinates(wire, name=None):
    x, y = 0, 0
    n_steps = 0
    for instruction in wire:
        direction = instruction[0]
        distance = int(instruction[1:])

        for _ in range(distance):
            x, y = eval(OPS[direction])
    
            # For Part 2: keep track of how many steps we needed to get there
            n_steps += 1
            if (x, y) not in WIRE_PATHS[name]:
                WIRE_PATHS[name][x, y] = n_steps

            yield x, y


def get_intersections(wire1, wire2):
    set1 = set(get_all_coordinates(wire1, 1))
    set2 = set(get_all_coordinates(wire2, 2))
    return set1.intersection(set2)


def get_closest_intersection(intersections):
    distances = [sum(abs(i) for i in coords) for coords in intersections]
    return min(distances)

interxs = get_intersections(wire1, wire2)
print(get_closest_intersection(interxs))


## PART 2

def get_intersection_with_fewest_steps(intersections):
    fewest = 100000000
    for coords in intersections:
        wire1_steps = WIRE_PATHS[1][coords]
        wire2_steps = WIRE_PATHS[2][coords]
        if wire1_steps + wire2_steps < fewest:
            fewest = wire1_steps + wire2_steps

    return fewest



print(get_intersection_with_fewest_steps(interxs))
