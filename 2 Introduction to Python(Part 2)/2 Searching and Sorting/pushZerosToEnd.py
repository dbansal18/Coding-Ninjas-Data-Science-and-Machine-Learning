# https://classroom.codingninjas.com/app/classroom/me/14075/content/257276/offering/3506100/problem/187

# Push Zeros to end

# You have been given a random integer array/list(ARR) of size N.
# You have been required to push all the zeros that are present in the array/list to the end of it.
# Also, make sure to maintain the relative order of the non-zero elements.

from sys import stdin


def pushZerosAtEnd(arr: list, n: int) -> None:
    count = 0
    for i in range(n):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1
    while count < n:
        arr[count] = 0
        count += 1


# Taking Input Using Fast I/O
def takeInput():
    n = int(stdin.readline().rstrip())

    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split()))
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

    pushZerosAtEnd(arr, n)
    printList(arr, n)

    t -= 1
