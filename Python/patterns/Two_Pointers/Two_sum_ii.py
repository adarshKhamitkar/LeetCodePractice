"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 

Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
"""

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        if n == 0: return [-1]
        left, right = 0, n-1

        while(left < right):
            sum_num = numbers[left] + numbers[right]
            if target == sum_num: return [(left+1), (right+1)]
            elif target < sum_num: right-=1
            else: left+=1

        return [-1,-1]

# Time Complexity: O(n), where n is the length of the input array numbers.
# Space Complexity: O(1), as we are using only a constant amount of extra space for the left and right pointers.
if __name__ == '__main__':
    sol = Solution()

    # Test case 1
    numbers1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Input: numbers = {numbers1}, target = {target1}")
    print(f"Output: {sol.twoSum(numbers1, target1)}")  # Expected Output: [1, 2]

    # Test case 2
    numbers2 = [2, 3, 4]
    target2 = 6
    print(f"Input: numbers = {numbers2}, target = {target2}")
    print(f"Output: {sol.twoSum(numbers2, target2)}")  # Expected Output: [1, 3]

    # Test case 3
    numbers3 = [-1, 0]
    target3 = -1
    print(f"Input: numbers = {numbers3}, target = {target3}")
    print(f"Output: {sol.twoSum(numbers3, target3)}")  # Expected Output: [1, 2]