directions = {
              'N':
                  {'L': 'W',
                   'R': 'E'
                   },
              'S':
                  {'L': 'E',
                   'R': 'W'
                   },
              'E':
                  {'R': 'S',
                   'L': 'N'
                   },
              'W':
                  {'R': 'N',
                   'L': 'S'
                   },
                  }

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
print abs(total_distance)
