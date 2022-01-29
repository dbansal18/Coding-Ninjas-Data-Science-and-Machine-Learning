# https://classroom.codingninjas.com/app/classroom/me/14075/content/257269/offering/3505993/problem/3065

# Code : Square Pattern
# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# 4444
# 4444
# 4444
# 4444


n = int(input())

i = 0

while i < n:
    j = 0
    while j < n:
        print(n, end="")
        j += 1
    print()
    i += 1
