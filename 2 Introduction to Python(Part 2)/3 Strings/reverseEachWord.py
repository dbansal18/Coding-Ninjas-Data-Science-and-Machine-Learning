# https://classroom.codingninjas.com/app/classroom/me/14075/content/257277/offering/3506118/problem/62

# Reverse Each Word

# Aadil has been provided with a sentence in the form of a string as a function parameter.
# The task is to implement a function so as to print the sentence such that each word in the sentence is reversed.


from sys import stdin


def reverseEachWord(s: str) -> str:
    s = s.split()
    ans = ""
    for i in s:
        ans += i[-1::-1] + " "
    return ans


# main
string = stdin.readline().strip()

ans = reverseEachWord(string)

print(ans)
