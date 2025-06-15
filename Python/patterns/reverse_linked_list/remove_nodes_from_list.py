"""
You are given the head of a linked list.

Remove every node which has a node with a greater value anywhere to the right side of it.

Return the head of the modified linked list.

 

Example 1:


Input: head = [5,2,13,3,8]
Output: [13,8]
Explanation: The nodes that should be removed are 5, 2 and 3.
- Node 13 is to the right of node 5.
- Node 13 is to the right of node 2.
- Node 8 is to the right of node 3.
Example 2:

Input: head = [1,1,1,1]
Output: [1,1,1,1]
Explanation: Every node has value 1, so no nodes are removed.
"""

from typing import Optional
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None

        curr = head
        stack = []
        res_list = []

        while curr:
            stack.append(curr.val)
            curr = curr.next

        maximum = -1
        while stack:
            next_val = stack.pop()
            if next_val >= maximum:
                res_list.append(next_val)
            maximum = res_list[-1]

        res_list = res_list[::-1]

        sentinal_node = ListNode(-100)
        curr = sentinal_node

        for i in res_list:
            new_node = ListNode(i)
            curr.next = new_node
            curr = new_node

        return sentinal_node.next
    
if __name__ == "__main__":
    # Example usage:
    head = ListNode(5, ListNode(2, ListNode(13, ListNode(3, ListNode(8)))))
    solution = Solution()
    new_head = solution.removeNodes(head)

    # Print the modified linked list
    curr = new_head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    # Output: 13 8

    #Time Complexity: O(n) where n is the number of nodes in the linked list
    #Space Complexity: O(n) for storing the values in the stack and result list