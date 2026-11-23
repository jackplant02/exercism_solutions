def resistor_label(colors):
    if len(colors) == 1:
        return "0 ohms"
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

    tolerance_map = {
        "grey": "0.05%",
        "violet": "0.1%",
        "blue": "0.25%",
        "green": "0.5%",
        "brown": "1%",
        "red": "2%",
        "gold": "5%",
        "silver": "10%",
    }

    four = len(colors) == 4
    five = len(colors) == 5

    if four:
        first_colour, second_colour, zeros, tol, *_ = colors
    if five:
        first_colour, second_colour, third_colour, zeros, tol, *_ = colors
        num3 = color_map[third_colour]

    num1 = color_map[first_colour]
    num2 = color_map[second_colour]
    num_zeros = color_map[zeros]
    tol_string = tolerance_map[tol]

    if four:
        output = int(str(num1) + str(num2) + "0" * num_zeros)
    if five:
        output = int(str(num1) + str(num2) + str(num3) + "0" * num_zeros)

    unit = "ohms"
    if output >= 1000000000:
        output /= 1000000000
        unit = "gigaohms"
    if output >= 1000000:
        output /= 1000000
        unit = "megaohms"
    if output >= 1000:
        output /= 1000
        unit = "kiloohms"

    return str(output) + " " + unit + " ±" + tol_string
