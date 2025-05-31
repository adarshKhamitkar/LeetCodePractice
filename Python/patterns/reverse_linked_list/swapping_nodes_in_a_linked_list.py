"""
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping 
the values of the kth node from the beginning and the kth node 
from the end (the list is 1-indexed).

Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
"""
# Definition for singly-linked list.
# This code needs to be implemented in Time O(n) and Space O(1).
# As of now it is implemented in Time O(n) and Space O(n).
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        if not head: return False

        input_list = []
        curr = head
        
        while curr:
            input_list.append(curr.val)
            curr=curr.next

        size = len(input_list)

        left = input_list[k-1]
        input_list[k-1] = input_list[size-k]
        input_list[size-k] = left

        head = ListNode(-1)
        curr = head
        for i in input_list:
            new_node = ListNode(i)
            curr.next = new_node
            curr = new_node

        return head.next
        