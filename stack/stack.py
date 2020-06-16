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

'''
 Node implementation from what I have done previously with college

 TODO: Once lecture and guided project is over, revisit and refactor
 as needed. All current tests for this file pass with both
 implementations
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None # Single next denotes singly linked list

    # Return the value of current Node
    def get_data(self):
        return self.value

    # Set the Current Nodes value
    def set_data(self, value):
        self.value = value

    # Get the next node in the List
    def get_next(self):
        return self.next

    # Set the next node in the list
    def set_next(self, next):
        self.next = next


'''
 Linked list implementation
 TODO: Refactor after lecture and guided project
 Initial Implementation passes tests but I want
 To see what we come up with tonight.
 This is slightly different than the linked lists
 I've done before so I could get the tests passing
'''

class Stack:
    def __init__(self, head=None):
        self.head = head
        self.count = 0
        self.storage = []

    # Ability to return the length of the list
    def __len__(self):
        return self.count

    # Insert a new Node into the list
    def push(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.storage.append(new_node)
        self.count += 1
        return self

    # delete an item at a given index
    def pop(self):
        if self.count == 0:
            return
        else:
            self.count -= 1
            return self.storage.pop().value


#  Array Implementation

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.storage.append(value)
#         self.size += 1
#         return self

#     def pop(self):
#         if self.size == 0:
#             return
#         else:
#             self.size -= 1
#             return self.storage.pop()
