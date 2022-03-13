# https://classroom.codingninjas.com/app/classroom/me/14074/content/257232/offering/3505422/problem/91

# Remove Duplicates Recursively

# Given a string S, remove consecutive duplicates from it recursively.

# Problem ID 91, removeConsecutiveDuplicates
def removeConsecutiveDuplicates(s: str) -> str:
    l = len(s)
    if l == 0 or l == 1:
        return s

    if s[0] == s[1]:
        return removeConsecutiveDuplicates(s[1:])

    return s[0] + removeConsecutiveDuplicates(s[1:])


string = input().strip()
print(removeConsecutiveDuplicates(string))
