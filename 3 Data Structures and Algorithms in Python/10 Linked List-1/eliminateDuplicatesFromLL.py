# https://classroom.codingninjas.com/app/classroom/me/14074/content/257242/offering/3505571/problem/327

# Eliminate duplicates from LL

# You have been given a singly linked list of integers where the elements are sorted in ascending order.
# Write a function that removes the consecutive duplicate values such that the given list onl
# contains unique elements and returns the head to the updated list.


from sys import stdin


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def removeDuplicates(head: Node) -> Node:
    curr = head
    while curr:
        if not curr.next:
            break

        if curr.next.data == curr.data:
            curr.next = curr.next.next
        else:
            curr = curr.next

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


# to print the linked list
def printLinkedList(head):

    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


# main
t = int(stdin.readline().strip())

while t > 0:
    head = takeInput()

    head = removeDuplicates(head)
    printLinkedList(head)

    t -= 1
