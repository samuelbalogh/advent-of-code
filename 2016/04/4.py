from string import ascii_lowercase as abc

def decypher_decoy_rooms(input_file):
    with open(input_file, 'r') as data:
        sum_of_sector_ids = 0
        valid_rooms = []
        while True:
            try:
                line = next(data).split('[')
                text = line[0][:-4].replace('-', ' ')
                code = line[1].strip().strip(']')
                sector_id = ''.join(line[0].split('-')[-1:])
                letter_counts = {letter: text.count(letter) for letter in text if letter in abc}
                sorted_by_abc = sorted(letter_counts)
                code_should_be = ''.join(sorted(sorted_by_abc, key=letter_counts.get, reverse=True))[:5]
                if code == code_should_be:
                    sum_of_sector_ids += int(sector_id)
                    valid_rooms.append((text, sector_id))
            except StopIteration:
                return sum_of_sector_ids, valid_rooms

def decrypt_room_name(room_name, sector_id):
    room_name = room_name.replace('-', ' ')
    alphabet = MyAlphabet(abc)
    decrypted_room_name = ''
    for letter in room_name:
        if letter != ' ':
            shifted_letter = alphabet[alphabet.index(letter) + sector_id]
            decrypted_room_name += shifted_letter
        else:
            decrypted_room_name += ' '
    return decrypted_room_name

class MyAlphabet(str):
    """ A string subclass that avoids IndexErrors.
        E.g. a string of length 10, when asked for its 11th item, will return its first. """
    def __getitem__(self, index):
        if len(self) <= index:
            new_index = index % len(self)
            return str.__getitem__(self, new_index)
        return str.__getitem__(self, index)

def decrypt_room_names(input_file):
    _, valid_rooms = decypher_decoy_rooms(input_file)
    room_names = []
    for item in valid_rooms:
        room_name, sector_id = item[0], int(item[1])
        alphabet = MyAlphabet(abc)
        decrypted_room_name = ''
        for letter in room_name:
            if letter != ' ':
                shifted_letter = alphabet[alphabet.index(letter) + sector_id]
                decrypted_room_name += shifted_letter
            else:
                decrypted_room_name += ' '
        room_names.append((room_name, decrypted_room_name, sector_id))
    return [room_name[1:3] for room_name in room_names]

for i in decrypt_room_names('input'):
    if 'north' in i[0]:
        print(i)

