# https://classroom.codingninjas.com/app/classroom/me/14074/content/257243/offering/3505583/problem/328

# Midpoint of Linked list

# For a given singly linked list of integers, find and return the node present at the middle of the list.


from sys import stdin


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def midPoint(head: Node) -> Node:
    if not head:
        return head

    slow = fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow


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


# Main
t = int(stdin.readline().rstrip())

while t > 0:

    head = takeInput()
    mid = midPoint(head)

    if mid is not None:
        print(mid.data)

    t -= 1
