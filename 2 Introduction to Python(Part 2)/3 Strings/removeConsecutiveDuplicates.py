# https://classroom.codingninjas.com/app/classroom/me/14075/content/257277/offering/3506118/problem/59

# Remove Consecutive Duplicates

# For a given string(str), remove all the consecutive duplicate characters.


from sys import stdin


def removeConsecutiveDuplicates(s: str) -> str:
    if len(s) < 2:
        return s

    ans = ""

    for i in range(1, len(s)):
        if s[i - 1] != s[i]:
            ans += s[i - 1]
    return ans + s[-1]


# main
string = stdin.readline().strip()

ans = removeConsecutiveDuplicates(string)

print(ans)
