# https://classroom.codingninjas.com/app/classroom/me/14074/content/257240/offering/3505547/problem/174

# Find the Unique Element

# You have been given an integer array/list(ARR) of size N. Where N is equal to [2M + 1].
# Now, in the given array/list, 'M' numbers are present twice and one number is present only once.
# You need to find and return that number which is unique in the array/list.

from sys import stdin


def findUnique(arr: list, n: int) -> int:
    ans = arr[0]

    for ele in arr[1:]:
        ans = ans ^ ele

    return ans


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
    print(findUnique(arr, n))

    t -= 1
