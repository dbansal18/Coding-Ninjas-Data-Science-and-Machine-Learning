# https://classroom.codingninjas.com/app/classroom/me/14075/content/257271/offering/3506033/problem/679

# Diamond of Stars4

# Print the following pattern for the given number of rows.
# Note: N is always odd.

# Pattern for N = 5
#   *
#  ***
# *****
#  ***
#   *

n = int(input())

for i in range(0, n // 2 + 1):
    for j in range(n // 2 - i, 0, -1):
        print(" ", end="")
    for j in range(0, 2 * i + 1):
        print("*", end="")
    print()

for i in range(n // 2 - 1, -1, -1):
    for j in range(n // 2 - i, 0, -1):
        print(" ", end="")
    for j in range(0, 2 * i + 1):
        print("*", end="")
    print()
