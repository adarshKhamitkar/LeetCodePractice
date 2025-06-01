"""
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, 
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, (n-1)
        max_area = 0
        while left < right:
            width = right - left
            max_area = max(max_area, (min(height[left], height[right]) * width))
            if height[left] > height[right]: right-=1
            else: left+=1
        return max_area
    
if __name__ == '__main__':
    sol = Solution()
    
    # Test case 1
    height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(f"Input: height = {height1}")
    print(f"Output: {sol.maxArea(height1)}")  # Expected Output: 49
    
    # Test case 2
    height2 = [1, 1]
    print(f"Input: height = {height2}")
    print(f"Output: {sol.maxArea(height2)}")  # Expected Output: 1
    # Test case 3
    height3 = [4, 3, 2, 1, 4]
    print(f"Input: height = {height3}")
    print(f"Output: {sol.maxArea(height3)}")  # Expected Output: 16

    # Time Complexity: O(n), where n is the length of the input array height.
    # Space Complexity: O(1), as we are using only a constant amount of extra space for the left and right pointers.
    # Note: The solution uses a two-pointer approach to find the maximum area efficiently. 