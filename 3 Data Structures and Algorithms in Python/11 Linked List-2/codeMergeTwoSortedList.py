# https://classroom.codingninjas.com/app/classroom/me/14074/content/257243/offering/3505585/problem/1144

# Code : Merge two sorted LL

# You have been given two sorted(in ascending order) singly linked lists of integers.
# Write a function to merge them in such a way that the resulting singly linked list is also sorted(in ascending order)
# and return the new head to the list.


from sys import stdin


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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


# Main
t = int(stdin.readline().rstrip())

while t > 0:

    head1 = takeInput()
    head2 = takeInput()

    newHead = mergeTwoSortedLinkedLists(head1, head2)
    printLinkedList(newHead)

    t -= 1
