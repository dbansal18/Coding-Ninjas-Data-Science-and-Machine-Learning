# https://classroom.codingninjas.com/app/classroom/me/14075/content/257270/offering/3506008/problem/3070

# Code : Mirror Number Pattern
# Print the following pattern for the given N number of rows.
# Pattern for N = 4

# . . .1
# . . 1 2
# . 1 2 3
# 1 2 3 4

# The dots represent spaces.


n = int(input())

i = 1

while i <= n:
    j = 1
    while j <= n - i:
        print(" ", end="")
        j += 1
    j = 1
    while j <= i:
        print(j, end="")
        j += 1
    print()
    i += 1
