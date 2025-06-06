"""
Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. 
In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.

 

Example 1:

Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
Example 2:

Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        L,R = 1,num
        while(L<=R):
            M = (L+R) // 2
            M_squared = M * M
            if (M_squared == num):
                return True
            elif M_squared < num:
                L = M + 1
            else:
                R = M - 1
        return False
# Example usage:
# sol = Solution()
# print(sol.isPerfectSquare(16))  # Output: True
# print(sol.isPerfectSquare(14))  # Output: False

# Time Complexity: O(log n)
# Space Complexity: O(1)
# The time complexity is O(log n) because we are using binary search to find the square root of the number.
# The space complexity is O(1) because we are using a constant amount of space for the variables L, R, M, and M_squared.