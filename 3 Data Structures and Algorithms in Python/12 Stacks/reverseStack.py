# https://classroom.codingninjas.com/app/classroom/me/14074/content/257244/offering/3505608/problem/419

# Reverse Stack
# Send Feedback
# You have been given two stacks that can store integers as the data. Out of the two given stacks,
# one is populated and the other one is empty.
# You are required to write a function that reverses the populated stack using the one which is empty.


from sys import setrecursionlimit, stdin

setrecursionlimit(10 ** 6)


def insertAtBottom(stack, item):
    if isEmpty(stack):
        stack.append(item)
    else:
        temp = stack.pop()
        insertAtBottom(stack, item)
        stack.append(temp)


def reverse(stack):
    if not isEmpty(stack):
        temp = stack.pop()
        reverse(stack)
        insertAtBottom(stack, temp)


def reverseStack(inputStack, extraStack):
    reverse(inputStack)


"""-------------- Utility Functions --------------"""

# Takes a list as a stack and returns whether the stack is empty or not
def isEmpty(stack):
    return len(stack) == 0


# Taking input using fast I/o method
def takeInput():
    size = int(stdin.readline().strip())
    inputStack = list()

    if size == 0:
        return inputStack

    values = list(map(int, stdin.readline().strip().split(" ")))
    inputStack = values

    return inputStack


# Main
inputStack = takeInput()
emptyStack = list()

reverseStack(inputStack, emptyStack)

while not isEmpty(inputStack):
    print(inputStack.pop(), end=" ")
