"""
Helpers for reading puzzle inputs, running tests, etc.
"""


def read_input(filename='input'):
    with open(filename, 'r') as source:
        for line in source:
            yield line.strip()


def read_chars(line, separator=','):
    for c in line.split(separator):
        yield c

