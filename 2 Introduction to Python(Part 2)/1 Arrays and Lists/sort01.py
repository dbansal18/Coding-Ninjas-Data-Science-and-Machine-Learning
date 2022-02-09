# https://classroom.codingninjas.com/app/classroom/me/14075/content/257275/offering/3506079/problem/23

# Sort 0 1

# You have been given an integer array/list(ARR) of size N that contains only integers, 0 and 1.
# Write a function to sort this array/list.
# Think of a solution which scans the array/list only once and don't require use of an extra array/list.

from sys import stdin

def sortZeroesAndOne(arr, n) :
    zeros = 0
    ones = 0
    for ele in arr:
        if ele:
            ones += 1
        else:
            zeros += 1
    for i in range(zeros):
        arr[i] = 0
    for i in range(zeros, ones+zeros):
        arr[i] = 1
    return arr


# # Alternative better solution
# def sortZeroesAndOne(arr, n) :
#     nextZero = 0
#     for i in range(n):
#         if arr[i] == 0:
#             temp = arr[nextZero]
#             arr[nextZero] = arr[i]
#             arr[i] = temp
#             nextZero += 1


#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())

    if n == 0 :
        return list(), 0

    
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = ' ')
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    sortZeroesAndOne(arr, n)
    printList(arr, n)
    print()

    t -= 1