"""Functions that investigate triangle properties."""


def equilateral(sides):
    """Determines if a triangle is equilateral.

    Args:
        sides: A list of triangle side lengths.

    Returns: (bool) whether or not the triangle is equilateral.
    """

    if not is_valid_triangle(sides):
        return False

    a, b, c = sides
    return a == b and b == c and a == c


def isosceles(sides):
    """Determines if a triangle is isosceles.

    Args:
        sides: A list of triangle side lengths.

    Returns: (bool) whether or not the triangle is isosceles.
    """

    if not is_valid_triangle(sides):
        return False

    a, b, c = sides
    return a == b or b == c or a == c


def scalene(sides):
    """Determines if a triangle is scalene.

    Args:
        sides: A list of triangle side lengths.

    Returns: (bool) whether or not the triangle is scalene.
    """

    if not is_valid_triangle(sides):
        return False

    a, b, c = sides
    return a != b and b != c and a != c


def is_valid_triangle(sides):
    """Checks if a triangle is valid.

    Args:
        sides: A list of triangle side lengths.

    Returns: (bool) whether or not the triangle is valid.
    """

    if any(side <= 0 for side in sides):
        return False

    a, b, c = sides
    if a + b < c:
        return False
    if b + c < a:
        return False
    return not c + a < b
