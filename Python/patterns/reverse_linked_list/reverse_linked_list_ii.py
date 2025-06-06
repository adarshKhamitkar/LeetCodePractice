"""

Given the head of a singly linked list and two integers left and right where left <= right,
reverse the nodes of the list from position left to position right,
and return the reversed list.

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Input: head = [5], left = 1, right = 1
Output: [5]

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head: return None

        prev, curr = None, head

        while left > 1:
            prev, curr = curr, curr.next
            left, right = left-1, right-1

        con, tail = prev, curr

        while right > 0:
            nxt = curr.next
            curr.next = prev
            prev, curr = curr, nxt
            right-=1

        if con:
            con.next = prev
        else:
            head = prev

        tail.next = curr

        return head

