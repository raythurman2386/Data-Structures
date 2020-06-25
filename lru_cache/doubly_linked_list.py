"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        # Initialize a new node
        new_node = ListNode(value)
        # Check if the list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # Otherwise add the node to the head and change pointers
            current_head = self.head
            self.head = new_node
            new_node.next = current_head
            current_head.prev = new_node
        # Increase the list length and return
        self.length += 1
        return self

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        if self.head is None:
            return

        current_head = self.head.value
        self.delete(self.head)
        return current_head

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return self

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        if self.tail is None:
            return

        current_tail = self.tail.value
        self.delete(self.tail)
        return current_tail

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        if node is self.head:
            return

        old_value = node.value
        self.delete(node)
        self.add_to_head(old_value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        if node is self.tail:
            return

        old_value = node.value
        self.delete(node)
        self.add_to_tail(old_value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        # Check if the list is empty
        if self.length is 0:
            return self

        # Decrement the length
        self.length -= 1

        # Checks for only one node
        if self.head == self.tail and node == self.head:
            self.head = None
            self.tail = None

        # Checks if the node is the current head
        elif self.head == node:
            self.head = node.next
            node.delete()

        # Checks if the node is the current tail
        elif self.tail == node:
            self.tail = node.prev
            node.delete()

        # find the node and delete it in the list
        else:
            node.delete()

    """Returns the highest value currently in the list"""

    def get_max(self):
        if not self.head:
            return None

        max_val = self.head.value
        current_node = self.head

        while current_node:
            if current_node.value > max_val:
                max_val = current_node.value
            current_node = current_node.next

        return max_val
