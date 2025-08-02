"""
Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.

 

Example 1:

Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
Example 2:

Input: nums = [2,3,1,3,2]
Output: [1,3,3,2,2]
Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.
Example 3:

Input: nums = [-1,1,-6,4,5,-6,1,4,1]
Output: [5,-1,4,4,-6,-6,1,1,1]
 

Constraints:

1 <= nums.length <= 100
-100 <= nums[i] <= 100
"""
import heapq

class Solution:
    def sortFrequency(self, nums):
        #get the frequncy of each item
        frequency = {}
        for i in nums:
            frequency[i] = frequency.get(i, 0) + 1

        #create a max heap since members with same frequency should be sorted in descreasing order
        _maxheap = []
        for k,v in frequency.items():
            heapq.heappush(_maxheap,(v, -k))

        #pop and append by negating
        _sorted = []
        while _maxheap:
            val, key = heapq.heappop(_maxheap)
            _sorted.extend([-key] * val)

        return _sorted
    
if __name__ == "__main__":
    nums = [1,1,2,2,2,3]
    print(Solution().sortFrequency(nums))  # Output: [3, 1, 1, 2, 2, 2]
    
    nums = [2,3,1,3,2]
    print(Solution().sortFrequency(nums))  # Output: [1, 3, 3, 2, 2]
    
    nums = [-1,1,-6,4,5,-6,1,4,1]   
    print(Solution().sortFrequency(nums))  # Output: [5, -1, 4, 4, -6, -6, 1, 1, 1]