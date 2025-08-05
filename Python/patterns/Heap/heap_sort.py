"""
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) 
time complexity and with the smallest space complexity possible.

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessarily unique.
 

Constraints:

1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104
"""

import heapq

class Solution:
    def sortArray(self,nums):
        _n = len(nums)

        if _n <= 1: return nums

        #create a min_heap from the array
        heapq.heapify(nums)

        #pop the elements from heapified array and store them in separate array with insertion order
        _sorted = []
        for i in range(_n):
            _sorted.append(heapq.heappop(nums))

        return _sorted
    
#Time complexity: O(nlog(n)) for heapify and O(nlog(n)) for popping elements from the heap
#Space complexity: O(1) because we are emptying nums by popping elements
#Using heapq to implement the heap operations efficiently