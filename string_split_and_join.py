def split_and_join(line):
    """
    split sentence and then join
    :param line: sentence to split
    :return: sentence
    """
    words = line.split(" ")
    sent = '-'.join(words)
    return sent

