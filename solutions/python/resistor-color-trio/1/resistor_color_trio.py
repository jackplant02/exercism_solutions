def label(colors):
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

    first_colour, second_colour, zeros, *_ = colors

    num1 = color_map[first_colour]
    num2 = color_map[second_colour]
    num3 = color_map[zeros]

    output = int(str(num1) + str(num2) + "0" * num3)

    unit = "ohms"
    if output >= 1000000000:
        output //= 1000000000
        unit = "gigaohms"
    if output >= 1000000:
        output //= 1000000
        unit = "megaohms"
    if output >= 1000:
        output //= 1000
        unit = "kiloohms"

    return str(output) + " " + unit
