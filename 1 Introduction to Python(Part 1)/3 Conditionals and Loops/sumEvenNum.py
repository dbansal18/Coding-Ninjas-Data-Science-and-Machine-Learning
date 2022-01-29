# https://classroom.codingninjas.com/app/classroom/me/14075/content/257268/offering/3505981/problem/965

# Sum of Even Numbers
# Given a number N, print sum of all even numbers from 1 to N.


n = int(input())

i = 2
sum = 0

while i <= n:
    sum += i
    i += 2

print(sum)
