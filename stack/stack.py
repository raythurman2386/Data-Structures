"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next # Single next denotes singly linked list


# Linked list implementation
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Insert a new Node into the front list
    def add_to_head(self, data):
        new_node = Node(data)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        return self

    # delete an item from the end
    def remove_head(self):
        if not self.head:
            return None

        if self.head.next is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value

        head_value = self.head.value
        self.head = self.head.next
        return head_value


# Initial stack class, part one of section
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1
        return self

    def pop(self):
        if self.size == 0:
            return
        else:
            removed_value = self.storage.head.value
            self.storage.remove_head()
            self.size -= 1
            return removed_value
