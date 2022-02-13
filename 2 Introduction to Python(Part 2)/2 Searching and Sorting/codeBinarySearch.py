# from re import search


# https://classroom.codingninjas.com/app/classroom/me/14075/content/257276/offering/3506083/problem/45

# Code Binary search

# You have been given a sorted(in ascending order) integer array/list(ARR) of size N and an element X.
# Write a function to search this element in the given input array/list using 'Binary Search'.
# Return the index of the element in the input array/list. In case the element is not present in the array/list, then return -1.

from sys import stdin


def binarySearch(arr: list, n: int, x: int) -> int:
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            start = mid + 1
        else:
            end = mid - 1

    return -1


# Taking Input Using Fast I/O
def takeInput():
    n = int(stdin.readline().strip())

    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


# main
arr, n = takeInput()
t = int(stdin.readline().strip())

while t > 0:

    x = int(input().strip())
    print(binarySearch(arr, n, x))

    t -= 1
