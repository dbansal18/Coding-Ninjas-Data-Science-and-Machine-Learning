# https://classroom.codingninjas.com/app/classroom/me/14074/content/257243/offering/3505591/problem/326

# Swap two Nodes of LL

# You have been given a singly linked list of integers along with two integers, 'i,' and 'j.'
# Swap the nodes that are present at the 'i-th' and 'j-th' positions.


from sys import stdin


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def swapNodes(head: Node, i: int, j: int) -> Node:
    if not head:
        return head

    if i == j:
        return head

    if i > j:
        i, j = j, i

    n1 = head
    k = 1
    while k < i:
        n1 = n1.next
        k += 1

    n2 = head
    k = 1
    while k < j:
        n2 = n2.next
        k += 1

    if i == 0 and i + 1 == j:
        n2 = n1.next
        n1.next = n2.next
        n2.next = n1
        return n2
    elif i + 1 == j:
        n3 = n2.next
        n1.next = n3
        n2.next = n3.next
        n3.next = n2
        return head
    elif i == 0:
        temp = n1.next
        head = n2.next
        n1.next = n2.next.next
        n2.next.next = temp
        n2.next = n1
    else:
        temp1 = n1.next
        temp2 = n2.next
        temp3 = temp1.next
        temp1.next = temp2.next
        temp2.next = temp3
        n1.next = temp2
        n2.next = temp1

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
    i_j = stdin.readline().strip().split(" ")

    i = int(i_j[0])
    j = int(i_j[1])

    newHead = swapNodes(head, i, j)
    printLinkedList(newHead)

    t -= 1
