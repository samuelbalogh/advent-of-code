from itertools import count

""" First part """


def is_pal(s):
    """ Returns True if s is palindrome, False otherwise """
    reverse = s[::-1]
    return s == reverse


def contains_palindrom_of_four_chars(s):
    """ Return True if s contains a palindrome of length four, composed of two different characters """
    for i in range(len(s) - 3):
        if is_pal(s[i : i + 4]) and len(set(s[i : i + 4])) != 1:
            return True
    return False


class ContinueWithNextLine(Exception):
    """ Custom exception in order to continue an outer loop """

    pass


def transport_layer_snooping(path):
    """ Main function """
    with open(path, "r") as data:
        contains_tls = 0
        for _ in count():
            try:
                line = next(data)
                slices = line.strip().replace("[", "#").replace("]", "#").split("#")
                between_square_brackets = (
                    slice for slice in slices if slices.index(slice) % 2 == 1
                )
                outside_square_brackets = (
                    slice for slice in slices if slices.index(slice) % 2 == 0
                )
                for slice in between_square_brackets:
                    if contains_palindrom_of_four_chars(slice):
                        raise ContinueWithNextLine
                for slice in outside_square_brackets:
                    if contains_palindrom_of_four_chars(slice):
                        contains_tls += 1
                        raise ContinueWithNextLine
            except ContinueWithNextLine:
                continue
            except StopIteration:
                break
    print(contains_tls)
    return contains_tls


""" Second part """


def contains_palindrom_of_three_chars(s):
    """ Return True if s contains a palindrome of length four, composed of two different characters """
    palindromes = []
    for i in range(len(s) - 2):
        if is_pal(s[i : i + 3]) and len(set(s[i : i + 3])) != 1:
            palindromes.append(s[i : i + 3])
    return palindromes


def super_secret_listening(path):
    """ Main function """
    with open(path, "r") as data:
        contains_ssl = 0
        for _ in count():
            try:
                line = next(data)
                slices = line.strip().replace("[", "#").replace("]", "#").split("#")
                between_square_brackets = (
                    slice for slice in slices if slices.index(slice) % 2 == 1
                )
                outside_square_brackets = (
                    slice for slice in slices if slices.index(slice) % 2 == 0
                )
                inner_palindromes = [
                    elem
                    for sublist in [
                        contains_palindrom_of_three_chars(slice)
                        for slice in between_square_brackets
                    ]
                    for elem in sublist
                ]
                outer_palindromes = [
                    elem
                    for sublist in [
                        contains_palindrom_of_three_chars(slice)
                        for slice in outside_square_brackets
                    ]
                    for elem in sublist
                ]
                if any(
                    [
                        True if set(inner) == set(outer) and inner != outer else False
                        for outer in outer_palindromes
                        for inner in inner_palindromes
                    ]
                ):
                    contains_ssl += 1
            except StopIteration:
                break
    print(contains_ssl)
    return contains_ssl


super_secret_listening("input")
