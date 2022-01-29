# https://classroom.codingninjas.com/app/classroom/me/14075/content/257269/offering/3506003/problem/472

# Number Pattern
# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# 1234
# 123
# 12
# 1

n = int(input())

i = n
while i > 0:
    j = 1
    while j <= i:
        print(j, end="")
        j += 1
    print()
    i -= 1
