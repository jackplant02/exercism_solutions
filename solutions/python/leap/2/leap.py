"Module that comptues if a given year is a leap year"

def leap_year(year):
    """Determines if a given year is a leap year.

    Args:
        year: The year in question

    Returns: (bool) True if the year is a leap year, false if not.
    
    """
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0
