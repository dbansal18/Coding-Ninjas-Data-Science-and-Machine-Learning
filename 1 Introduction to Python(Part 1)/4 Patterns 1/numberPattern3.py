# https://classroom.codingninjas.com/app/classroom/me/14075/content/257269/offering/3506003/problem/471

# Number Pattern 3
# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# 1
# 11
# 121
# 1221

n = int(input())

i = 0
while i < n:
    j = 0
    while j <= i:
        if j == 0 or j == i:
            print(1, end="")
        else:
            print(2, end="")
        j += 1
    print()
    i += 1
