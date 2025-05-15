def recursive_reverse_string(s):
    if len(s) == 0: return s
    else: return s[-1] + recursive_reverse_string(s[:-1])

def is_palindrome(s) -> bool:
    if s == recursive_reverse_string(s): return True
    return False

def word_count(statement: str) -> dict:
    word_counter = dict()
    for word in statement.split():
        word_counter[word] = word_counter.get(word, 0) + 1 
    return word_counter

class Node:
    def __init__(self, data):
        self.val = data
        self.next = None
        
class Singly_Linked_List:
    def __init__(self):
        self.size = 0
        self.head = Node(0) #sentinal node; beginning holder for a LL. 
        
    def add_at_index(self, index:int, x:int) -> None:
        if index < 0 or index > self.size: return #return if the index is invalid
    
        new_node = Node(x)
        
        self.size+=1 
        curr = self.head
        
        for i in range(index):
            curr = curr.next
            
        new_node.next = curr.next 
        curr.next = new_node
        
    def del_at_index(self, index:int) -> None:
        if index < 0 or index >= self.size: return #return if the index is invalid
        
        self.size-=1 
        
        curr = self.head
        
        for i in range(index):
            curr = curr.next
            
        curr.next = curr.next.next
        
    def add_at_head(self, data:int) -> None:
        self.add_at_index(0,data)
        
    def add_at_tail(self, data:int) -> None:
        self.add_at_index(self.size,data)
       
    def print_list(self) -> None:
        curr = self.head.next
        for i in range(self.size):
            print(curr.val)
            curr = curr.next
    
    
def main():
    # statement = "sampagappa na maga mari sampagappa"
    # print(word_count(statement))

    list_obj = Singly_Linked_List()
    list_obj.add_at_head(5)
    list_obj.add_at_index(1,10)
    list_obj.add_at_index(2,15)
    list_obj.add_at_index(3,20)
    list_obj.add_at_tail(25)
    
    list_obj.print_list()
    
if __name__ == "__main__":
    main()
    