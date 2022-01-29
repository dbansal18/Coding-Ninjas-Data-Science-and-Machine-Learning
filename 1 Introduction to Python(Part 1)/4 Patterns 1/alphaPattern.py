# https://classroom.codingninjas.com/app/classroom/me/14075/content/257269/offering/3506003/problem/661

# Alpha Pattern
# Print the following pattern for the given N number of rows.
# Pattern for N = 3
#  A
#  BB
#  CCC

n = int(input())

i = 1
while i <= n:
    j = 1
    while j <= i:
        print(chr(ord("A") + i - 1), end="")
        j += 1
    print()
    i += 1
