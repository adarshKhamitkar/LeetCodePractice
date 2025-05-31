"""
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if (n == 0) or (s == s[::-1]): return s
        left, right = 0, 0
        res = []
        while(left<(n-1)):
            right = left+1
            while(right<=n):
                substr = s[left:right]
                if substr == substr[::-1]: res.append(substr)
                right+=1
            left+=1
        res.sort(key=len)
        return res.pop()
    
# Time Complexity: O(n^3)
# Space Complexity: O(n^2) for storing all substrings in res 
