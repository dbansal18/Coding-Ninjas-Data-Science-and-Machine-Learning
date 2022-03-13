# https://classroom.codingninjas.com/app/classroom/me/14074/content/257232/offering/3505420/problem/39

# Remove X

# Given a string, compute recursively a new string where all 'x' chars have been removed.


def removeX(string: str) -> str:
    if len(string) == 0:
        return ""

    if string[0] == "x":
        return removeX(string[1:])
    return string[0] + removeX(string[1:])


# Main
string = input()
print(removeX(string))
