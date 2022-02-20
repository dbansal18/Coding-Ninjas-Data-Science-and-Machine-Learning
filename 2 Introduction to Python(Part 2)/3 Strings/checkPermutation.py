# https://classroom.codingninjas.com/app/classroom/me/14075/content/257277/offering/3506118/problem/349

# Check Permutation

# For a given two strings, 'str1' and 'str2', check whether they are a permutation of each other or not.


from sys import stdin


def release_list(a):
    del a[:]
    del a


def isPermutation(str1: str, str2: str) -> bool:
    arr = [0] * 26

    for c in str1:
        arr[ord(c) - ord("a")] += 1

    for c in str2:
        arr[ord(c) - ord("a")] -= 1

    for i in range(26):
        if arr[i] != 0:
            return False

    return True


# main
string1 = stdin.readline().strip()
string2 = stdin.readline().strip()

ans = isPermutation(string1, string2)

if ans:
    print("true")
else:
    print("false")
