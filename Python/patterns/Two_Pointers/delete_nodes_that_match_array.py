"""
You are given an array of integers nums and the head of a linked list. 
Return the head of the modified linked list after removing all nodes from 
the linked list that have a value that exists in nums.

Example 1:

Input: nums = [1,2,3], head = [1,2,3,4,5]

Output: [4,5]

Example 2:

Input: nums = [1], head = [1,2,1,2,1,2]

Output: [2,2,2]
"""

# Definition for singly-linked list.
from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or len(nums) == 0: return None

        remove_nodes = set(nums)

        sentinal_node = ListNode(-1,head)

        curr = sentinal_node

        while curr.next:
            if curr.next.val in remove_nodes:
                curr.next = curr.next.next #Start with sentinal node and the next will point to head.
            else:
                curr = curr.next #Just move the pointer forward.

        return sentinal_node.next # Return the next of sentinal node which is the head of the modified linked list.
    
    #Time Complexity: O(n) where n is the number of nodes in the linked list.
    #Space Complexity: O(m) where m is the number of elements in nums, since we are using a set to store the elements to be removed.