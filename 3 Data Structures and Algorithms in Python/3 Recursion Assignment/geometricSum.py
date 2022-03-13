# https://classroom.codingninjas.com/app/classroom/me/14074/content/257233/offering/3505435/problem/35

# Geometric Sum

# Given k, find the geometric sum i.e.
# 1 + 1/2 + 1/4 + 1/8 + ... + 1/(2^k)
# using recursion.


def geometricSum(k: int) -> float:
    n = 1 - (1 / 2) ** (k + 1)
    d = 0.5

    return n / d


k = int(input())
print("{0:.5f}".format(geometricSum(k)))
