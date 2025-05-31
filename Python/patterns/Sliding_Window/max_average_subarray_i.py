"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value 
and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
 

Constraints:

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104
"""

from typing import List

class Solution:
    def findMaxAverage(self, nums:List[int], k) -> float:
        n = len(nums)
        if n < k : return 0.0
        
        sum_window = 0
        for i in range(k):
            sum_window += nums[i]

        final_res = sum_window # Calculate the sum of first k elemnts of the array.

        for i in range(k, n):
            sum_window += nums[i] - nums[i-k] #Slide the window by adding next elemnt of the window and removing the first element of the window.
            final_res = max(final_res, sum_window) #Compare the existing max sum of elements with size K and sum of elements of current window of size K.

        return final_res / k #Return the average of the max sum of elements of size K.
    
if __name__ == '__main__':
    sol = Solution()

    # Test case 1
    nums1 = [1, 12, -5, -6, 50, 3]
    k1 = 4
    print(f"Input: nums = {nums1}, k = {k1}")
    print(f"Output: {sol.findMaxAverage(nums1, k1)}")  # Expected Output: 12.75

    # Test case 2
    nums2 = [5]
    k2 = 1
    print(f"Input: nums = {nums2}, k = {k2}")
    print(f"Output: {sol.findMaxAverage(nums2, k2)}")  # Expected Output: 5.0

    # Test case 3
    nums3 = [0,4,0,3,2]
    k3 = 1
    print(f"Input: nums = {nums3}, k = {k3}")
    print(f"Output: {sol.findMaxAverage(nums3, k3)}")  # Expected Output: 4.0

    # Test case 4
    nums4 = [4,2,1,3,3]
    k4 = 2
    print(f"Input: nums = {nums4}, k = {k4}")
    print(f"Output: {sol.findMaxAverage(nums4, k4)}")  # Expected Output: 3.0

# Time Complexity: O(n), where n is the length of the input array nums.
# The code iterates through the array once to calculate the sum of each window.
# Space Complexity: O(1), The code uses a constant amount of extra space, regardless of the input size.

