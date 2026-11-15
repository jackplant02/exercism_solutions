"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time required.

    Args:
        number_of_layers (int): The number of layers desired for the lasagna.

    Returns:
        int: The preparation time needed for the given number of layers.

    This function calculates the preparation time based on the formula that 2 minutes
    are required for each layer (with the constant defined above).
    """
    return PREPARATION_TIME * number_of_layers


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculates the number of minutes passed in the kitchen so far.

    Args:
        number_of_layers (int): The number of layers added to the lasagna.
        elapsed_bake_time (int): The number of minutes the lasagna has spent baking in
            the oven already.

    Returns:
        int: The toal minutes you have been in the kitchen cooking

    This function returns the preparation time that must have elapsed based on the
    number of layers in the lasagna (see preparation_time_in_minutes()), and the
    elapsed bake time.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
