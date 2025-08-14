# Implement a Least Recently Used (LRU) cache with a specified capacity. It should support the following operations:
# get(key): Get the value of the key if it exists in the cache, otherwise return -1.
# put(key, value): Set or insert the value. When the cache reaches its capacity, it should invalidate the least recently used item before inserting a new item.

from collections import OrderedDict
class LRU:
    def __init__(self,capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
    
    def get(self,key):
        if key not in self.cache:
            return -1
        
        self.cache.move_to_end(key)
        return self.cache[key]
    def put(self,key,value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
    
    def print_cache(self):
        print("Current Cache State: ", list(self.cache.items()))

            
Lru = LRU(3)
Lru.put(1,1)
Lru.put(2,2)
Lru.put(3,3)
Lru.print_cache()
print(Lru.get(1))
Lru.print_cache()
Lru.put(4,4)
Lru.print_cache()
print(Lru.get(4))
Lru.print_cache()
print(Lru.get(1))
Lru.print_cache()
