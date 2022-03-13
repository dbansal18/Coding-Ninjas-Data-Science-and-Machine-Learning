# https://classroom.codingninjas.com/app/classroom/me/14074/content/257233/offering/3505435/problem/36

# Check Palindrome (recursive)

# Check whether a given String S is a palindrome using recursion. Return true or false.


def isPalindrome(s: str) -> bool:
    l = len(s)
    if l == 0 or l == 1:
        return True

    if s[0] == s[l - 1]:
        return isPalindrome(s[1:-1])

    return False


s = input()

if isPalindrome(s):
    print("true")
else:
    print("false")
