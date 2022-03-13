# https://classroom.codingninjas.com/app/classroom/me/14074/content/257233/offering/3505435/problem/33

# Multiplication (Recursive)

# Given two integers M & N, calculate and return their multiplication using recursion.
# You can only use subtraction and addition for your calculation. No other operators are allowed.

import sys

sys.setrecursionlimit(10 ** 6)


def multiply(n: int, m: int) -> int:
    if (m == 0) or (n == 0):
        return 0

    return n + multiply(n, m - 1)


n = int(input())
m = int(input())
print(multiply(n, m))
