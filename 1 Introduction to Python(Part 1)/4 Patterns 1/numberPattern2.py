# https://classroom.codingninjas.com/app/classroom/me/14075/content/257269/offering/3506003/problem/470

# Number Pattern 2
# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# 1
# 11
# 202
# 3003

n = int(input())

i = 0
while i < n:
    j = 0
    while j <= i:
        if i == 0:
            print(1, end="")
        else:
            if j == 0 or j == i:
                print(i, end="")
            else:
                print(0, end="")
        j += 1
    print()
    i += 1
