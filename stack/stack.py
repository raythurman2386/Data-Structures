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
# from linked_list import LinkedList
from doubly_linked_list import DoublyLinkedList


# Initial stack class, part one of section
class Stack:
    def __init__(self):
        self.storage = DoublyLinkedList()

    def __len__(self):
        return len(self.storage)# Refactor

    def push(self, value):
        self.storage.add_to_head(value)
        return self

    def pop(self):
        if self.storage is None:
            return
        else:
            return self.storage.remove_from_head()
