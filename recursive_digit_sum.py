
import os


# Complete the superDigit function below.

def superDigit(n, k):
    """ (str,int) -> int
    calculates superdigit
    :param n: string representation of an integer
    :param k: number of concatenations of n
    :return: superdigit
    """
    digit = n*k
    check = 2
    list_string = list(str(digit))
    list_num = list(map(int, list_string))

    while check>1:
        n = sum(list_num)
        list_string = list(str(n))
        list_num = list(map(int, list_string))
        check = len(list_num)
    return n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
