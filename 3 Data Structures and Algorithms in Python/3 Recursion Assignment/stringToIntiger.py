# https://classroom.codingninjas.com/app/classroom/me/14074/content/257233/offering/3505435/problem/40

# String to Integer

# Write a recursive function to convert a given string into the number it represents.
# That is input will be a numeric string that contains only numbers,
# you need to convert the string into corresponding integerand return the answer.


def strToInt(s: str) -> int:
    l = len(s)

    if l == 0:
        return 0

    smallAns = int(s[0])

    if l == 1:
        return smallAns
    else:
        return smallAns * (10 ** (l - 1)) + strToInt(s[1:])


n = input()
print(strToInt(n))
