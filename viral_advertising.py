import os

def viralAdvertising(n):
    """ int -> int
    calculates number of total likes given a certain amount of days that have passed
    :param n: number of days
    :return: number of total likes
    """
    total_like_counter = 0
    shared_counter = 5

    for i in range(n):
        like_day = shared_counter//2
        total_like_counter = total_like_counter+like_day
        shared_counter = like_day*3
    return total_like_counter
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

