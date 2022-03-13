# https://classroom.codingninjas.com/app/classroom/me/14074/content/257233/offering/3505435/problem/55

# Check AB

# Suppose you have a string, S, made up of only 'a's and 'b's.
# Write a recursive function that checks if the string was generated using the following rules:
# a. The string begins with an 'a'
# b. Each 'a' is followed by nothing or an 'a' or "bb"
# c. Each "bb" is followed by nothing or an 'a'
# If all the rules are followed by the given string, return true otherwise return false.


def checkAB(s: str, check: str) -> bool:
    l = len(s)

    if l <= 0:
        return True

    if s.find(check) == 0:
        if check == "bb":
            return checkAB(s[2:], "a") or checkAB(s[2:], "")
        if check == "a":
            return checkAB(s[1:], "a") or checkAB(s[1:], "bb") or checkAB(s[1:], "")
        else:
            return False
    else:
        return False


s = input()
if checkAB(s, "a"):
    print("true")
else:
    print("false")
