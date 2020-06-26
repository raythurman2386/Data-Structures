from doubly_linked_list import DoublyLinkedList

"""
WHAT IS AN LRU CACHE???
"""
"""
LRU(Least Recently Used) Cache discards the least recently used items first. 
This algorithm requires keeping track of what was used when, which is 
expensive if one wants to make sure the algorithm always discards the least recently used item.

General implementations of this technique require keeping "age bits" for cache lines and 
track the LRU cache line based on age bits

LRU Should support the following operations
> get - get the value, will always be positive, of the key if the key exists
> put - set or insert the value if the key is not present.
    When the cache reaches capacity, it should remove the last item before
    inserting a new item
""" 

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.storage = {}
        self.list = DoublyLinkedList()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # Check for the key in storage
        if key not in self.storage:
            # return none if no key
            return None
        else:
            # if it's in storage, set to a variable
            item = self.storage[key]
            # move the key to the end of the queue
            self.list.move_to_end(item)
            # return the value associated with key
            # the item should be a tuple
            # the actual value needed should be in position [1]
            # of the tuple
            return item.value[1]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # Check for the item in storage
        if key in self.storage:
            item = self.storage[key]
            # update the items values
            item.value = (key, value)
            # add the item to the end of the list
            self.list.move_to_end(item)
            return
        # if the length of the list is at the limit
        if len(self.list) >= self.limit:
            # remove the oldest item
            # the oldest item should be the head of the list/queue
            del self.storage[self.list.head.value[0]]
            self.list.remove_from_head()

        # otherwise add the item to the list and
        self.list.add_to_tail((key, value))
        # Add the item to the LRU storage
        self.storage[key] = self.list.tail
