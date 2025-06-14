"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def binarySearch(left_boundary, right_boundary, target):
            left, right = left_boundary, right_boundary
            while (left <= right):
                mid = left + (right - left) //2
                if nums[mid] == target: return mid
                elif nums[mid] > target: right = mid - 1
                else: left = mid + 1
            return -1
        
        left, right = 0, (n-1)

        while (left <= right):
            mid = left + (right - left) // 2
            if nums[mid] > nums[-1]:
                right = mid - 1
            else: left = mid + 1

        result = binarySearch(0, left - 1, target)
        if result != -1: return result
        return binarySearch(left, n - 1, target)
          
    #  #Time Complexity: O(log n)
    #  #Space Complexity: O(1)
    #       #Brute Force
    #       for i in range(len(nums)):
    #            if nums[i] == target:
    #                 return i
    #       return -1
    #  #Time Complexity: O(N)
    #  #Space Complexity: O(1)
