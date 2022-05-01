# https://classroom.codingninjas.com/app/classroom/me/14074/content/257242/offering/3505571/problem/329

# Print Reverse LinkedList

# You have been given a singly linked list of integers. Write a function to print the list in a reverse order.
# To explain it further, you need to start printing the data from the tail and move towards the head of the list,
# printing the head data at the end.


from sys import setrecursionlimit, stdin

setrecursionlimit(10 ** 6)

# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def printReverse(head: Node) -> None:
    if not head:
        return

    printReverse(head.next)
    print(head.data, end=" ")


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
    printReverse(head)
    print()

    t -= 1
