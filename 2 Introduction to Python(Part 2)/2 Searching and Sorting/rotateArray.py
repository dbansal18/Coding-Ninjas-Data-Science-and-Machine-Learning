# https://classroom.codingninjas.com/app/classroom/me/14075/content/257276/offering/3506100/problem/188

# Rotate array

# You have been given a random integer array/list(ARR) of size N.
# Write a function that rotates the given array/list by D elements(towards the left).


from sys import stdin


def rotateArr(arr: list, start: int, end: int) -> None:
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def rotate(arr: list, n: int, d: int) -> None:
    if d == 0:
        return
    rotateArr(arr, 0, n - 1)
    rotateArr(arr, 0, n - d - 1)
    rotateArr(arr, n - d, n - 1)


# Taking Input Using Fats I/O
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
    d = int(stdin.readline().rstrip())
    rotate(arr, n, d)
    printList(arr, n)

    t -= 1
