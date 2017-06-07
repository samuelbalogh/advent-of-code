keypad = [
          [1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]
         ]

directions = {
            'D': [1, 0],
            'L': [0, -1],
            'U': [-1, 0],
            'R': [0, 1]
}

def get_button(step, start=(1,1)):
    try:
        keypad[start[0] + directions[step][0]][start[1] + directions[step][1]]
        if start[0] + directions[step][0] == -1 or start[1] + directions[step][1] == -1:
            return (start[0], start[1])
        return (start[0] + directions[step][0], start[1] + directions[step][1])
    except IndexError:
        return (start[0], start[1])

def get_button_from_lots_of_steps(steps, start=(1,1)):
    current_button = start
    for i in range(len(steps)):
        current_button = get_button(steps[i], current_button)
    return current_button[0], current_button[1]

def solve_for_multiple_lines(path):
    with open(path, 'r') as instructions:
        result = []
        current_button = (1,1)
        for line in instructions.readlines():
            line = line.strip()
            current_button = get_button_from_lots_of_steps(line, start=current_button)
            result.append(keypad[current_button[0]][current_button[1]])
        print(''.join([str(i) for i in result]))

""" Part two """

keypad =  [
      [ '', '' , 1 , '' , '' ],
      [ '' , 2 , 3 , 4 , '' ],
      [ 5 , 6 , 7 , 8 , 9 ],
      ['', 'A', 'B', 'C', ''],
      ['' , '' , 'D' , '' , '']
        ]


directions = {
            'D': [1, 0],
            'L': [0, -1],
            'U': [-1, 0],
            'R': [0, 1]
}

def get_button(step, start=(2,0)):
    try:
        keypad[start[0] + directions[step][0]][start[1] + directions[step][1]]
        if start[0] + directions[step][0] == -1 or start[1] + directions[step][1] == -1:
            return (start[0], start[1])
        if keypad[start[0] + directions[step][0]][start[1] + directions[step][1]]:
            return (start[0] + directions[step][0], start[1] + directions[step][1])
        else:
            return (start[0], start[1])
    except IndexError:
        print('IndexError at ', step, start)
        return (start[0], start[1])

def get_button_from_lots_of_steps(steps, start=(2,0)):
    current_button = start
    for i in range(len(steps)):
        current_button = get_button(steps[i], current_button)
    return (current_button[0], current_button[1])

def solve_for_multiple_lines(path):
    with open(path, 'r') as instructions:
        result = []
        current_button = (2,0)
        for line in instructions.readlines():
            line = line.strip()
            current_button = get_button_from_lots_of_steps(line, start=current_button)
            result.append(keypad[current_button[0]][current_button[1]])
        print(''.join([str(i) for i in result]))

solve_for_multiple_lines('input')
