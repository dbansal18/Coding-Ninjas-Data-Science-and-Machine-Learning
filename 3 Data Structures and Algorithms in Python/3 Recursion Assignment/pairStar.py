# https://classroom.codingninjas.com/app/classroom/me/14074/content/257233/offering/3505435/problem/43

# Pair Star

# Given a string S, compute recursively a new string where identical chars that are adjacent in
# the original string are separated from each other by a "*".


def pairStr(s: str) -> str:
    l = len(s)

    if l < 2:
        return s

    if s[0] == s[1]:
        return s[0] + "*" + pairStr(s[1:])
    return s[0] + pairStr(s[1:])


s = input()
print(pairStr(s))
