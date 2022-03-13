# https://classroom.codingninjas.com/app/classroom/me/14074/content/257231/offering/3505409/problem/1124

# Check Number in Array

# Given an array of length N and an integer x, you need to find if x is present in the array or not. Return true or false.
# Do this recursively.


def checkNumber(arr: list, x: int) -> bool:
    if len(arr) == 0:
        return False
    if arr[0] == x:
        return True
    return checkNumber(arr[1:], x)


# Main
from sys import setrecursionlimit

setrecursionlimit(11000)
n = int(input())
arr = list(int(i) for i in input().strip().split(" "))
x = int(input())
if checkNumber(arr, x):
    print("true")
else:
    print("false")
