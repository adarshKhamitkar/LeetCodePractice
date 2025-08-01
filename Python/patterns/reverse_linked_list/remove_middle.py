# Definition for singly-linked list.

from typing import Optional

"""
Given the head of a singly linked list, delete the middle node, and return the head of the modified linked list.

If there are two middle nodes, delete the second middle node.
"""
# Example 1:
# Input: head = [1,3,4,7,1,2,6]
# Output: [1,3,4,1,2,6]
# Explanation: The list is modified to [1,3,4,1,2,6] after deleting the middle node with value 7.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return None

        p1 = p2 = head
        _size = 0

        while p1:
            _size += 1
            p1 = p1.next

        _middle = _size // 2

        for i in range(_middle - 1):
            p2 = p2.next

        p2.next = p2.next.next
        return head
    
#Time Complexity: O(n) where n is the number of nodes in the linked list.
#Space Complexity: O(1) as we are using only constant space.