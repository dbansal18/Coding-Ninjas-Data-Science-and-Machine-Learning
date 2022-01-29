# https://classroom.codingninjas.com/app/classroom/me/14075/content/257272/offering/3506050/problem/478

# Check Armstrong

# Write a Program to determine if the given number is Armstrong number or not. Print true if number is armstrong, otherwise print false.
# An Armstrong number is a number (with digits n) such that the sum of its digits raised to nth power is equal to the number itself.
# For example,
# 371, as 3^3 + 7^3 + 1^3 = 371
# 1634, as 1^4 + 6^4 + 3^4 + 4^4 = 1634


def checkArmstrong(num: int):
    l = len(str(num))
    sum = 0
    n = num
    while n > 0:
        sum += (n % 10) ** l
        n = n // 10
    if sum == num:
        return True
    return False


num = int(input())
if checkArmstrong(num):
    print("true")
else:
    print("false")
