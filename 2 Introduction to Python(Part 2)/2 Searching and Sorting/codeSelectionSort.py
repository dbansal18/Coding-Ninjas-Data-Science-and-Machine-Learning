# https://classroom.codingninjas.com/app/classroom/me/14075/content/257276/offering/3506087/problem/181

# Code Selection Sort

# Provided with a random integer array/list(ARR) of size N, you have been required to sort this array using 'Selection Sort'.

from sys import stdin


def selectionSort(arr: list, n: int) -> None:
    for i in range(n - 1):
        newMin = i
        for j in range(i + 1, n):
            if arr[newMin] > arr[j]:
                newMin = j
        arr[i], arr[newMin] = arr[newMin], arr[i]


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
    selectionSort(arr, n)
    printList(arr, n)

    t -= 1
