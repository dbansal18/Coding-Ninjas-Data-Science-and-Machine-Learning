# https://classroom.codingninjas.com/app/classroom/me/14074/content/257240/offering/3505539/problem/1121

# Power Of A Number

# Write a program to find x to the power n (i.e. x^n). Take x and n from the user. You need to return the answer.
# Do this recursively.


def power(x: int, n: int) -> int:
    if n == 0:
        return 1

    small_ans = power(x, n // 2)

    if n % 2 == 1:
        return x * small_ans * small_ans

    return small_ans * small_ans


# Main
from sys import setrecursionlimit

setrecursionlimit(11000)
x, n = list(int(i) for i in input().strip().split(" "))
print(power(x, n))
