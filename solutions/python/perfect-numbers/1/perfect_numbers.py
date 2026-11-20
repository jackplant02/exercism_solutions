def classify(number):
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    aliquot_sum = 0

    for factor in find_factors_less_than_self(number):
        aliquot_sum += factor

    if aliquot_sum == number:
        return "perfect"
    if aliquot_sum > number:
        return "abundant"
    return "deficient"


def find_factors_less_than_self(number):
    """Finds all factors of a number less than itself.

    :param number: int a positive integer
    :return: list[int] a list of the number's factors less than itself
    """
    factors = []
    for i in range(1, number):
        if number % i == 0:
            factors.append(i)

    return factors
