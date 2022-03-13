# https://classroom.codingninjas.com/app/classroom/me/14074/content/257233/offering/3505435/problem/41

# Sum of digits (recursive)

# Write a recursive function that returns the sum of the digits of a given integer.


def sumDigits(n: int) -> int:
    if n <= 0:
        return 0

    return n % 10 + sumDigits(n // 10)


n = int(input())
print(sumDigits(n))
