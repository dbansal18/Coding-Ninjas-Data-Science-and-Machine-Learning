# from tokenize import Number


# https://classroom.codingninjas.com/app/classroom/me/14074/content/257231/offering/3505400/problem/467

# Power Of A Number

# Write a program to find x to the power n (i.e. x^n). Take x and n from the user. You need to print the answer.
# Note : For this question, you can assume that 0 raised to the power of 0 is 1


def pow(n: int, x: int) -> int:
    if x == 0:
        return 1

    return n * pow(n, x - 1)


a, b = input().split()
a = int(a)
b = int(b)

print(pow(a, b))
