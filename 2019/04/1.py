from itertools import combinations_with_replacement

lower_bound = 136818
upper_bound = 685979

def numbers_between(lower, upper):
    for num in range(lower, upper):
        yield num


def generate_numbers_with_increasing_digits():
    digits = list(range(0, 10))
    combos = list(combinations_with_replacement(digits, r=6))
    combos = [int(''.join(str(d) for d in c)) for c in combos]


generate_numbers_with_increasing_digits()
