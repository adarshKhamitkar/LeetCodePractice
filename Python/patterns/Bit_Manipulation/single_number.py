"""
Given
a
non - empty
array
of
integers
nums, every
element
appears
twice except for one.Find that single one.

You
must
implement
a
solution
with a linear runtime complexity and use only constant extra space.

Example
1:

Input: nums = [2, 2, 1]

Output: 1

Example
2:

Input: nums = [4, 1, 2, 1, 2]

Output: 4

Example
3:

Input: nums = [1]

Output: 1

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
"""
class Solution:
    def singleNumber(self, nums: list) -> int:
        counter = dict()
        for i in nums:
            counter[i] = counter.get(i,0) + 1

        for key in counter:
            if counter.get(key) == 1: return key
        return -1
