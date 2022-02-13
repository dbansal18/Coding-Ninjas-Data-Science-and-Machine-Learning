# https://classroom.codingninjas.com/app/classroom/me/14075/content/257276/offering/3506100/problem/29

# Sort 0 1 2

# You are given an integer array/list(ARR) of size N. It contains only 0s, 1s and 2s.
# Write a solution to sort this array/list in a 'single scan'.
# 'Single Scan' refers to iterating over the array/list just once or to put it in other words,
# you will be visiting each element in the array/list just once.

from sys import stdin


def sort012(arr: list, n: int) -> None:
    i = 0
    next0 = 0
    next2 = n - 1
    while i <= next2:
        if arr[i] == 0:
            arr[i], arr[next0] = arr[next0], arr[i]
            next0 += 1
            i += 1
        elif arr[i] == 2:
            arr[i], arr[next2] = arr[next2], arr[i]
            next2 -= 1
        else:
            i += 1


# Taking Input Using Fast I/O
def takeInput():
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


# to print the array/list
def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")

    print()


# main
t = int(stdin.readline().rstrip())

while t > 0:

    arr, n = takeInput()

    sort012(arr, n)
    printList(arr, n)

    t -= 1
