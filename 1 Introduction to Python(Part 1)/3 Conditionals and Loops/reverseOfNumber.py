# https://classroom.codingninjas.com/app/classroom/me/14075/content/257268/offering/3505989/problem/468

# Reverse of a number
# Write a program to generate the reverse of a given number N. Print the corresponding reverse number.
# Note : If a number has trailing zeros, then its reverse will not include them. For e.g., reverse of 10400 will be 401 instead of 00401.


n = int(input())
rev = 0

while n > 0:
    rev = (rev * 10) + (n % 10)
    n = n // 10

print(rev)
