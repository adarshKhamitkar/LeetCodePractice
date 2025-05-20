class DLLNode:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None 
        
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = DLLNode(-1,-1)
        self.tail = DLLNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def add(self,node) -> None: # always add the node all the right end, that says most recently used with O(1)
        existing_end = self.tail.prev
        existing_end.next = node 
        node.prev = existing_end
        node.next = self.tail
        self.tail.prev = node
        
    def remove(self,node) -> None: #just remove the node, irrespective of the position 
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def get(self,key) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.add(node)
        return node.val 
        
    def put(self, key, val) -> None:
        if key in self.cache:
            old_node = self.cache[key]
            self.remove(old_node)
        
        new_node = DLLNode(key,val)
        self.cache[key] = new_node
        self.add(new_node)
        
        if len(self.cache) > self.capacity:
            remove_node = self.head.next
            self.remove(remove_node)
            del self.cache[remove_node.key]
            
if __name__ == "__main__":
    
    obj = LRUCache(2)
    result_list = []
    result_list.append(obj.put(1,1))
    result_list.append(obj.put(2,2))
    result_list.append(obj.get(1))
    result_list.append(obj.put(3,3))
    result_list.append(obj.get(2))
    result_list.append(obj.put(4,4))
    result_list.append(obj.get(1))
    result_list.append(obj.get(3))
    result_list.append(obj.get(4))
    
    print(result_list)
    