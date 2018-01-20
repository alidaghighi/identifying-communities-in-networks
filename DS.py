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
        self.child = None


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

    def __add__(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            node.next.prev = node
            self.head = node

    def add__child(self, child):
        p = self.head
        if p is not None:
            p.child = child

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

    def pop(self):
        p = self.head
        tmp = p.prev
        self.head = tmp

    def clear(self):
        p = self.head
        p.next = None
        p.data = None
        p.prev = None
        p.child = None

    def __str__(self):
        s = ""
        p = self.head
        if p is not None:
            while p.next is not None:
                s += str(p.data) + '\t'
                p = p.next
            s += str(p.data)
        return s
