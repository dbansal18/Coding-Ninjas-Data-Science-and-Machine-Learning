# https://classroom.codingninjas.com/app/classroom/me/14075/content/257277/offering/3506112/problem/983

# Check Palindrome

# Given a string, determine if it is a palindrome, considering only alphanumeric characters.


from sys import stdin


def isPalindrome(string: str) -> bool:
    return string == string[-1::-1]


# main
string = stdin.readline().strip()
ans = isPalindrome(string)

if ans:
    print("true")
else:
    print("false")
