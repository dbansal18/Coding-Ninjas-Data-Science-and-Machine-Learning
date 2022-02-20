# https://classroom.codingninjas.com/app/classroom/me/14075/content/257277/offering/3506118/problem/65


# Compress the String

# Write a program to do basic string compression. For a character which is consecutively repeated more than once,
# replace consecutive duplicate occurrences with the count of repetitions.

from sys import stdin


def getCompressedString(input: str) -> str:
    if len(input) < 2:
        return input
    ans = ""
    i = 0
    count = 0
    while i < (len(input) - 1):
        if input[i] == input[i + 1]:
            count += 1
        else:
            ans += input[i]
            count += 1
            if count > 1:
                ans += str(count)
            count = 0
        i += 1

    ans += input[i]
    count += 1
    if count > 1:
        ans += str(count)

    return ans


# Main.
string = stdin.readline().strip()
ans = getCompressedString(string)
print(ans)
