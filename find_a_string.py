
def count_substring(string, sub_string):
    """  check for occurrencies of substring in string
    (str,str) -> int
    :param string: string that contains substring
    :param sub_string: the substring pattern to check
    :return: number of occurrencies
    """
    counter = 0
    for i in range(len(string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            counter = counter + 1

    return counter
