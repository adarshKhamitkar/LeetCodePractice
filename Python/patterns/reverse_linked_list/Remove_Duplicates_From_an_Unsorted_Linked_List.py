"""
Given the head of a linked list,
find all the values that appear more than once in the list and delete the nodes that have any of those values.

Return the linked list after the deletions.

Input: head = [1,2,3,2]
Output: [1,3]
Explanation: 2 appears twice in the linked list, so all 2's should be deleted.
             After deleting all 2's, we are left with [1,3].

Input: head = [2,1,1,2]
Output: []
Explanation: 2 and 1 both appear twice. All the elements should be deleted.

Input: head = [3,2,2,1,3,2,4]
Output: [1,4]
Explanation: 3 appears twice and 2 appears three times.
             After deleting all 3's and 2's, we are left with [1,4].
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        if not head: return None
        seen = dict()
        res = []

        curr = head
        while curr:
            seen[curr.val] = seen.get(curr.val, 0) + 1
            curr = curr.next
        for i in seen.keys():
            if seen[i] == 1: res.append(i)

        res_list = ListNode(0)
        curr = res_list
        for i in (res):
            new_node = ListNode(i)
            curr.next = new_node
            curr = new_node
        return res_list.next
