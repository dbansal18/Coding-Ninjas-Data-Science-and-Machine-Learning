# https://classroom.codingninjas.com/app/classroom/me/14074/content/257243/offering/3505574/problem/14

# Reverse LL (Recursive)

# Given a singly linked list of integers, reverse it using recursion and return the head to the modified list.
# You have to do this in O(N) time complexity where N is the size of the linked list.


from sys import setrecursionlimit, stdin

setrecursionlimit(10 ** 6)

# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverseLinkedListRec(head: Node) -> Node:
    if not head:
        return head

    if not head.next:
        return head

    newHead = reverseLinkedListRec(head.next)
    head.next.next = head
    head.next = None
    return newHead


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


def printLinkedList(head):

    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


# main
t = int(stdin.readline().rstrip())

while t > 0:

    head = takeInput()

    newHead = reverseLinkedListRec(head)
    printLinkedList(newHead)

    t -= 1
