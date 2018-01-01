import numpy as np
"""
We have Node class:
    Data
    next node
    previous node
"""


class Node:
    def __init__(self, data):
        self.next = None
        self.data = data
        self.prev = None

"""
Linked List:
    add
    remove
    search
    show:printing the LinkedList
"""


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            node.next.prev = node
            self.head = node

    def search(self, k):
        p = self.head
        if p is not None:
            while p.next is not None:
                if p.data is k:
                    return p
                p = p.next
            if p.data is k:
                return p
        return None

    def remove(self, p):
        tmp = p.prev
        p.prev.next = p.next
        p.prev = tmp

"""
Adjacency Matrix:

"""


class Matrix:
    def __init__(self, number):
        self.matrix = [[0 for i in range(number)] for i in range(number)]

