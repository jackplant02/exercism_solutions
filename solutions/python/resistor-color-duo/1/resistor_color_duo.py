def value(colors):
    color_map = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9,
    }

    first_colour, second_colour, *_ = colors

    num1 = color_map[first_colour]
    num2 = color_map[second_colour]

    return int(str(num1) + str(num2))
