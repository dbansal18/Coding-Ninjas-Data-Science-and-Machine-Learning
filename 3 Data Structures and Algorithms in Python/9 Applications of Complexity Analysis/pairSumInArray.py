# https://classroom.codingninjas.com/app/classroom/me/14074/content/257240/offering/3505547/problem/20

# Pair sum in array

# You have been given an integer array/list(ARR) and a number 'num'.
# Find and return the total number of pairs in the array/list which sum to 'num'.
# Note:
# Given array/list can contain duplicate elements.

from sys import stdin


def pairSum(arr: list, n: int, num: int) -> int:
    freq = dict()

    for i in arr:
        j = freq.get(i, 0)
        freq[i] = j + 1

    ans = 0
    for i in arr:
        ans += freq.get(num - i, 0)

        if num - i == i:
            ans -= 1

    return int(ans / 2)


# taking input using fast I/O method
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
    num = int(stdin.readline().strip())
    print(pairSum(arr, n, num))

    t -= 1
