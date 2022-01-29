# https://classroom.codingninjas.com/app/classroom/me/14075/content/257269/offering/3505996/problem/3066

# Code : Triangular Star Pattern
# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# *
# **
# ***
# ****


n = int(input())

i = 1

while i <= n:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print()
    i += 1
