def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    steps = 0

    while number != 1:
        if is_even(number):
            number = number / 2
        else:
            number = number * 3 + 1

        steps += 1
    return steps


def is_even(number):
    return number % 2 == 0
