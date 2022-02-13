# https://classroom.codingninjas.com/app/classroom/me/14075/content/257276/offering/3506100/problem/22

# Sum of Two Arrays

# Two random integer arrays/lists have been given as ARR1 and ARR2 of size N and M respectively.
# Both the arrays/lists contain numbers from 0 to 9(i.e. single digit integer is present at every index
# The idea here is to represent each array/list as an integer in itself of digits N and M.
# You need to find the sum of both the input arrays/list treating them as two integers and put the result
# in another array/list i.e. output array/list will also contain only single digit at every index.

from sys import stdin


def sumOfTwoArrays(arr1: list, n: int, arr2: list, m: int, output: list) -> None:
    carry = 0
    n -= 1
    m -= 1
    i = len(output) - 1
    while n >= 0 or m >= 0:
        if n < 0:
            output[i] = arr2[m] + carry
            carry = output[i] // 10
            output[i] = output[i] % 10
            m -= 1
            i -= 1
        elif m < 0:
            output[i] = arr1[n] + carry
            carry = output[i] // 10
            output[i] = output[i] % 10
            n -= 1
            i -= 1
        else:
            output[i] = arr2[m] + arr1[n] + carry
            carry = output[i] // 10
            output[i] = output[i] % 10
            m -= 1
            n -= 1
            i -= 1
    output[0] = carry


# Taking Input Using Fast I/O
def takeInput():
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


# to print the array/list
def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")

    print()


# main
t = int(stdin.readline().rstrip())

while t > 0:
    arr1, n = takeInput()
    arr2, m = takeInput()

    outputSize = 1 + max(n, m)
    output = outputSize * [0]

    sumOfTwoArrays(arr1, n, arr2, m, output)
    printList(output, outputSize)

    t -= 1
