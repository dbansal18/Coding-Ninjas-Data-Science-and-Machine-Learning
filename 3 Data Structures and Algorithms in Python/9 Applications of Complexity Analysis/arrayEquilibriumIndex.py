# https://classroom.codingninjas.com/app/classroom/me/14074/content/257240/offering/3505545/problem/31

# Array Equilibrium Index

# For a given array/list(ARR) of size 'N,' find and return the 'Equilibrium Index' of the array/list.
# Equilibrium Index of an array/list is an index 'i' such that the sum of elements at indices [0 to (i - 1)]
# is equal to the sum of elements at indices [(i + 1) to (N-1)]. One thing to note here is, the item at the index 'i'
# is not included in either part.
# If more than one equilibrium indices are present, then the index appearing first in left to right fashion should be returned.
# Negative one(-1) if no such index is present.

from sys import stdin


def arrayEquilibriumIndex_alter(arr: list, n: int) -> int:
    for i in range(1, n):
        arr[i] = arr[i - 1] + arr[i]

    for i in range(n):
        if i == 0:
            sum_left = 0
        else:
            sum_left = arr[i - 1]

        if i == n - 1:
            sum_right = 0
        else:
            sum_right = arr[n - 1] - arr[i]

        if sum_left == sum_right:
            return i

    return -1


def arrayEquilibriumIndex(arr: list, n: int) -> int:
    right_sum, left_sum = 0, 0

    for i in range(n):
        right_sum += arr[i]

    for i in range(n):
        right_sum -= arr[i]

        if right_sum == left_sum:
            return i

        left_sum += arr[i]

    return -1


# Taking input using fast I/O method
def takeInput():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()


# main
t = int(stdin.readline().strip())

while t > 0:

    arr, n = takeInput()
    print(arrayEquilibriumIndex(arr, n))

    t -= 1
