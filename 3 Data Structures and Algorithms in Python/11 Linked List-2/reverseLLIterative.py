# https://classroom.codingninjas.com/app/classroom/me/14074/content/257243/offering/3505580/problem/13

# Reverse LL (Iterative)

# Given a singly linked list of integers, reverse it iteratively and return the head to the modified list.


from sys import setrecursionlimit, stdin

setrecursionlimit(10 ** 6)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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


# To print the linked list
def printLinkedList(head):

    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


def reverse(head: Node) -> Node:
    if (not head) or (not head.next):
        return head

    prev = None
    while head:
        temp = head.next
        head.next = prev
        prev = head
        head = temp

    return prev


# Main
t = int(stdin.readline().rstrip())

while t > 0:

    head = takeInput()

    ans = reverse(head)
    printLinkedList(ans)

    t -= 1
