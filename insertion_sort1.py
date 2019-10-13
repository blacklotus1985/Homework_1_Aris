
# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    """ (int,list) -> none

    :param n: lenght of list
    :param arr: array list to reorganize
    :return: none
    """
    last = arr[-1]
    for i in range(1,n):
        if last < arr[-i-1]:
            arr[-i] = arr[-i-1]
            print(*arr)
        if last >= arr[-i-1]:
            arr[-i] = last
            print(*arr)
            break


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
