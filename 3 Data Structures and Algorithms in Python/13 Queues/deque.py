# https://classroom.codingninjas.com/app/classroom/me/14074/content/257246/offering/3505629/problem/1337

# Dequeue

# You need to implement a class for Dequeue i.e. for double ended queue.
# In this queue, elements can be inserted and deleted from both the ends.
# You don't need to double the capacity.
# You need to implement the following functions -
# 1. constructor
# You need to create the appropriate constructor. Size for the queue passed is 10.
# 2. insertFront -
# This function takes an element as input and insert the element at the front of queue.
# Insert the element only if queue is not full. And if queue is full, print -1 and return.
# 3. insertRear -
# This function takes an element as input and insert the element at the end of queue.
# Insert the element only if queue is not full. And if queue is full, print -1 and return.
# 4. deleteFront -
# This function removes an element from the front of queue. Print -1 if queue is empty.
# 5. deleteRear -
# This function removes an element from the end of queue. Print -1 if queue is empty.
# 6. getFront -
# Returns the element which is at front of the queue. Return -1 if queue is empty.
# 7. getRear -
# Returns the element which is at end of the queue. Return -1 if queue is empty.


## Read input as specified in the question.
## Print output as specified in the question.
import collections


class Dequeue:
    def __init__(self, maxSize=10):
        self.__size = 0
        self.__q = collections.deque()
        self.__max_size = maxSize

    def __is_full(self):
        return self.__max_size == self.__size

    def __is_empty(self):
        return self.__size == 0

    def __print_error(self):
        print(-1)

    def insertFront(self, ele):
        if self.__is_full():
            self.__print_error()
            return

        self.__q.appendleft(ele)
        self.__size += 1

    def insertRear(self, ele):
        if self.__is_full():
            self.__print_error()
            return

        self.__q.append(ele)
        self.__size += 1

    def deleteFront(self):
        if self.__is_empty():
            return -1

        self.__size -= 1
        return self.__q.popleft()

    def deleteRear(self):
        if self.__is_empty():
            return -1

        self.__size -= 1
        return self.__q.pop()

    def getFront(self):
        if self.__is_empty():
            return -1
        ele = self.deleteFront()
        self.insertFront(ele)
        return ele

    def getRear(self):
        if self.__is_empty():
            return -1

        ele = self.deleteRear()
        self.insertRear(ele)
        return ele


inputs = input().strip().split(" ")
n = len(inputs)
i = 0
queue = Dequeue()

while True:
    if i >= n:
        break

    choice = int(inputs[i])

    if choice == 1:
        queue.insertFront(int(inputs[i + 1]))
        i += 2
    elif choice == 2:
        queue.insertRear(int(inputs[i + 1]))
        i += 2
    elif choice == 3:
        ele = queue.deleteFront()

        # print(queue.deleteFront())
        if ele == -1:
            print(-1)
        i += 1
    elif choice == 4:
        ele = queue.deleteRear()
        # print(queue.deleteRear())
        if ele == -1:
            print(-1)
        i += 1
    elif choice == 5:
        print(queue.getFront())
        i += 1
    elif choice == 6:
        print(queue.getRear())
        i += 1
    else:
        break
