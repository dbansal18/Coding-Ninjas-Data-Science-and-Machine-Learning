# https://classroom.codingninjas.com/app/classroom/me/14075/content/257268/offering/3505989/problem/971

# Nth Fibonacci Number
# Nth term of Fibonacci series F(n), where F(n) is a function, is calculated using the following formula -
#     F(n) = F(n-1) + F(n-2),
#     Where, F(1) = F(2) = 1
# Provided N you have to find out the Nth Fibonacci Number.

n = int(input())
i = 1
j = 1

if n == 1 or n == 2:
    print(1)
else:
    k = 3
    while k <= n:
        temp = i + j
        i = j
        j = temp
        k += 1
    print(j)
