""" Part one """

def decompress(path):
    with open(path) as data:
        decompressed = ''
        buffer = ''
        marker = ''
        in_buffer_mode = False
        in_marker = False
        for char in data.read():
            if in_buffer_mode:
                steps += 1
                if steps == repeat_chars:
                    buffer += char
                    in_buffer_mode = False
                    in_marker = False
                    buffer = repeat_times * buffer
                    decompressed += buffer
                    continue
                else:
                    buffer += char
            if in_marker and not in_buffer_mode:
                if char == ')':
                    in_marker = False
                    in_buffer_mode = True
                    repeat_chars, repeat_times = [int(i) for i in marker.split('x')]
                    marker = ''
                    buffer = ''
                    steps = 0
                else:
                    marker += char
            if char == '(' and not in_marker:
                in_marker = True
                marker = ''
            if not in_buffer_mode and not in_marker:
                decompressed += char
            else:
                continue
        print(decompressed)
        return decompressed

""" Part two - UNDER CONSTRUCTION """

def find_next_marker(segment):
    marker = ''
    in_marker = False
    for char in segment:
        if in_marker and char != ')':
            marker += char
        if in_marker and char == ')':
            return marker
        if not in_marker and char == '(':
            in_marker = True


def unzip_segment(marker, segment):
    repeat_chars = [int(i) for i in marker.split('x')][0]
    repeat_times = [int(i) for i in marker.split('x')][1]
    if '(' not in segment:
        return segment[:repeat_chars] * repeat_times
    next_marker = find_next_marker(segment)
    next_segment = segment[segment.index(next_marker)+len(marker)+1:]
    return repeat_times * unzip_segment(next_marker, next_segment)

def length_of_unzipped_segment(marker, segment, length=0):
    decompressed_segment = ''
    repeat_chars = [int(i) for i in marker.split('x')][0]
    repeat_times = [int(i) for i in marker.split('x')][1]
    current_segment = segment[:repeat_chars]
    if '(' not in segment:
        #print(') not in segment')
        #print(len(current_segment) * repeat_times)
        return len(current_segment) * repeat_times
    next_marker = find_next_marker(segment)
    next_segment = segment[segment.index(next_marker) + len(marker):].strip(')')
    if repeat_chars < segment.index(next_segment):
        return length_of_unzipped_segment(next_marker, next_segment)
    '''
    print('segment: ', segment)
    print(' ')
    print('next marker: ', next_marker)
    print('next segment: ', next_segment)
    '''
    solution = repeat_times * length_of_unzipped_segment(next_marker, next_segment)
    #print(solution)
    return solution


data1 = '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'

data2 = 'X(8x2)(3x3)ABCY'

data3 = '(27x12)(20x12)(13x14)(7x10)(1x12)A '

data3 = '(3x3)XYZ'

def solve_for_input(data, decompressed=0):
    in_marker = False
    decompressed_segment = ''
    for char in range(len(data)):
        if data[char] == '(' and not in_marker:
            marker = ''
            in_marker = True
        elif data[char] != ')' and in_marker:
            marker += data[char]
        elif data[char] == ')' and in_marker:
            in_marker = False
            repeat_chars = [int(i) for i in marker.split('x')][0]
            decompressed += length_of_unzipped_segment(marker, data[char:char+repeat_chars])
            decompressed_segment += unzip_segment(marker, data[char:char+repeat_chars])
            return decompressed + solve_for_input(data[char+repeat_chars:], decompressed=decompressed)
            marker = ''
        else:
            decompressed += 1
            decompressed_segment += data[char]
    print(decompressed_segment)
    return decompressed

print(solve_for_input(data2))

# length_of_unzipped_segment('25x3', '(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN')

# length_of_unzipped_segment('27x12', '(20x12)(13x14)(7x10)(1x12)A')

# length_of_unzipped_segment('8x2', '(3x3)ABCY')

# length_of_unzipped_segment('3x3', 'XYZ')


def decompress(path):
    with open(path) as data:
        decompressed = ''
        buffer = ''
        marker = ''
        in_buffer_mode = False
        in_marker = False
        repeat_times = 1
        for char in data.read():
            if in_buffer_mode:
                steps += 1
                if steps == repeat_chars:
                    buffer += char
                    in_buffer_mode = False
                    in_marker = False
                    buffer = repeat_times * buffer
                    decompressed += buffer
                    continue
                else:
                    buffer += char
            if in_marker and not in_buffer_mode:
                if char == ')':
                    in_marker = False
                    in_buffer_mode = True
                    repeat_chars = [int(i) for i in marker.split('x')][0]
                    repeat_times = [int(i) for i in marker.split('x')][1]
                    marker = ''
                    buffer = ''
                    steps = 0
                else:
                    marker += char
            if char == '(' and not in_marker:
                in_marker = True
                marker = ''
            if not in_buffer_mode and not in_marker:
                decompressed += char
            else:
                continue
        return decompressed


# print(decompress('sample'))