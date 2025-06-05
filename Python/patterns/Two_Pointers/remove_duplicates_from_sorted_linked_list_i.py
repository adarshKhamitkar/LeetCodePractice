# Definition for singly-linked list.

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None

        back, front = head, head.next

        while front:
            if back.val != front.val:
                back, front = back.next, front.next
            else:    
                front = front.next
                back.next = front

        return head
    
    # Time Complexity: O(n) - where n is the number of nodes in the linked list
    # Space Complexity: O(1) - in-place modification of the linked list
    # Note: This solution uses O(1) space as it modifies the linked list in-place.