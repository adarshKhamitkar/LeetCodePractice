"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        item_to_index = {}

        for i in range(n):
            complement = target - nums[i]
            if complement in item_to_index:
                return [i, item_to_index[complement]]
            item_to_index[nums[i]] = i #store the index as value for number as the key
        return [-1,-1]
    
    #Time Complexity: O(n)
    #Space Complexity: O(n)