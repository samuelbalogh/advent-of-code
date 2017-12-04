from copy import deepcopy
favorite = 10

def parity_of(integer):
    parity = 0
    while integer:
        parity = ~parity
        integer = integer & (integer - 1)
    return parity

def decide_if_wall_or_space(x, y, favorite):
    sum_of_products = x*x + 3*x + 2*x*y + y + y*y
    sum_of_products += favorite
    if parity_of(sum_of_products): # parity is -1, odd, its a wall
        return '#'
    else:
        return '.'

def create_maze(favorite):
    maze = [[decide_if_wall_or_space(x,y, favorite) for x in range(favorite)] for y in range(favorite)]
    for i in range(favorite):
        print(i, ' ', ' '.join(maze[i][:favorite]))
    return maze


def walk_through_maze(maze):
    '''- at crossroads:
            save coordiates and try one of the possible ways
       - not at crossroads (only one way to move forward):
            move
        '''

grid = create_maze(10)
steps = 0
copygrid = deepcopy(grid)


def search(x, y):
    print('---')
    for i in range(10):
        print(i, ' ', ' '.join(grid[i][:10]))
    if (x,y) == (7,4):
        print(steps)
        return True
    if grid[x][y] == '#':
        return False
    if grid[x][y] == 'o':
        return False
    grid[x][y] = 'o'
    # explore neighbors clockwise starting by the one on the right
    if ((x < len(grid) - 1 and search(x + 1, y))
        or (y > 0 and search(x, y - 1))
        or (x > 0 and search(x - 1, y))
        or (y < len(grid) - 1 and search(x, y + 1))):
        steps += 1
        print(steps)
        return True

    return False

print(search(1,1))