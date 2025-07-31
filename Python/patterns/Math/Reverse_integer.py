"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-2^31 <= x <= 2^31 - 1
"""

class Solution:
    def reverse(self, x: int) -> int:
        def reverse(s:str) -> str:
            return s[::-1]
        
        num = str(x)
        if num[0] != "-":
            return int(reverse(num)) if int(reverse(num)) <= ((2 ** 31) - 1) else 0
        else:
            return ((-1) * int(reverse(num[1:(len(num)+1)]))) if ((-1) * int(reverse(num[1:(len(num)+1)]))) >= ((-1) * (2 ** 31)) else 0

if __name__ == "__main__":
    sol = Solution()
    print(sol.reverse(123))   # Output: 321
    print(sol.reverse(-123))  # Output: -321
    print(sol.reverse(120))   # Output: 21
    print(sol.reverse(1534236469))  # Output: 0 (out of bounds)
    print(sol.reverse(-2147483648))  # Output: 0 (out of bounds)
    print(sol.reverse(0))  # Output: 0
    print(sol.reverse(100))  # Output: 1

#Time Complexity: O(n), where n is the number of digits in x.

