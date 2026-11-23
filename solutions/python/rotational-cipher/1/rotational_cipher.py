def cipher_map(key):

    cipher_text = []
    text = "abcdefghijklmnopqrstuvwxyz"

    for i in range(len(text)):
        if i < len(text) - key:
            new_char_index = i + key
        else:
            new_char_index = i + key - len(text)

        new_char = text[new_char_index]
        cipher_text.append(new_char)

    return "".join(cipher_text)


def rotate(text, key):

    rotated_text = []
    cipher_mapping = cipher_map(key)
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for i, char in enumerate(text):
        if not char.isalpha():
            rotated_text.append(char)
        elif char.isupper():
            lower_char = char.lower()
            index = alphabet.index(lower_char)
            rotated_text.append(cipher_mapping[index].upper())

        else:
            index = alphabet.index(char)
            rotated_text.append(cipher_mapping[index])

    return "".join(rotated_text)
