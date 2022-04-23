# https://classroom.codingninjas.com/app/classroom/me/14074/content/257240/offering/3505547/problem/25

# Duplicate in array

# You have been given an integer array/list(ARR) of size N which contains numbers from 0 to (N - 2).
# Each number is present at least once. That is, if N = 5, the array/list constitutes values ranging from 0 to 3,
# and among these, there is a single integer value that is present twice. You need to find and
# return that duplicate number present in the array.

from sys import stdin


def findDuplicate(arr: list, n: int) -> int:
    # Sum of n-2 natural numbers
    sum = ((n - 1) * (n - 2)) / 2

    sum_arr = 0
    for ele in arr:
        sum_arr += ele

    return int(sum_arr - sum)


# Taking input using fast I/O method
def takeInput():
    n = int(stdin.readline().rstrip())

    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


# main
t = int(stdin.readline().rstrip())

while t > 0:

    arr, n = takeInput()
    print(findDuplicate(arr, n))

    t -= 1
