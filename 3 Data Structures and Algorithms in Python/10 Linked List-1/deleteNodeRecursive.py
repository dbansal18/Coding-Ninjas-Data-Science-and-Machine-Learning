# https://classroom.codingninjas.com/app/classroom/me/14074/content/257242/offering/3505568/problem/325

# Delete node (recursive)

# Given a singly linked list of integers and position 'i', delete the node present at the 'i-th'
# position in the linked list recursively.

# Note :
# Assume that the Indexing for the linked list always starts from 0.

# No need to print the list, it has already been taken care. Only return the new head to the list.


from sys import setrecursionlimit, stdin

setrecursionlimit(10 ** 6)

# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def deleteNodeRec(head: Node, pos: int) -> Node:
    if not head:
        return None

    if pos == 0:
        return head.next

    smallHead = deleteNodeRec(head.next, pos - 1)
    head.next = smallHead
    return head


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
    pos = int(stdin.readline().rstrip())

    newHead = deleteNodeRec(head, pos)
    printLinkedList(newHead)

    t -= 1
