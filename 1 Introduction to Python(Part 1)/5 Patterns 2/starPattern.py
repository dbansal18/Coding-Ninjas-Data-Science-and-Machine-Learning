# https://classroom.codingninjas.com/app/classroom/me/14075/content/257270/offering/3506010/problem/969

# Code : Star Pattern
# Print the following pattern

# Pattern for N = 4

# ...*
# ..***
# .*****
# *******

# The dots represent spaces.

n = int(input())

i = 1
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
