# https://classroom.codingninjas.com/app/classroom/me/14075/content/257270/offering/3506014/problem/680

# Arrow pattern

# Print the following pattern for the given number of rows.
# Assume N is always odd.
# Note : There is space after every star.
# Pattern for N = 7
# *
#  * *
#    * * *
#      * * * *
#    * * *
#  * *
# *


def printLine(i):
    if i == 1:
        print("*")
    else:
        j = 2 * (i - 1) - 1
        while j > 0:
            print(" ", end="")
            j -= 1
        j = 1
        while j < 2 * i:
            if j % 2 == 0:
                print(" ", end="")
            else:
                print("*", end="")
            j += 1
        print()


n = int(input())

i = 1

while i <= n:
    if i > (n // 2 + 1):
        printLine(n - i + 1)
    else:
        printLine(i)
    i += 1
