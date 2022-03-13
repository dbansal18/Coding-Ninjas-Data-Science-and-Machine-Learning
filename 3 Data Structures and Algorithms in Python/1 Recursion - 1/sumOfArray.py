# https://classroom.codingninjas.com/app/classroom/me/14074/content/257231/offering/3505408/problem/1123

# Sum Of Array

# Given an array of length N, you need to find and return the sum of all elements of the array.
# Do this recursively.


def sumArrayHelper(arr: list, n: int) -> int:
    if n == 0:
        return 0
    return arr[0] + sumArrayHelper(arr[1:], n - 1)


def sumArray(arr: list) -> int:
    return sumArrayHelper(arr, len(arr))


# Main
from sys import setrecursionlimit

setrecursionlimit(11000)
n = int(input())
arr = list(int(i) for i in input().strip().split(" "))
print(sumArray(arr))
