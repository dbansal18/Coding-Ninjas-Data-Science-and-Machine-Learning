# https://classroom.codingninjas.com/app/classroom/me/14075/content/257269/offering/3506003/problem/469

# Number Pattern 1
# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# 1
# 11
# 111
# 1111

n = int(input())

i = 1

while i <= n:
    j = 1
    while j <= i:
        print(1, end="")
        j += 1
    print()
    i += 1
