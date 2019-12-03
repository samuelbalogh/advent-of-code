from string import ascii_lowercase

""" First part """


def find_consensus_string(path):
    with open(path, "r") as data:
        profile = {i: {j: 0 for j in ascii_lowercase} for i in range(8)}
        while True:
            try:
                line = next(data)
                for index in range(len(line.strip())):
                    profile[index][line[index]] += 1
            except StopIteration:
                break
    result = "".join(
        [
            sorted(profile[index], key=profile[index].get, reverse=True)[0]
            for index in profile
        ]
    )
    print(result)
    return result


find_consensus_string("input")


""" Second part """


def find_consensus_string(path):
    with open(path, "r") as data:
        profile = {i: {j: 0 for j in ascii_lowercase} for i in range(8)}
        while True:
            try:
                line = next(data)
                for index in range(len(line.strip())):
                    profile[index][line[index]] += 1
            except StopIteration:
                break
    result = "".join(
        [sorted(profile[index], key=profile[index].get)[0] for index in profile]
    )
    print(result)
    return result


find_consensus_string("input")
