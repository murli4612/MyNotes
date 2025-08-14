Let's start with Question 1: Implement an LRU Cache

Problem Statement
Design a Least Recently Used (LRU) Cache that supports the following operations in O(1) time complexity:

get(key): Returns the value of the key if it exists; otherwise, returns -1.
put(key, value): Inserts or updates the key-value pair. If the cache reaches its capacity, remove the least recently used item before inserting.
Approach
We use:
✅ OrderedDict from collections (preserves order of insertions)
✅ Doubly Linked List + Hash Map (efficient for large-scale use)

Solution Using OrderedDict
Python’s OrderedDict maintains insertion order and allows O(1) pop/move operations.

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()  # Maintains insertion order
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Move accessed item to the end (mark as recently used)
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Move existing key to end
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # Remove LRU (first item)

# Example usage:
lru = LRUCache(2)
lru.put(1, 10)  # Cache: {1:10}
lru.put(2, 20)  # Cache: {1:10, 2:20}
print(lru.get(1))  # Returns 10, moves key 1 to recent {2:20, 1:10}
lru.put(3, 30)  # Removes LRU key 2 -> {1:10, 3:30}
print(lru.get(2))  # Returns -1 (not found)


\
Solution Using Doubly Linked List + HashMap
For large-scale applications, OrderedDict has extra overhead. Instead, we use:
1️⃣ HashMap {key -> Node} for O(1) lookups
2️⃣ Doubly Linked List for O(1) insertions/removals


class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Hashmap: key -> Node
        
        # Dummy head and tail
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """Remove node from the list"""
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def _add_to_end(self, node):
        """Insert node at the end (most recently used)"""
        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._remove(node)
        self._add_to_end(node)  # Move to end as most recently used
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])  # Remove old node
        
        node = Node(key, value)
        self.cache[key] = node
        self._add_to_end(node)

        if len(self.cache) > self.capacity:
            # Remove LRU node
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]

# Example usage:
lru = LRUCache(2)
lru.put(1, 10)
lru.put(2, 20)
print(lru.get(1))  # 10
lru.put(3, 30)  # Removes LRU key 2
print(lru.get(2))  # -1

