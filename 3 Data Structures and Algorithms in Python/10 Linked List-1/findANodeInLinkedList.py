# https://classroom.codingninjas.com/app/classroom/me/14074/content/257242/offering/3505571/problem/1146

# Find a Node in Linked List

# You have been given a singly linked list of integers.
# Write a function that returns the index/position of integer data denoted by 'N' (if it exists). Return -1 otherwise.

# Note :
# Assume that the Indexing for the singly linked list always starts from 0.


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def findNode(head: Node, n: int) -> int:
    i = 0
    curr = head

    while curr:
        if curr.data == n:
            return i
        i += 1
        curr = curr.next

    return -1
