# https://classroom.codingninjas.com/app/classroom/me/14074/content/257245/offering/3505628/problem/2244

# Queue Using LL

# Implement a Queue Data Structure specifically to store integer data using a Singly Linked List.
# The data members should be private.
# You need to implement the following public functions :
# 1. Constructor:
# It initialises the data members as required.
# 2. enqueue(data) :
# This function should take one argument of type integer. It enqueues the element into the queue and returns nothing.
# 3. dequeue() :
# It dequeues/removes the element from the front of the queue and in turn, returns the element being
# dequeued or removed. In case the queue is empty, it returns -1.
# 4. front() :
# It returns the element being kept at the front of the queue. In case the queue is empty, it returns -1.
# 5. getSize() :
# It returns the size of the queue at any given instance of time.
# 6. isEmpty() :
# It returns a boolean value indicating whether the queue is empty or not.


from sys import stdin


# Following is the structure of the node class for a Singly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    """----------------- Public Functions of Stack -----------------"""

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def enqueue(self, data):
        self.size += 1

        temp = Node(data)
        if self.size == 1:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp

    def dequeue(self):
        if self.size == 0:
            return -1
        self.size -= 1
        data = self.head.data
        self.head = self.head.next
        return data

    def front(self):
        if self.size == 0:
            return -1
        return self.head.data


# main
q = int(stdin.readline().strip())

queue = Queue()

while q > 0:

    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])

    if choice == 1:
        data = int(inputs[1])
        queue.enqueue(data)

    elif choice == 2:
        print(queue.dequeue())

    elif choice == 3:
        print(queue.front())

    elif choice == 4:
        print(queue.getSize())

    else:
        if queue.isEmpty():
            print("true")
        else:
            print("false")

    q -= 1
