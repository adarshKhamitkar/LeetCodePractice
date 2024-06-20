class Queue:
    
    def __init__(self,queue_list,start_index):
        self.queue_list = list()
        self.start_index = 0
        
    def enqueue(self,val):
        self.queue_list.append(val)
        return True
    
    def dequeue(self):
        if(self.start_index >= len(self.queue_list)): return False
        self.start_index+=1
        return True
        
    def returnQueue(self):
        return self.queue_list
    
    def getFront(self):
        return self.queue_list[self.start_index]
    
class CircularQueue:
    
    def __init__(self,k):
        self.capacity = k
        self.headIndex = 0
        self.count = 0
        self.arrayList = [0] * k
        
    def enqueue(self,val):
        if self.count == self.capacity: return False
        self.arrayList[(self.headIndex+self.count)%self.capacity]=val
        self.count+=1
        return True
    
    def dequeue(self):
        if self.count == 0: return False
        self.headIndex = (self.headIndex + 1) % self.capacity
        self.count-=1
        return True
        
    def getFront(self):
        if self.count == 0: return False
        return self.arrayList[self.headIndex]
    
    def getRear(self):
        if self.count == 0: return False
        return self.arrayList[(self.headIndex+self.count-1)%self.capacity]
    
class Stack:
    def __init__(self):
        self.stack_list = list()
    
    def push(self,val):
        self.stack_list.append(val)
        return True
    
    def pop(self):
        if (len(self.stack_list) == 0): return False
        self.stack_list.remove(self.stack_list[len(self.stack_list)-1])
        return True
    
    def returnTop(self):
        return self.stack_list[len(self.stack_list)-1]
        
    def returnStack(self):
        return self.stack_list
    
if __name__ == "__main__":
    q_list=list()
    i = 0
    q = Queue(q_list,i)
    
    q.enqueue(5)
    q.enqueue(15)
    q.enqueue(25)
    q.enqueue(35)
    q.enqueue(45)
    
    print(q.returnQueue())
    
    q.dequeue()
    print(q.getFront())
    print(q.returnQueue())
    
    s = Stack()
    s.push(25)
    s.push(50)
    s.push(75)
    s.push(100)
    s.push(125)
    
    print(s.returnStack())
    s.pop()
    print(s.returnStack())
        
