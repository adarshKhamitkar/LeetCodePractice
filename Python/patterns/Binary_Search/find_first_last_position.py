"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
"""
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #Find the first arriving of index of target
        #Then find the last arriving index of target

        def find_first(nums,target):
            n = len(nums)
            left, right = 0, (n-1)
            first = -1
            while left <= right:
                mid  = left + (right - left) // 2
                if nums[mid] >= target: right = mid - 1
                else: left = mid + 1
                if nums[mid] == target: first = mid
            return first
        
        def find_last(nums,target):
            n = len(nums)
            l, r  = 0, (n-1)
            last = -1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] <= target: l = mid + 1
                else: r = mid - 1
                if nums[mid] == target: last = mid
            return last
        
        return [find_first(nums, target), find_last(nums, target)]
# Time Complexity: O(log n) for both find_first and find_last
# Space Complexity: O(1) as we are not using any extra space that grows with input size
# Example usage:

if __name__ == "__main__":
    solution = Solution()
    print(solution.searchRange([5,7,7,8,8,10], 8))  # Output: [3, 4]
    print(solution.searchRange([5,7,7,8,8,10], 6))  # Output: [-1, -1]
    print(solution.searchRange([], 0))               # Output: [-1, -1]
    print(solution.searchRange([1,2,3,4,5], 3))      # Output: [2, 2]