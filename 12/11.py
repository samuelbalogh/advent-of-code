""" Part one """

def copy_command(line):
    register = line.split()[2].strip()
    value = line.split()[1].strip()
    try:
        int(value)
        registers[register] = int(value)
    except ValueError:
        registers[register] = registers[value]

def increase(line):
    register = line.split()[1].strip()
    registers[register] += 1

def decrease(line):
    register = line.split()[1].strip()
    registers[register] -= 1

def jump_command(line, idx):
    step = line.split()[2].strip()
    idx = idx + int(step)
    return idx

def parse_file(data):
    commands = []
    with open(data) as instructions:
        while True:
            try:
                line = next(instructions)
                commands.append(line.strip())
            except StopIteration:
                break
    return commands

def parse_commands(data):
    commands = parse_file(data)
    idx = 0
    while True:
        try:
            line = commands[idx]
            command = line.split()[0]
            if command == 'cpy':
                copy_command(line)
            elif command == 'jnz':
                condition = line.split()[1]
                try:
                    if registers[condition] != 0:
                        idx = jump_command(line, idx)
                        continue
                    else:
                        idx += 1
                        continue
                except KeyError:
                    if condition != '0':
                        idx = jump_command(line, idx)
                        continue
                    else:
                        idx += 1
                        continue
            elif command == 'inc':
                increase(line)
            elif command == 'dec':
                decrease(line)
            idx += 1
        except IndexError as e:
            break
    for register in registers:
        print(register, registers[register])

registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
parse_commands('input')


""" Part two """

registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
parse_commands('input')
