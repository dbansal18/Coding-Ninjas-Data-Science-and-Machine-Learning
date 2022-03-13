# https://classroom.codingninjas.com/app/classroom/me/14074/content/257233/offering/3505435/problem/846

# Staircase

# A child is running up a staircase with N steps, and can hop either 1 step, 2 steps or 3 steps at a time.
# Implement a method to count how many possible ways the child can run up to the stairs.
# You need to return number of possible ways W.


def staircase(n: int) -> int:
    if n == 0:
        return 1
    if n < 0:
        return 0

    return staircase(n - 1) + staircase(n - 2) + staircase(n - 3)


n = int(input())
print(staircase(n))
