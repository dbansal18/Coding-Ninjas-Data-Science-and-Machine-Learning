# https://classroom.codingninjas.com/app/classroom/me/14075/content/257276/offering/3506094/problem/26

# Code Insertion Sort

# Provided with a random integer array/list(ARR) of size N, you have been required to sort this array using 'Insertion Sort'.

from sys import stdin


def insertionSort(arr: list, n: int) -> None:
    for i in range(1, n):
        k = i
        for j in range(i - 1, -1, -1):
            if arr[k] >= arr[j]:
                break
            if arr[j] > arr[k]:
                arr[j], arr[k] = arr[k], arr[j]
                k = j


# Taking Input Using Fast I/O
def takeInput():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


# to print the array/list
def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")

    print()


# main
t = int(stdin.readline().strip())

while t > 0:

    arr, n = takeInput()
    insertionSort(arr, n)
    printList(arr, n)

    t -= 1
