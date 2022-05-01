# https://classroom.codingninjas.com/app/classroom/me/14074/content/257245/offering/3505628/problem/420

# Reverse Queue

# You have been given a queue that can store integers as the data.
# You are required to write a function that reverses the populated queue itself without using any other data structures.


import queue
from sys import setrecursionlimit, stdin

setrecursionlimit(10 ** 6)


def reverseQHelper(q, n):
    if n == 1:
        return

    ele = q.get()
    reverseQHelper(q, n - 1)
    q.put(ele)


def reverseQueue(inputQueue):
    n = inputQueue.qsize()

    reverseQHelper(inputQueue, n)


"""-------------- Utility Functions --------------"""


def takeInput():
    n = int(stdin.readline().strip())

    qu = queue.Queue()
    values = list(map(int, stdin.readline().strip().split()))

    for i in range(n):
        qu.put(values[i])

    return qu


# main
t = int(stdin.readline().strip())

while t > 0:

    qu = takeInput()
    reverseQueue(qu)

    while not qu.empty():
        print(qu.get(), end=" ")

    print()

    t -= 1
