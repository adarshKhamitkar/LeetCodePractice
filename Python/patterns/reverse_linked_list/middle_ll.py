"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

"""

# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head

        p1 = p2 = head
        _len = 0

        while p1:
            _len += 1
            p1 = p1.next

        _middle = _len // 2

        for i in range(_middle):
            p2 = p2.next

        return p2

#Time Complexity: O(n) where n is the number of nodes in the linked list.
#Space Complexity: O(1) as we are using only constant space.