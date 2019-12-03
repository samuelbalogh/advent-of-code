def get_checksum():
    with open("input", "r") as input_data:
        checksum = 0
        for line in input_data:
            nums = sorted([int(item) for item in line.split()])
            for index, num in enumerate(nums):
                dividend = [
                    larger_num
                    for larger_num in nums[index + 1 :]
                    if larger_num % num == 0
                ]
                if dividend:
                    checksum += dividend.pop() // num
                    continue
    return checksum


print(get_checksum())
