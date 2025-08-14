class Node:
    def __init__(self,key=None,value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        
class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache ={}
        
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def remove(self,node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        
    def addToFront(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        
    def getValue(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.addToFront(node)
            return node.value
        return -1
    
    def putValue(self,key,value):
        
        if key in self.cache:
            self.remove(self.cache[key])
        elif len(self.cache) >= self.capacity:
            leastRecentlyUsed = self.tail.prev
            self.remove(leastRecentlyUsed)
            del self.cache[leastRecentlyUsed.key]
        
        new_node = Node(key,value)
        self.cache[key] = new_node
        self.addToFront(new_node)
        return list(self.cache.items())


Lru = LRU(3)
Lru.putValue(1,1)
Lru.putValue(2,2)
Lru.putValue(3,3)
# Lru.putValue(4,4)
print(Lru.putValue(4,4))
# print(Lru.getValue(2))