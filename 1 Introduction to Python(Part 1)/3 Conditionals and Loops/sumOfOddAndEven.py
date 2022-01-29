# https://classroom.codingninjas.com/app/classroom/me/14075/content/257268/offering/3505989/problem/466

# Sum of even & odd
# Write a program to input an integer N and print the sum of all its even digits and sum of all its odd digits separately.
# Digits mean numbers, not the places! That is, if the given integer is "13245", even digits are 2 & 4 and odd digits are 1, 3 & 5.


n = int(input())

even = 0
odd = 0

while n > 0:
    smallAns = n % 10
    if smallAns % 2 == 0:
        even += smallAns
    else:
        odd += smallAns
    n = n // 10

print(even, " ", odd)
