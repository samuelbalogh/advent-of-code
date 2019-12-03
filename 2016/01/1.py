""" Part one"""

directions = {
    "N": {"L": "W", "R": "E"},
    "S": {"L": "E", "R": "W"},
    "E": {"R": "S", "L": "N"},
    "W": {"R": "N", "L": "S"},
}

"""
progress = {'N': 0, 'S': 0, 'E': 0, 'W': 0}

with open('input', 'r') as data:
    facing = 'N'
    line = data.readline()
    progress[directions[facing][line.split(',')[0][0]]] += int(line.split(',')[0][1])
    facing = directions[facing][line.split(',')[0][0]]
    for block in line.split(',')[1:]:
        facing = directions[facing][block.strip()[0]]
        progress[facing] += int(block.strip('RL '))

total_distance = abs(progress['N'] - progress['S']) + abs(progress['E'] - progress['W'])
print(abs(total_distance))
"""

""" Part two """

progress = {"N": 0, "S": 0, "E": 0, "W": 0}
positions = {}


def back_to_square_one():
    with open("input", "r") as data:
        facing = "N"
        line = data.readline()
        progress[directions[facing][line.split(",")[0][0]]] += int(
            line.split(",")[0][1]
        )
        facing = directions[facing][line.split(",")[0][0]]
        step = 0
        positions[step] = progress["N"] - progress["S"], progress["E"] - progress["W"]
        for block in line.split(",")[1:]:
            facing = directions[facing][block.strip()[0]]
            for i in range(int(block.strip("RL "))):
                step += 1
                progress[facing] += 1
                if (
                    progress["N"] - progress["S"],
                    progress["E"] - progress["W"],
                ) in positions.values():
                    total_distance = abs(progress["N"] - progress["S"]) + abs(
                        progress["E"] - progress["W"]
                    )
                    print(total_distance)
                    return total_distance
                positions[step] = (
                    progress["N"] - progress["S"],
                    progress["E"] - progress["W"],
                )
        print(positions)


back_to_square_one()
