# from xml.dom.minidom import CharacterData


# Remove Character

# For a given a string(str) and a character X, write a function to remove all the occurrences of X from the given string.
# The input string will remain unchanged if the given character(X) doesn't exist in the input string.


from sys import stdin


def removeAllOccurrencesOfChar(string: str, ch: str) -> str:
    ans = ""
    for c in string:
        if c == ch:
            continue
        ans += c

    return ans


# main
string = stdin.readline().strip()
ch = stdin.readline().strip()[0]

ans = removeAllOccurrencesOfChar(string, ch)

print(ans)
