def encode(message, key):
    cipher = ""
    for word in range(len(message)):
        character = message[word]
        cipher += chr(ord(character) + key)
    return cipher


def encode_better(message, key):
    cipher = ""

    for i in range(len(message)):
        character = ord(message[i]) - 65
        shift = ord(key[i % len(key)]) - 65
        add = character + shift
        check = add % 58
        convert = check + 65
        revert = chr(convert)
        cipher += revert
    return cipher
