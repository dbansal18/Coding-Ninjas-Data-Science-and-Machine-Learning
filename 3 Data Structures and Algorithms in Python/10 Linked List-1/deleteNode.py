# https://classroom.codingninjas.com/app/classroom/me/14074/content/257242/offering/3505563/problem/1140

# Delete node

# You have been given a linked list of integers.
# Your task is to write a function that deletes a node from agiven position, 'POS'.

# Note :
# Assume that the Indexing for the linked list always starts from 0.

# If the position is greater than or equal to the length of the linked list,
# you should return the same linked list without any change.


from sys import stdin


# Following is the Node class already written for the Linked List.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def length(head: Node) -> int:
    l = 0
    while head:
        l += 1
        head = head.next

    return l


def deleteNode(head: Node, pos: int) -> Node:
    l = length(head)
    if pos + 1 > l:
        return head
    curr = head
    prev = None

    i = 0
    while i < pos and curr:
        prev = curr
        curr = curr.next
        i += 1

    if prev:
        prev.next = curr.next
    else:
        head = head.next

    return head


# Taking Input Using Fast I/O.
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


# To print the linked list.
def printLinkedList(head):

    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


# Main.
t = int(stdin.readline().strip())

while t > 0:

    head = takeInput()
    pos = int(stdin.readline().rstrip())

    head = deleteNode(head, pos)
    printLinkedList(head)

    t -= 1
