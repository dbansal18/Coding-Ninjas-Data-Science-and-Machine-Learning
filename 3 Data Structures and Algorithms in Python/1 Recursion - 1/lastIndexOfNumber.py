# https://classroom.codingninjas.com/app/classroom/me/14074/content/257231/offering/3505415/problem/1134

# Last Index Of Number Question

# Given an array of length N and an integer x, you need to find and return the last index of integer x present in the array.
# Return -1 if it is not present in the array.
# Last index means - if x is present multiple times in the array, return the index at which x comes last in the array.
# You should start traversing your array from 0, not from (N - 1).
# Do this recursively. Indexing in the array starts from 0.


def lastIndexHelper(arr: list, x: int, n: int, i: int) -> int:
    if i == -1:
        return -1

    if arr[i] == x:
        return i

    return lastIndexHelper(arr, x, n, i - 1)


def lastIndex(arr: list, x: int) -> int:
    n = len(arr)

    if n == 0:
        return -1

    return lastIndexHelper(arr, x, n, n - 1)


# Main
from sys import setrecursionlimit

setrecursionlimit(11000)
n = int(input())
arr = list(int(i) for i in input().strip().split(" "))
x = int(input())
print(lastIndex(arr, x))
