# https://classroom.codingninjas.com/app/classroom/me/14074/content/257242/offering/3505571/problem/6

# AppendLastNToFirst

# You have been given a singly linked list of integers along with an integer 'N'.
# Write a function to append the last 'N' nodes towards the front of the singly linked list
# and returns the new head to the list.


from sys import stdin


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def lenLL(head: Node) -> int:
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next

    return length


def lastNode(head: Node) -> Node:
    while head.next:
        head = head.next

    return head


def appendLastNToFirst(head: Node, n: int) -> Node:
    if n == 0:
        return head

    curr = head
    l = lenLL(head)
    if l == 0:
        return head
    i = 1
    j = l - n

    while curr:
        if i == j:
            break
        curr = curr.next
        i += 1

    newHead = curr.next
    last = lastNode(head)
    last.next = head
    curr.next = None
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
    n = int(stdin.readline().rstrip())

    head = appendLastNToFirst(head, n)
    printLinkedList(head)

    t -= 1
