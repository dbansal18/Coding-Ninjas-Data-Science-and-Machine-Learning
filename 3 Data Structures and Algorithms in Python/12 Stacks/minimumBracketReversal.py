# https://classroom.codingninjas.com/app/classroom/me/14074/content/257244/offering/3505611/problem/348

# Minimum bracket Reversal

# For a given expression in the form of a string, find the minimum number of brackets that can be reversed
# in order to make the expression balanced. The expression will only contain curly brackets.
# If the expression can't be balanced, return -1.


from sys import stdin


def countBracketReversals(exp: str) -> int:
    n = len(exp)

    if n == 0:
        return 0
    if n % 2 == 1:
        return -1

    ans = 0
    i = 0
    for ele in exp:
        if ele == "{":
            ans += 1
        else:
            ans -= 1

        if ans < 0:
            ans = 1
            i += 1
    return i + ans // 2


# main
print(countBracketReversals(stdin.readline().strip()))
