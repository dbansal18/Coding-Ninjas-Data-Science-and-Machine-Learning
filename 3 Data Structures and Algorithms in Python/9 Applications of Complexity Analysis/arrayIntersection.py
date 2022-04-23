# https://classroom.codingninjas.com/app/classroom/me/14074/content/257240/offering/3505542/problem/27

# Array Intersection

# You have been given two integer arrays/list(ARR1 and ARR2) of size N and M, respectively.
# You need to print their intersection; An intersection for this problem can be defined when both the arrays/lists
# contain a particular value or to put it in other words, when there is a common value that exists in both the arrays/lists.

# Note :Input arrays/lists can contain duplicate elements.
# The intersection elements printed would be in the order they appear in the first sorted array/list(ARR1).

from sys import stdin


def intersection(arr1: list, arr2: list, n: int, m: int) -> None:
    arr1.sort()
    arr2.sort()

    i = 0
    j = 0

    while i < n and j < m:
        if arr1[i] == arr2[j]:
            print(arr1[i], end=" ")
            i += 1
            j += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            i += 1


# Taking input using fast I/O method
def takeInput():
    n = int(stdin.readline().strip())

    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


# main
t = int(stdin.readline().strip())

while t > 0:

    arr1, n = takeInput()
    arr2, m = takeInput()
    intersection(arr1, arr2, n, m)
    print()

    t -= 1
