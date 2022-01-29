# https://classroom.codingninjas.com/app/classroom/me/14075/content/257270/offering/3506011/problem/671

# Code : Triangle of Numbers

# Print the following pattern for the given number of rows.

# Pattern for N = 4
# ...1
# ..232
# .34543
# 4567654


# The dots represent spaces.

n = int(input())

i = 1

while i <= n:
    j = n - i
    while j > 0:
        print(" ", end="")
        j -= 1
    j = 0
    while j < i:
        print(j + i, end="")
        j += 1
    j = i - 1
    while j > 0:
        print(j + i - 1, end="")
        j -= 1
    print()
    i += 1
