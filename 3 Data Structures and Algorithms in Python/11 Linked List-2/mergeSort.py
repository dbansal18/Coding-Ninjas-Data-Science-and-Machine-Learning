# https://classroom.codingninjas.com/app/classroom/me/14074/content/257243/offering/3505587/problem/17

# Code : Merge Sort

# Given a singly linked list of integers, sort it using 'Merge Sort.'


from sys import setrecursionlimit, stdin

setrecursionlimit(10 ** 6)

# Following is the Node class already written for the Linked List
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


def mergeTwoSortedLinkedLists(head1: Node, head2: Node) -> Node:
    if (not head1) and (not head2):
        return None

    if not head1:
        return head2

    if not head2:
        return head1

    if head1.data > head2.data:
        head = head2
        head2 = head2.next
    else:
        head = head1
        head1 = head1.next

    curr = head

    while head1 and head2:
        if head1.data > head2.data:
            curr.next = head2
            head2 = head2.next
        else:
            curr.next = head1
            head1 = head1.next
        curr = curr.next

    if head1:
        curr.next = head1
    if head2:
        curr.next = head2

    return head


def mergeSort(head: Node) -> Node:
    if not head:
        return head

    if head.next == None:
        return head

    mid = midPoint(head)
    head2 = mid.next
    mid.next = None
    newHead1 = mergeSort(head)
    newHead2 = mergeSort(head2)
    finalHead = mergeTwoSortedLinkedLists(newHead1, newHead2)
    return finalHead


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

    newHead = mergeSort(head)
    printLinkedList(newHead)

    t -= 1
