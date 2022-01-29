# https://classroom.codingninjas.com/app/classroom/me/14075/content/257268/offering/3505989/problem/479

# Palindrome number
# Write a program to determine if given number is palindrome or not. Print true if it is palindrome, false otherwise.
# Palindrome are the numbers for which reverse is exactly same as the original one. For eg. 121


def checkPalindrome(num):
    n = num
    rev = 0
    while n > 0:
        rev = (rev * 10) + (n % 10)
        n = n // 10
    return num == rev


num = int(input())
isPalindrome = checkPalindrome(num)
if isPalindrome:
    print("true")
else:
    print("false")
