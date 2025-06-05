"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list. Return the linked list sorted as well.
Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]
"""

# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        input_map = dict()
        res = []
        while head:
            input_map[head.val] = input_map.get(head.val,0) + 1
            head = head.next

        for i in input_map.keys():
            if input_map.get(i) == 1:
                res.append(i)

        head = ListNode(0)
        curr = head

        for i in res:
            new_node = ListNode(i)
            curr.next = new_node
            curr = new_node
        
        return head.next

    # Time Complexity: O(n) - where n is the number of nodes in the linked list
    # Space Complexity: O(n) - for storing the values in a dictionary
    # Note: This solution uses O(n) space due to the dictionary, which is not in-place.