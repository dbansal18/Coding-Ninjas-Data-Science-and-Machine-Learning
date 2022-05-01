# https://classroom.codingninjas.com/app/classroom/me/14074/content/257243/offering/3505591/problem/332

# Bubble Sort (Iterative) LinkedList

# Given a singly linked list of integers, sort it using 'Bubble Sort.'


from sys import stdin


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def swapAdjacent(head: Node) -> Node:
    temp = head.next
    head.next = temp.next
    temp.next = head
    return temp


def length(head: Node) -> int:
    l = 0
    while head:
        l += 1
        head = head.next

    return l


def bubbleSort(head: Node) -> Node:
    n = length(head)

    if n == 0 or n == 1:
        return head

    newHead = head

    for i in range(n):
        curr = newHead
        prev = None
        swapped = False
        for j in range(0, n - i - 1):
            if curr.data > curr.next.data:
                swapped = True
                if not prev:
                    newHead = swapAdjacent(curr)
                    prev = newHead
                    curr = newHead.next
                else:
                    temp = swapAdjacent(curr)
                    prev.next = temp
                    prev = temp
                    curr = temp.next
            else:
                prev = curr
                curr = curr.next

        if not swapped:
            break
    return newHead


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
head = takeInput()
head = bubbleSort(head)
printLinkedList(head)
