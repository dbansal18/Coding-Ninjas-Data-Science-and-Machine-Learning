# https://classroom.codingninjas.com/app/classroom/me/14075/content/257271/offering/3506033/problem/682

# Rectangular numbers

# Print the following pattern for the given number of rows.
# Pattern for N = 4
# 4444444
# 4333334
# 4322234
# 4321234
# 4322234
# 4333334
# 4444444
# Input format : N (Total no. of rows)

# Output format : Pattern in N lines

n = int(input())
for i in range(1, n + 1):
    temp = n
    for j in range(1, i):
        print(temp, end="")
        temp = temp - 1
    for j in range(1, (2 * n) - (2 * i) + 2):
        print(n - i + 1, end="")
    for j in range(1, i):
        temp = temp + 1
        print(temp, end="")
    print()
for i in range(n - 1, 0, -1):
    temp = n
    for j in range(1, i):
        print(temp, end="")
        temp = temp - 1
    for j in range(1, (2 * n) - (2 * i) + 2):
        print(n - i + 1, end="")
    for j in range(1, i):
        temp = temp + 1
        print(temp, end="")
    print()
