# https://classroom.codingninjas.com/app/classroom/me/14074/content/257243/offering/3505591/problem/331

# Even after Odd LinkedList

# For a given singly linked list of integers, arrange the elements such that all the even numbers are
# placed after the odd numbers. The relative order of the odd and even terms should remain unchanged.


from sys import stdin


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def evenAfterOdd(head: Node) -> Node:
    oddHead = evenHead = oddTail = evenTail = None

    while head:
        curr = head
        head = head.next
        curr.next = None

        if curr.data % 2 == 0:
            if not evenHead:
                evenHead = evenTail = curr
            else:
                evenTail.next = curr
                evenTail = evenTail.next
        else:
            if not oddHead:
                oddHead = oddTail = curr
            else:
                oddTail.next = curr
                oddTail = oddTail.next

    if not oddHead:
        return evenHead

    oddTail.next = evenHead
    return oddHead


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
    newHead = evenAfterOdd(head)
    printLinkedList(newHead)

    t -= 1
