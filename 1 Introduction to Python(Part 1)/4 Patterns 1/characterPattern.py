# https://classroom.codingninjas.com/app/classroom/me/14075/content/257269/offering/3506000/problem/3069

# Code : Character Pattern
# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# A
# BC
# CDE
# DEFG

n = int(input())

i = 1

while i <= n:
    j = 0
    while j < i:
        print(chr(ord("A") + i + j - 1), end="")
        j += 1
    print()
    i += 1
