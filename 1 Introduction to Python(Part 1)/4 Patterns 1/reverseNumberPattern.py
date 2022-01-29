# https://classroom.codingninjas.com/app/classroom/me/14075/content/257269/offering/3505998/problem/3068

# Code : Reverse Number Pattern
# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# 1
# 21
# 321
# 4321

n = int(input())

i = 1

while i <= n:
    j = i
    while j > 0:
        print(j, end="")
        j -= 1
    print()
    i += 1
