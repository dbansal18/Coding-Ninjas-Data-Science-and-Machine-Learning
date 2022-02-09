# https://classroom.codingninjas.com/app/classroom/me/14075/content/257275/offering/3506079/problem/1290

# Pair sum

# You have been given an integer array/list(ARR) and a number X.
# Find and return the total number of pairs in the array/list which sum to X.

from sys import stdin


def pairSum(arr: list, n: int, x: int) -> int:
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == x:
                ans += 1
    return ans


# Taking Input Using Fast I/O
def takeInput():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


# main
t = int(stdin.readline().strip())

while t > 0:

    arr, n = takeInput()
    x = int(stdin.readline().strip())
    print(pairSum(arr, n, x))

    t -= 1
