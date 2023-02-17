class ListNode():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):  
        self.capacity = capacity
        self.cache = {}
        # dummy nodes to point to the lru and mru
        self.left, self.right = ListNode(0,0), ListNode(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    # remove from the linked list
    def remove(self, node):
        prev, _next = node.prev, node.next
        prev.next = _next
        _next.prev = prev
    
    # insert to the right since right side is the most recently used 
    def insert(self, node):
        prev, _right = self.right.prev, self.right
        prev.next = _right.prev = node
        node.next, node.prev = _right, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # we want to remove it from the current position and move it to the right side of 
            # the linked list (most recently used side)
            self.remove(self.cache[key]) #remove it from curr pos
            self.insert(self.cache[key]) #insert it to the most recetly used side (right)
            return self.cache[key].value
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        # if key already exists in cache remove it to update its value
        if key in self.cache:
            self.remove(self.cache[key])
        # construct the new node from the key and value
        # insert it at the right side
        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])
        # evict lru => left.next is the lru
        # remove the lru node from the list and then delete it from the cache
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        

    

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)