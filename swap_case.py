def swap_case(s):
    """ converts lower to upper and upper to lower
    string -> string
    :param s: string to convert
    :return: converted string
    """
    list=[]
    for char in s:
        if char.isupper():
            list.append(char.lower())
        else:
            list.append(char.upper())
    fin_str = ''.join(list)
    return fin_str

