def is_leap(year):
    """ calculate if year is leap year
    int -> boolean
    :param year: year to check if leap
    :return: boolean if leap or not
    """
    leap = False
    if year % 4 == 0:
        leap = True
    if year % 100 == 0:
        leap = False
    if year % 400 == 0:
        leap = True
    return leap