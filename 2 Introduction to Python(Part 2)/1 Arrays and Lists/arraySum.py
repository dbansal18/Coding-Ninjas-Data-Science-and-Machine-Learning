# https://classroom.codingninjas.com/app/classroom/me/14075/content/257275/offering/3506068/problem/1101

# Array Sum

# Given an array of length N, you need to find and print the sum of all elements of the array.
# Input Format :
# Line 1 : An Integer N i.e. size of array
# Line 2 : N integers which are elements of the array, separated by spaces


def arraySum(n: int, li: list) -> int:
    sum = 0
    for i in li:
        sum += i
    return sum


if __name__ == "__main__":
    n = int(input())
    li = [int(x) for x in input().split()]
    print(arraySum(n, li))
