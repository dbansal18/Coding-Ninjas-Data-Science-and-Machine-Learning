# https://classroom.codingninjas.com/app/classroom/me/14075/content/257269/offering/3505997/problem/3067

# Code : Triangle Number Pattern
# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# 1
# 22
# 333
# 4444

n = int(input())

i = 1

while i <= n:
    j = 1
    while j <= i:
        print(i, end="")
        j += 1
    print()
    i += 1
