import hashlib
from itertools import count

""" Part one """
"""
door_ID = 'uqwqemis'
password = ''
count_from = 0
for i in range(8):
    for integer in count(count_from):
        to_be_hashed = door_ID + str(integer)
        digest = hashlib.md5(str(to_be_hashed)).hexdigest()
        if digest[:5] == '00000':
            password += digest[5]
            print(digest[5])
            count_from = integer + 1
            break
    print(password)
print(password)
"""

""" Part two """
door_ID = "uqwqemis"
password = [0] * 8
count_from = 0
digits_decyphered = 0
positions_decyphered = []
while digits_decyphered < len(password):
    for integer in count(count_from):
        to_be_hashed = door_ID + str(integer)
        digest = hashlib.md5(str(to_be_hashed)).hexdigest()
        if digest[:5] == "00000":
            try:
                position = int(digest[5])
                if position < len(password) and position not in positions_decyphered:
                    password[position] = digest[6]
                    positions_decyphered.append(position)
                    digits_decyphered += 1
            except (TypeError, ValueError):
                continue
            count_from = integer + 1
            break
    print(password)
print("".join(password))
