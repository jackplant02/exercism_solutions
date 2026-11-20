def reverse(text):
    reversed_string = ""
    for i in range(len(text)):
        index = -i - 1
        reversed_string += text[index]

    return reversed_string
