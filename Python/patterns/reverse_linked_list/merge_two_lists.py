"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list.
The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: list1 = [], list2 = []
Output: []

Input: list1 = [], list2 = [0]
Output: [0]

"""
"""
Time Complexity: O(n + m)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        input_list = []
        while list1:
            input_list.append(list1.val)
            list1 = list1.next

        while list2:
            input_list.append(list2.val)
            list2 = list2.next

        head = ListNode(-1)
        curr = head
        for i in sorted(input_list):
            new_node = ListNode(i)
            curr.next = new_node
            curr = new_node

        return head.next

