def get_checksum():
    with open("input", "r") as input_data:
        checksum = 0
        for line in input_data:
            nums = [int(item) for item in line.split()]
            diff = max(nums) - min(nums)
            checksum += diff
    return checksum


def get_checksum_with_comprehension():
    with open("input", "r") as input_data:
        return sum(
            (
                max([int(item) for item in line.split()])
                - min([int(item) for item in line.split()])
            )
            for line in input_data
        )


print(get_checksum())
