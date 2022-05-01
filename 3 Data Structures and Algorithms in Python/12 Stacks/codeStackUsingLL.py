# https://classroom.codingninjas.com/app/classroom/me/14074/content/257244/offering/3505600/problem/1474

# Code : Stack Using LL

# Implement a Stack Data Structure specifically to store integer data using a Singly Linked List.
# The data members should be private.
# You need to implement the following public functions :
# 1. Constructor:
#     It initialises the data members as required.
# 2. push(data) :
#     This function should take one argument of type integer. It pushes the element into the stack and returns nothing.
# 3. pop() :
#     It pops the element from the top of the stack and in turn, returns the element being popped or deleted.
#     In case the stack is empty, it returns -1.
# 4. top :
#     It returns the element being kept at the top of the stack. In case the stack is empty, it returns -1.
# 5. size() :
#     It returns the size of the stack at any given instance of time.
# 6. isEmpty() :
#     It returns a boolean value indicating whether the stack is empty or not.


from sys import stdin


# Following is the structure of the node class for a Singly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.__head = None
        self.__size = 0

    def getSize(self) -> int:
        return self.__size

    def isEmpty(self) -> bool:
        return self.__size == 0

    def push(self, data) -> None:
        newHead = Node(data)
        newHead.next = self.__head
        self.__head = newHead
        self.__size += 1

    def pop(self) -> int:
        if self.__size == 0:
            return -1
        top = self.top()
        self.__head = self.__head.next
        self.__size -= 1
        return top

    def top(self) -> int:
        if self.__size == 0:
            return -1
        return self.__head.data


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
