# https://classroom.codingninjas.com/app/classroom/me/14075/content/257268/offering/3505980/problem/3082

# Sum of n numbers
# Given an integer n, find and print the sum of numbers from 1 to n.

n = int(input())

i = 1
sum = 0

while i <= n:
    sum += i
    i += 1

print(sum)
