"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
"""

from typing import List

class Solution:
    def trapRainWater(self,height:List[int]) -> int:
        n = len(height)
        
        #Scan heights array from both left and right to get max from both the directions
        max_left = [0] * n
        max_right = [0] * n
        
        #get the variable to return max height at every iteration
        l_wall, r_wall = 0, 0
        
        #initialize the max_left and max_right arrays from both the directions
        for i in range(n):
            j = -i -1
            max_left[i] = l_wall
            max_right[j] = r_wall
            
            l_wall = max(l_wall, height[i])
            r_wall = max(r_wall, height[j])
            
        print(max_left)
        print(max_right)
        summ = 0 #to store the total amount of water trapped
        #Calculate the potential height at every iteration and trap the water
        for i in range(n):
            potential_height = min(max_left[i],max_right[i])
            summ+= max(0, potential_height - height[i])
        return summ
    
if __name__ == "__main__":
    obj = Solution()
    
    result = obj.trapRainWater([0,1,0,2,1,0,1,3,2,1,2,1])
    
    print(result)

    #Time Complexity: O(n) where n is the length of the height array.
    #Space Complexity: O(n) for the max_left and max_right arrays.
    result = obj.trapRainWater([4,2,0,3,2,5])
    print(result)  # Output: 9
    #Time Complexity: O(n) where n is the length of the height array.
    #Space Complexity: O(n) for the max_left and max_right arrays.
    result = obj.trapRainWater([1,0,2,1,0,1,3,2,1,2,1])
    print(result)  # Output: 6
    #Time Complexity: O(n) where n is the length of the height array.
    #Space Complexity: O(n) for the max_left and max_right arrays.
    result = obj.trapRainWater([1,2,3,4,5])
    print(result)  # Output: 0
    #Time Complexity: O(n) where n is the length of the height array.
    #Space Complexity: O(n) for the max_left and max_right arrays.