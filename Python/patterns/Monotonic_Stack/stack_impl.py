"""
Implement stack using a list in Python.
"""
class Stack:
    def __init__(self, val = []):
        self.val = val
        
    def push(self,data:int)-> None:
        self.val.append(data)
        
    def isEmpty(self) -> bool:
        return len(self.val) == 0
    
    def top(self) -> int:
        return self.val[len(self.val) - 1]
    
    def pop(self) -> bool:
        if len(self.val) == 0: return False
        self.val.remove(self.val[len(self.val) - 1])
        
    def print_stack(self) -> None:
        for i in self.val:
            print(i)
        
if __name__ == "__main__":
    obj = Stack()
    
    obj.push(1)
    obj.push(2)
    obj.push(3)
    obj.push(4)
    obj.push(5)
    obj.pop()
    obj.print_stack()
    print("Top element is:", obj.top())
    print("Is stack empty?", obj.isEmpty())
    obj.pop()
    obj.print_stack()

    #Time Complexity: O(1) for push, pop, top, isEmpty
    #Space Complexity: O(n) for storing elements in the stack
#     # where n is the number of elements in the stack
#     # Note: The space complexity is O(n) because we are using a list to store the elements of the stack.