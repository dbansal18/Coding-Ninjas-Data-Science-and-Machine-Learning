# https://classroom.codingninjas.com/app/classroom/me/14075/content/257272/offering/3506050/problem/977

# Fibonacci Member

# Given a number N, figure out if it is a member of fibonacci series or not. Return true if the number is member of fibonacci series else false.
# Fibonacci Series is defined by the recurrence
#     F(n) = F(n-1) + F(n-2)
# where F(0) = 0 and F(1) = 1


def checkMember(n):
    i = 0
    j = 1
    while i <= n:
        if i == n:
            return True
        j = i + j
        i = j - i
    return False


# Alternate approch to try:
# Let the number be n. Then, n would be a Fibonacci number if and only if either one or both of the numbers ((5 * n * n) + 4) and ((5 * n * n) - 4) is a perfect square. This condition applies only if the Fibonacci sequence starts with 0, 1, 1...

# For example, let n = 5
# Now,
# ((5 * n * n) + 4) = 5 * 5 * 5 + 4 = 125 + 4 = 129
# ((5 * n * n) - 4) = 5 * 5 * 5 - 4 = 125 - 4 = 121

# As you can see, 121 is a perfect square (11^2), so 5 is a Fibonacci Number.

n = int(input())
if checkMember(n):
    print("true")
else:
    print("false")
