# https://classroom.codingninjas.com/app/classroom/me/14074/content/257242/offering/3505560/problem/1141

# Print ith node

# For a given a singly linked list of integers and a position 'i', print the node data at the 'i-th' position.


from sys import stdin


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


def printIthNode(head: Node, i: int) -> int:
    j = 0
    while head:
        if i == j:
            print(head.data)
            return
        head = head.next
        j += 1


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
    i = int(stdin.readline().rstrip())
    printIthNode(head, i)

    t -= 1
