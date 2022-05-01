# https://classroom.codingninjas.com/app/classroom/me/14074/content/257242/offering/3505559/problem/1142

# Length of LL

# For a given singly linked list of integers, find and return its length. Do it using an iterative method.


from sys import stdin


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None


def length(head: Node) -> int:
    l = 0
    while head:
        l += 1
        head = head.next

    return l


# Taking Input Using Fast I/O
def takeInput():
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1):
        data = datas[i]
        newNode = Node(data)

        if head is None:
            head = newNode
            tail = newNode

        else:
            tail.next = newNode
            tail = newNode

        i += 1

    return head


# to print the linked list
def printLinkedList(head):

    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


# main
t = int(stdin.readline().rstrip())

while t > 0:

    head = takeInput()
    print(length(head))

    t -= 1
