# https://classroom.codingninjas.com/app/classroom/me/14075/content/257270/offering/3506014/problem/492

# Pyramid Number Pattern

# Print the following pattern for the given number of rows.
# Pattern for N = 4
#    1
#   212
#  32123
# 4321234

n = int(input())

i = 1
while i <= n:
    j = n - i
    while j > 0:
        print(" ", end="")
        j -= 1
    j = i
    while j > 0:
        print(j, end="")
        j -= 1
    j = 2
    while j <= i:
        print(j, end="")
        j += 1
    print()
    i += 1
