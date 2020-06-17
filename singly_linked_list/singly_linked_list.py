
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next  # Single next denotes singly linked list


# Linked list implementation
# TODO: Refactor and handle the length from this class
# TODO: Refactor LinkedList to pass tests
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
