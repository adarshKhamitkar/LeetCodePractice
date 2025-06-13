class Node:
    def __init__(self,x):
        self.val = x
        self.next = None 

class SinglyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = Node(0)
        
    def add_at_index(self, index:int, val:int):
        if index < 0 or index > self.size:
            print("Invalid Index!")
            return
        
        new_node = Node(val)
        self.size+=1 
        
        pred = self.head
        
        for i in range(index):
            pred = pred.next
            
        new_node.next = pred.next
        pred.next = new_node
        
    def del_at_index(self, index:int):
        if index < 0 or index >= self.size:
            print("Invalid Index!")
            return -1
            
        self.size-=1 
        
        pred = self.head
        for i in range(index):
            pred = pred.next
            
        pred.next = pred.next.next
        
    def add_at_beginning(self, val:int):
        
        self.add_at_index(0,val)
        
    def add_at_end(self, val:int):
        
        self.add_at_index(self.size,val)
        
    def get(self, index:int) -> int:
        
        if index < 0 or index >= self.size:
            print("invalid index")
            return -1
        
        curr = self.head
        
        for i in range(index+1):
            curr = curr.next
            
        return curr.val
    
    def print_linked_list(self):
        curr = self.head.next

        for i in range(self.size):
            print(curr.val)
            curr = curr.next

if __name__ == "__main__":
    
    obj = SinglyLinkedList()
    output_list = []
    output_list.append(obj.add_at_beginning(1))
    output_list.append(obj.add_at_end(3))
    output_list.append(obj.add_at_index(1,2))
    output_list.append(obj.get(1))
    output_list.append(obj.del_at_index(1))
    output_list.append(obj.get(1))
    
   # print(output_list)    [None, None, None, 2, None, 3]
    obj.print_linked_list()