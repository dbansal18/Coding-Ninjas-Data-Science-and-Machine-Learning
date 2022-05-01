# https://classroom.codingninjas.com/app/classroom/me/14074/content/257243/offering/3505591/problem/1147

# Find a node in LL (recursive)

# Given a singly linked list of integers and an integer n, find and return the index for
# the first occurrence of 'n' in the linked list. -1 otherwise.
# Follow a recursive approach to solve this.


from sys import setrecursionlimit, stdin

setrecursionlimit(10 ** 6)

# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def findNodeRec(head: Node, n: int) -> int:
    if not head:
        return -1

    if head.data == n:
        return 0

    smallAns = findNodeRec(head.next, n)

    if smallAns == -1:
        return -1

    return 1 + smallAns


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
    n = int(stdin.readline().rstrip())

    print(findNodeRec(head, n))

    t -= 1
