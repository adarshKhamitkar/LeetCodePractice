"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
"""

from typing import List

class Solution:
    def searchMatrix(self,matrix:List[List[int]], target: int) -> bool:
        def binarySearch(arr, target) -> bool:
            n = len(arr)
            l, r = 0, (n-1)
            while l<=r:
                m = l + (r - l) // 2
                if target == arr[m]: return True
                elif target > arr[m]: l = m + 1
                else: r = m - 1
            return False
        
        n = len(matrix)
        l, r = 0, (n-1)
        while l<=r:
            m = l + (r - l) // 2
            if target > matrix[m][0] and target < matrix[m][(len(matrix[m]) - 1)]:
                return binarySearch(matrix[m], target)
            elif target < matrix[m][0]:
                r = m - 1
            else:
                l = m + 1
        return False
    
if __name__ == "__main__":
    soln = Solution()
    matrix, target = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13
    print(soln.searchMatrix(matrix,target))
    
    matrix, target = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3
    print(soln.searchMatrix(matrix,target))

#Time Complexity: O(log(m * n))
#Space Complexity: O(1)