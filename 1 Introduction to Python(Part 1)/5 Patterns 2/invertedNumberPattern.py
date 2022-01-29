# https://classroom.codingninjas.com/app/classroom/me/14075/content/257270/offering/3506006/problem/3071

# Code : Inverted Number Pattern
# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# 4444
# 333
# 22
# 1


n = int(input())

i = n

while i > 0:
    j = 1
    while j <= i:
        print(i, end="")
        j += 1
    print()
    i -= 1
