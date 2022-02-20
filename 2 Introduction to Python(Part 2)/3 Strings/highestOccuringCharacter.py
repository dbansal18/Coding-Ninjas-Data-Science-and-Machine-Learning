# https://classroom.codingninjas.com/app/classroom/me/14075/content/257277/offering/3506118/problem/60

# Highest Occuring Character

# For a given a string(str), find and return the highest occurring character.
# If there are two characters in the input string with the same frequency, return the character which comes first.


from sys import stdin


def highestOccuringChar(string: str) -> str:
    freq = [0] * 26
    firstOccr = [1000001] * 26

    for i in range(len(string)):
        j = ord(string[i]) - ord("a")
        freq[j] += 1
        if firstOccr[j] == -1:
            firstOccr[j] = i

    ans = 0
    min_freq = freq[0]
    first = firstOccr[0]

    for i in range(1, 26):
        if min_freq < freq[i] or (min_freq == freq[i] and firstOccr[i] < first):
            min_freq = freq[i]
            ans = i
            first = firstOccr[i]

    return chr(ans + ord("a"))


# main
string = stdin.readline().strip()
ans = highestOccuringChar(string)

print(ans)
