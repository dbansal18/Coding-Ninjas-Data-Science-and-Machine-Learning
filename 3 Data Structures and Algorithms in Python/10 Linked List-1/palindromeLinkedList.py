# https://classroom.codingninjas.com/app/classroom/me/14074/content/257242/offering/3505571/problem/330

# Palindrome LinkedList

# You have been given a head to a singly linked list of integers.
# Write a function check to whether the list given is a 'Palindrome' or not.


from sys import setrecursionlimit, stdin

setrecursionlimit(10 ** 5)

# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def isPalindrome(head: Node) -> bool:
    arr = []

    while head:
        arr.append(head.data)
        head = head.next

    i = 0
    j = len(arr) - 1

    while i < j:
        if arr[i] != arr[j]:
            return False
        i += 1
        j -= 1

    return True


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

    if isPalindrome(head):
        print("true")
    else:
        print("false")

    t -= 1
