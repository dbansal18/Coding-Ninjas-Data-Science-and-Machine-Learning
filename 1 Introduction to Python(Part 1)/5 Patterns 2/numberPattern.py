# https://classroom.codingninjas.com/app/classroom/me/14075/content/257270/offering/3506014/problem/484

# Number Pattern

# Print the following pattern for n number of rows.
# For eg. N = 5

# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321

n = int(input())

i = 1

while i <= n:
    j = 1
    while j <= i:
        print(j, end="")
        j += 1
    j = 1
    while j <= 2 * (n - i):
        print(" ", end="")
        j += 1
    j = i
    while j > 0:
        print(j, end="")
        j -= 1
    print()
    i += 1
