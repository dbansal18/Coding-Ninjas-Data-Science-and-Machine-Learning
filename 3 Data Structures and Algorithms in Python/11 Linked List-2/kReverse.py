# https://classroom.codingninjas.com/app/classroom/me/14074/content/257243/offering/3505591/problem/7

# kReverse

# Given a singly linked list of integers, reverse the nodes of the linked list 'k' at a time and return its modified list.
# 'k' is a positive integer and is less than or equal to the length of the linked list.
# If the number of nodes is not a multiple of 'k,' then left-out nodes, in the end, should be reversed as well.
# Example :
# Given this linked list: 1 -> 2 -> 3 -> 4 -> 5

# For k = 2, you should return: 2 -> 1 -> 4 -> 3 -> 5

# For k = 3, you should return: 3 -> 2 -> 1 -> 5 -> 4


from sys import stdin


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverseList(head: Node) -> Node:
    if (not head) or (not head.next):
        return head
    newTail = head
    prev = None
    while head:
        temp = head.next
        head.next = prev
        prev = head
        head = temp

    return prev, newTail


def kReverse(head: Node, k: int) -> Node:
    if k == 0 or k == 1:
        return head
    if not head:
        return head

    i = 1
    curr = head

    while i < k and curr:
        curr = curr.next
        i += 1

    if not curr:
        smallHead, smallTail = reverseList(head)
        return smallHead

    smallList = curr.next
    curr.next = None
    smallHead, smallTail = reverseList(head)
    smallList = kReverse(smallList, k)
    smallTail.next = smallList
    return smallHead


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
    k = int(stdin.readline().strip())

    newHead = kReverse(head, k)
    printLinkedList(newHead)

    t -= 1
