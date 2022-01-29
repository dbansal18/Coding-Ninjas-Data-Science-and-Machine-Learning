# https://classroom.codingninjas.com/app/classroom/me/14075/content/257271/offering/3506033/problem/644

# Print Number Pyramid
# Print the following pattern for a given n.
# For eg. N = 6
# 123456
#  23456
#   3456
#    456
#     56
#      6
#     56
#    456
#   3456
#  23456
# 123456

n = int(input())

for i in range(n, 0, -1):
    for j in range(1, n + 1):
        if j <= (n - i):
            print(" ", end="")
        else:
            print(j, end="")
    print()
for i in range(2, n + 1):
    for j in range(1, n + 1):
        if j <= (n - i):
            print(" ", end="")
        else:
            print(j, end="")
    print()
