"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]

Input: head = []
Output: []

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None: return None
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev #Broke the nxt pointer and initialized to previous
            prev = curr
            curr = nxt #shift both the pointers
        return prev
    # Time Complexity = O(N)
    # Space Complexity = O(1) -> achieved by using of pointers only