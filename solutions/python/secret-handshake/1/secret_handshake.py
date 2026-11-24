def commands(binary_str):
    actions = ["jump", "close your eyes", "double blink", "wink"]

    reverse = int(binary_str[0])

    if reverse:
        iter_order = range(1, 5)
    else:
        iter_order = range(-1, -5, -1)

    output = []
    for i in iter_order:
        print(i)
        if reverse:
            subtract = 1
        else:
            subtract = 0

        if int(binary_str[i]):
            output.append(actions[i - subtract])

    return output
