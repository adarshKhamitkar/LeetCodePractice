#Implement Queue using deque

from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
        
    def isEmpty(self) -> bool:
        return len(self.items) == 0
    
    def size(self) -> int:
        return len(self.items)
    
    def enqueue(self,item):
        self.items.append(item)
        
    def dequeue(self):
        if not self.isEmpty():
            self.items.popleft()
        else:
            raise IndexError("List is Empty!")
            
    def returnQueue(self):
        return self.items
            

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)
    
    print(queue.returnQueue())
    
    queue.dequeue()
    
    print(queue.returnQueue())
  
#time complexity: O(1) for enqueue and dequeue operations
#space complexity: O(n) where n is the number of elements in the queue
#deque is used for efficient appending and popping from both ends