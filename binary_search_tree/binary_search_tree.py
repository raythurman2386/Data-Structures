"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Take the value of the current node (self.value)
        # COmpare to the value that we are inserting

        # if new_value < self.value
        if value < self.value:
            # if self.left is taken by a node,
            if self.left is not None:
                # make that node, call insert
                self.left.insert(value)
            else:
                # Set the left to the new node
                self.left = BSTNode(value)
        # if new_value > self.value
        if value >= self.value:
            # if self.right is taken,
            if self.right is not None:
                # make self.right call insert
                self.right.insert(value)
            else:
                # set the right value to the new node
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True

        # Compare the target to the current value
        # if current value < target
        if self.value > target:
            # check the left subtree
            if self.left is None:
                return False
            found = self.left.contains(target)
        else:
            if self.right is None:
                return False

            found = self.right.contains(target)

        return found

    # Return the maximum value found in the tree
    def get_max(self):
        # if the root is empty return
        if self.value is None:
            return self

        # Set max value to initial node if there is one
        max_value = self.value
        # check if the right node is none
        if self.right is None:
            # if it is return max value
            return max_value

        # if self.right > max_value
        if self.right.value > max_value:
            # recursively run get max on self.right
            max_value = self.right.get_max()

        return max_value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # if self is none
        if self.value is None:
            return

        # run function on current value
        fn(self.value)

        # check make sure left is not none
        if self.left is not None:
            # run foreach on the existing left node
            self.left.for_each(fn)

        # check make sure right is not none
        if self.right is not None:
            # run for_each on existing right node
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # as long as there is a node
        if node:
            # recursively call the function passing in left node
            self.in_order_print(node.left)
        # print the current node value
            print(node.value)
        # recursively call the function passing in the right node
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


my_tree = BSTNode(1)
my_tree.insert(6)
my_tree.insert(3)
my_tree.insert(9)
my_tree.insert(5)
my_tree.insert(4)
my_tree.insert(6)
my_tree.insert(10)
my_tree.insert(12)
my_tree.insert(7)

# Testing in_order_print
my_tree.in_order_print(my_tree)
