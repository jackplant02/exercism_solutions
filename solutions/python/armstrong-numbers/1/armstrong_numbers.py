def is_armstrong_number(number):
    number_string = str(number)
    sum_of_squares = 0
    for digit in number_string:
        sum_of_squares += int(digit) ** len(number_string)

    return number == sum_of_squares
