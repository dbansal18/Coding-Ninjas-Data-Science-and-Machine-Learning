# https://classroom.codingninjas.com/app/classroom/me/14075/content/257276/offering/3506097/problem/981

# Code Merge Two Sorted Arrays

# You have been given two sorted arrays/lists(ARR1 and ARR2) of size N and M respectively,
# merge them into a third array/list such that the third array is also sorted.

from sys import stdin


def merge(arr1: list, n: int, arr2: list, m: int) -> list:
    i = 0
    j = 0
    ans = []
    while i < n and j < m:
        if arr1[i] > arr2[j]:
            ans.append(arr2[j])
            j += 1
        else:
            ans.append(arr1[i])
            i += 1
    ans = ans + arr1[i:n] + arr2[j:m]
    return ans


# Taking Input Using Fast I/O
def takeInput():
    n = int(stdin.readline().rstrip())
    if n != 0:
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n

    return list(), 0


# to print the array/list
def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")

    print()


# main
t = int(stdin.readline().rstrip())

while t > 0:

    arr1, n = takeInput()
    arr2, m = takeInput()

    ans = merge(arr1, n, arr2, m)
    printList(ans, (n + m))

    t -= 1
