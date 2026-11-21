def is_valid(isbn):
    no_dash = ''.join(char for char in isbn if char.isalnum())

    if len(no_dash) != 10:
        return False
    
    check_sum = 0

    for i in range(10):
        if no_dash[i] == 'X' and i == 9:
            num = 10
        elif no_dash[i].isdigit():
            num = int(no_dash[i])
        else:
            return False
        check_sum += num * (10 - i)

    return check_sum % 11 == 0

