# https://classroom.codingninjas.com/app/classroom/me/14075/content/257276/offering/3506090/problem/24

# Code Bubble Sort

# Provided with a random integer array/list(ARR) of size N, you have been required to sort this array using 'Bubble Sort'.


from sys import stdin


def bubbleSort(arr: list, n: int) -> None:
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[i]:
                arr[j], arr[i] = arr[i], arr[j]


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
    bubbleSort(arr, n)
    printList(arr, n)

    t -= 1
