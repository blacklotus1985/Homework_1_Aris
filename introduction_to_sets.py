def average(array):
    """ calculates average distinct heights
    array -> int
    :param array: array of heights
    :return: average of heights
    """
    denum = len(set(array))
    num = sum(set(array))
    return num / denum

