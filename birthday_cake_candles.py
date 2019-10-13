
import os
from collections import Counter

def birthdayCakeCandles(ar):
    """ calculates how many blown candles
    array -> int
    :param ar: array representing candles
    :return: number of candles blown
    """
    qt = Counter(ar)
    key = list(qt.keys())
    return qt[max(key)]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = map(int, input().rstrip().split())

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
