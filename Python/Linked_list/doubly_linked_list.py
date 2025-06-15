# https://leetcode.com/problems/design-linked-list/editorial/
class DLLNode:
    def __init__(self, data: int):
        self.val = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.size = 0
        self.head, self.tail = DLLNode(0), DLLNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size: return -1

        if index + 1 < self.size - index:
            curr = self.head
            for i in range(index + 1):
                curr = curr.next

        else:
            curr = self.tail
            for i in range(self.size - index):
                curr = curr.prev

        return curr.val

    def addAtIndex(self, index: int, data: int) -> None:
        if index > self.size: return

        if index < 0:
            index = 0

        if index < self.size - index:
            pred = self.head
            for i in range(index):
                pred = pred.next
            succ = pred.next
        else:
            succ = self.tail
            for i in range(self.size - index):
                succ = succ.prev
            pred = succ.prev

        new_node = DLLNode(data)
        self.size += 1

        new_node.next = succ
        new_node.prev = pred
        pred.next = new_node
        succ.prev = new_node

    def addAtHead(self, data: int) -> None:
        pred, succ = self.head, self.head.next

        new_node = DLLNode(data)
        self.size += 1

        new_node.next = succ
        new_node.prev = pred
        pred.next = new_node
        succ.prev = new_node

    def addAtTail(self, data: int) -> None:
        succ, pred = self.tail, self.tail.prev

        new_node = DLLNode(data)
        self.size += 1

        new_node.next = succ
        new_node.prev = pred
        pred.next = new_node
        succ.prev = new_node

    def delAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size: return

        if index < self.size - index:
            pred = self.head
            for i in range(index):
                pred = pred.next
            succ = pred.next.next  # initialize the successor as next of current next of existing predecessor

        else:
            succ = self.tail
            for i in range(
                    self.size - index - 1):  # making sure that the index to be deleted is not included in the range
                succ = succ.prev
            pred = succ.prev.prev  # initialize the predecessor as previous of current previous of existing successor

        self.size -= 1

        # since we have already initialized in the above stud, now assigning will do the work
        pred.next = succ
        succ.prev = pred

if __name__ == "__main__":
    obj2 = DoublyLinkedList()
    print(obj2.addAtHead(1))
    print(obj2.addAtTail(3))
    print(obj2.addAtIndex(1, 2))
    print(obj2.get(1))
    print(obj2.delAtIndex(1))
    print(obj2.get(1))
