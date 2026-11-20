def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    num_steps = 0

    while number != 1:
        if is_even(number):
            number = number / 2
        else:
            number = number * 3 + 1

        num_steps += 1
    return num_steps


def is_even(number):
    return number % 2 == 0
