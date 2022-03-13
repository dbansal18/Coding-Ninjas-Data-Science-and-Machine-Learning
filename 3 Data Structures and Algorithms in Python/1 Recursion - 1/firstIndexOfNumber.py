# https://classroom.codingninjas.com/app/classroom/me/14074/content/257231/offering/3505412/problem/1130

# First Index of Number - Question

# Given an array of length N and an integer x, you need to find and return the first index of integer x present in the array.
# Return -1 if it is not present in the array.
# First index means, the index of first occurrence of x in the input array.
# Do this recursively. Indexing in the array starts from 0.


def firstIndexHelper(arr: list, x: int, n: int, i: int):
    if i > n:
        return -1

    if arr[i] == x:
        return i

    return firstIndexHelper(arr, x, n, i + 1)


def firstIndex(arr: list, x: int) -> int:
    n = len(arr)
    if n == 0:
        return -1

    return firstIndexHelper(arr, x, n - 1, 0)


# Main
from sys import setrecursionlimit

setrecursionlimit(11000)
n = int(input())
arr = list(int(i) for i in input().strip().split(" "))
x = int(input())
print(firstIndex(arr, x))
