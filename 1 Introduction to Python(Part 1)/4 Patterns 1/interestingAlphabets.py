# https://classroom.codingninjas.com/app/classroom/me/14075/content/257269/offering/3506001/problem/663

# Code : Interesting Alphabets
# Print the following pattern for the given number of rows.
# Pattern for N = 5
# E
# DE
# CDE
# BCDE
# ABCDE

n = int(input())

i = 1
while i <= n:
    j = 1
    while j <= i:
        print(chr(ord("A") + n - i + j - 1), end="")
        j += 1
    print()
    i += 1
