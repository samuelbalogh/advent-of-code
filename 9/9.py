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

""" Part two - CANNOT TAKE CREDIT FOR THIS ONE, HAD TO LOOK UP SOLUTION ON REDDIT:
https://www.reddit.com/r/adventofcode/comments/5hbygy/2016_day_9_solutions/daz279z/ """

from itertools import count

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
    return False


def recurse_decompress_segment(segment):
    if not find_next_marker(segment):
        return len(segment)
    length = 0
    for _ in count():
        if find_next_marker(segment):
            marker = find_next_marker(segment)
            length += segment.index(marker) - 1
            segment = segment[segment.index(marker)-1:]
            repeat_chars = segment[1:segment.index(marker)+len(marker)].split('x')[0]
            repeat_times = segment[1:segment.index(marker)+len(marker)].split('x')[1]
            segment = segment[segment.index(marker) +len(marker) + 1:]
            length += recurse_decompress_segment(segment[:int(repeat_chars)]) * int(repeat_times)
            segment = segment[int(repeat_chars):]
        else:
            break
    length += len(segment)
    return length

with open('input') as data:
    segment = data.read()
    print(recurse_decompress_segment(segment))