# https://classroom.codingninjas.com/app/classroom/me/14075/content/257276/offering/3506100/problem/186

# Second Largest in array

# You have been given a random integer array/list(ARR) of size N. You are required to find and return the second largest
# element present in the array/list.
# If N <= 1 or all the elements are same in the array/list then return -2147483648 or
# -2 ^ 31(It is the smallest value for the range of Integer)


from sys import stdin


def secondLargestElement(arr: list, n: int) -> int:
    # Base case
    int_min = -2147483648
    if n <= 1:
        return int_min
    lar = int_min
    ans = int_min
    for i in range(n):
        if lar < arr[i]:
            ans = lar
            lar = arr[i]
        elif ans < arr[i] and arr[i] != lar:
            ans = arr[i]
    if ans == lar:
        return int_min
    return ans


# Taking Input Using Fast I/O
def takeInput():
    n = int(stdin.readline().rstrip())
    if n != 0:
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n

    return list(), 0


# main
t = int(stdin.readline().rstrip())

while t > 0:

    arr, n = takeInput()
    print(secondLargestElement(arr, n))

    t -= 1
