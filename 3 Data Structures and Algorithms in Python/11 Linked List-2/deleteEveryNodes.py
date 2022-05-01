# https://classroom.codingninjas.com/app/classroom/me/14074/content/257243/offering/3505591/problem/367

# Delete every N nodes

# You have been given a singly linked list of integers along with two integers, 'M,' and 'N.'
# Traverse the linked list such that you retain the 'M' nodes, then delete the next 'N' nodes.
# Continue the same until the end of the linked list.
# To put it in other words, in the given linked list, you need to delete N nodes after every M nodes.


from sys import stdin


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def skipMdeleteN(head: Node, m: int, n: int) -> Node:
    if not head:
        return head
    if n == 0:
        return head
    if m == 0:
        return None

    curr = head
    prevTail = None
    while curr:

        i = 1
        while i < m and curr:
            curr = curr.next
            i += 1
        prevTail = curr
        if not curr:
            break
        curr = curr.next
        prevTail.next = None

        i = 1
        while i < n and curr:
            curr = curr.next
            i += 1

        if curr:
            curr = curr.next
            prevTail.next = curr

    return head


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
    m_n = stdin.readline().strip().split(" ")

    m = int(m_n[0])
    n = int(m_n[1])

    newHead = skipMdeleteN(head, m, n)
    printLinkedList(newHead)

    t -= 1
