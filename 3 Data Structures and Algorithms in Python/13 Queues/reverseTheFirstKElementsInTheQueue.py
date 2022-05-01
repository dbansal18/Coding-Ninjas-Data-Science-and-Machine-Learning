# https://classroom.codingninjas.com/app/classroom/me/14074/content/257245/offering/3505628/problem/2244

# Reverse the First K Elements in the Queue

# For a given queue containing all integer data, reverse the first K elements.
# You have been required to make the desired change in the input queue itself.


import queue
from sys import stdin


def reverseQHelper(q, n):
    if n == 1:
        return

    ele = q.get()
    reverseQHelper(q, n - 1)
    q.put(ele)


def reverseQueue(inputQueue):
    n = inputQueue.qsize()
    reverseQHelper(inputQueue, n)


def swapQ(q1, q2):
    while not q1.empty():
        q2.put(q1.get())


def reverseKElements(q, k):
    if k < 2:
        return q

    tempQ = queue.Queue()

    for i in range(k):
        tempQ.put(q.get())

    reverseQueue(tempQ)
    swapQ(q, tempQ)
    return tempQ


"""-------------- Utility Functions --------------"""


# Takes a list as a stack and returns whether the stack is empty or not
def isEmpty(stack):
    return len(stack) == 0


# Takes a list as a stack and returns the element at the top
def top(stack):
    # assuming the stack is never empty
    return stack[len(stack) - 1]


def takeInput():
    n_k = list(map(int, stdin.readline().strip().split(" ")))
    n = n_k[0]
    k = n_k[1]

    qu = queue.Queue()
    values = list(map(int, stdin.readline().strip().split()))

    for i in range(n):
        qu.put(values[i])

    return k, qu


# main
k, qu = takeInput()

qu = reverseKElements(qu, k)

while not qu.empty():
    print(qu.get(), end=" ")
