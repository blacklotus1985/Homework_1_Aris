import numpy
def arrays(arr):
    """ gets a white space array and returns it into floats and inverted
    :param arr: array to be inverted
    :return: inverted and changed array
    """
    lst = []
    for elem in arr:
        lst.append(elem)
    arr = numpy.array(lst, float)
    sorted_arr = arr[::-1]
    return sorted_arr


arr = input().strip().split(' ')
result = arrays(arr)
print(result)