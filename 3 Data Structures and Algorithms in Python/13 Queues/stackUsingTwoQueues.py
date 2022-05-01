# https://classroom.codingninjas.com/app/classroom/me/14074/content/257245/offering/3505626/problem/1416

# Stack Using 2 Queues

# Implement a Stack Data Structure specifically to store integer data using two Queues.
# You have to implement it in such a way that the push operation is done in O(1) time and
# the pop and top operations are done in O(N) time.
# There should be two data members, both being Queues to store the data internally. You may use the inbuilt Queue.
# Implement the following public functions :
# 1. Constructor:
# It initialises the data members as required.
# 2. push(data) :
# This function should take one argument of type integer. It pushes the element into the stack and returns nothing.
# 3. pop() :
# It pops the element from the top of the stack and in turn, returns the element being popped or deleted.
# In case the stack is empty, it returns -1.
# 4. top :
# It returns the element being kept at the top of the stack. In case the stack is empty, it returns -1.
# 5. size() :
# It returns the size of the stack at any given instance of time.
# 6. isEmpty() :
# It returns a boolean value indicating whether the stack is empty or not.


from queue import Queue
from sys import stdin


class Stack:
    def __init__(self):
        self.__q1 = Queue()
        self.__q2 = Queue()
        self.__size = 0

    """----------------- Public Functions of Stack -----------------"""

    def getSize(self):
        return self.__size

    def isEmpty(self):
        return self.__size == 0

    def push(self, data):
        self.__q1.put(data)
        self.__size += 1

    def pop(self):
        if self.__size == 0:
            return -1

        for i in range(self.__size - 1):
            ele = self.__q1.get()
            self.__q2.put(ele)

        self.__size -= 1
        self.__q1, self.__q2 = self.__q2, self.__q1
        return self.__q2.get()

    def top(self):
        if self.__size == 0:
            return -1

        for i in range(self.__size - 1):
            ele = self.__q1.get()
            self.__q2.put(ele)

        self.__q1, self.__q2 = self.__q2, self.__q1
        top = self.__q2.get()
        self.__q1.put(top)
        return top


# main
q = int(stdin.readline().strip())

stack = Stack()

while q > 0:

    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])

    if choice == 1:
        data = int(inputs[1])
        stack.push(data)

    elif choice == 2:
        print(stack.pop())

    elif choice == 3:
        print(stack.top())

    elif choice == 4:
        print(stack.getSize())

    else:
        if stack.isEmpty():
            print("true")
        else:
            print("false")

    q -= 1
