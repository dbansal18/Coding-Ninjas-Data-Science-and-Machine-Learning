# https://classroom.codingninjas.com/app/classroom/me/14075/content/257271/offering/3506033/problem/662

# Binary Pattern
# Print the following pattern for the given number of rows.
# Pattern for N = 4
# 1111
# 000
# 11
# 0

n = int(input())

for i in range(1, n + 1):
    for j in range(0, n - i + 1):
        if i % 2 == 0:
            print("0", end="")
        else:
            print("1", end="")
    print()
