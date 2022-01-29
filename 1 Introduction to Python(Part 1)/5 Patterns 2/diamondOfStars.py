# https://classroom.codingninjas.com/app/classroom/me/14075/content/257270/offering/3506012/problem/679

# Code : Diamond of stars

# Print the following pattern for the given number of rows.
# Note: N is always odd.

# Pattern for N = 5
# ..*
# .***
# *****
# .***
# ..*

# The dots represent spaces.

input = int(input())

i = 1
n = input // 2 + 1
while i <= n:
    j = n - i
    while j > 0:
        print(" ", end="")
        j -= 1
    j = 1 + 2 * (i - 1)
    while j > 0:
        print("*", end="")
        j -= 1
    print()
    i += 1

n = input - n + 1
i = n - 1
while i > 0:
    j = n - i
    while j > 0:
        print(" ", end="")
        j -= 1
    j = 1 + 2 * (i - 1)
    while j > 0:
        print("*", end="")
        j -= 1
    print()
    i -= 1
