from helpers import read_input, read_chars


def operation(opcode, inp1, inp2):
    if opcode == 1:
        return inp1 + inp2
    elif opcode == 2:
        return inp1 * inp2
    elif opcode == 99:
        raise Exception(f"Halt")
    else:
        raise Exception(f"Invalid opcode: {opcode}")

intcode = [1,0,0,0,99]

def process_intcode(intcode):
    result = intcode
    for index in range(0, len(intcode), 4):
        opcode = intcode[index]
        inp1, inp2 = intcode[intcode[index + 1]], intcode[intcode[index + 2]]

        try:
            result = operation(opcode, inp1, inp2)
        except:
            return intcode
        target = intcode[index + 3]
        intcode[target] = result

    return intcode

                            
def main1():                
    chars = []              
    for line in read_input('02/input.txt'):
        chars.extend([int(i) for i in read_chars(line)])

    chars[1] = 12
    chars[2] = 2
    intcode = process_intcode(chars)
            

if __name__ == "__main__":
    print(main1())
