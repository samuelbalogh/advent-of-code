bots = {}
outputs = {}
import random

class Bot(object):
    def __init__(self):
        self.number = 0
        self.chips = []

def initial_state(instructions):
    with open(instructions) as data:
        while True:
            try:
                line = next(data)
                if line.startswith('value'):
                    value = line.split(' ')[1].strip()
                    bot = line.split(' ')[5].strip()
                    try:
                        bots[bot].append(value)
                    except KeyError:
                        bots[bot] = [value]
            except StopIteration:
                break

def get_orders(instructions):
    with open(instructions) as data:
        orders = [line.strip() for line in data.readlines() if line.startswith('bot')]
    return orders

def next_bot_with_two_chips():
    return ''.join([bot for bot in bots if len(bots[bot]) == 2][0])

def get_bots_with_two_chips():
    return [bot for bot in bots if len(bots[bot]) > 2]


def process_intstruction(line):
    line = line.split()
    target_type_one = line[5]
    target_type_two = line[10]
    print(target_type_one)
    print(target_type_two)
    bot = line[1]
    lower = min(bots[bot])
    higher = max(bots[bot])
    target_one = line[6]
    target_two = line[11]
    if target_type_one == 'output':
        try:
            outputs[target_one].append(lower)
        except KeyError:
            outputs[target_one] = [lower]
    else:
        try:
            bots[target_one].append(lower)
        except KeyError:
            bots[target_one] = [lower]
    if target_type_two == 'output':
        try:
            outputs[target_two].append(higher)
        except KeyError:
            outputs[target_two] = [higher]
    else:
        try:
            bots[target_two].append(higher)
        except KeyError:
            bots[target_two] = [higher]
    bots[bot] = []

def process_instructions(instructions):
    initial_state(instructions)
    orders = get_orders(instructions)
    next_bot = next_bot_with_two_chips()
    while any(bots.values()):
        try:
            if '17' in bots[next_bot] and '61' in bots[next_bot]:
                print(next_bot)
                return next_bot
        except KeyError:
            pass
        for order in orders:
            if order.split()[1] == next_bot:
                process_intstruction(order)
                next_bot =  next_bot_with_two_chips()
                break

process_instructions('input')
print(bots)
print(outputs)
'''
initial_state('input')
print(bots)
print(next_bot_with_two_chips())
'''