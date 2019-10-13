def mutate_string(string, position, character):
    """ mutates string
    (str,int,char) -> str
    :param string: string to analyze
    :param position: position of mutation
    :param character: char that modifies
    :return: mutated string
    """
    lis = list(string)
    lis[position] = character
    final_string = ''.join(lis)
    return final_string
