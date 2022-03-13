# https://classroom.codingninjas.com/app/classroom/me/14074/content/257233/offering/3505435/problem/34

# Count Zeros

# Given an integer N, count and return the number of zeros that are present in the given integer using recursion.


def countZeros(n: int) -> int:
    if n == 0:
        return 1

    smallAns = 0
    if (n % 10) == 0:
        smallAns = 1

    if (n // 10) > 0:
        return smallAns + countZeros(n // 10)
    else:
        return smallAns


n = int(input())
print(countZeros(n))
