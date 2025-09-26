"""
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

 

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537
 

Constraints:

0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
"""

class Solution:
    def tribonacci(self, n: int) -> int:
        
        #using Tabulation; T = O(n); S = O(n)
        if n == 0: return 0
        if n == 1 or n == 2: return 1
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 1
        for i in range(3,len(dp)):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        return dp[n]
    
        #using memoization; T = O(n); S = O(n)
        # memo = {0:0, 1:1, 2:1}
        # def findTrib(n):
        #     if n not in memo:
        #         memo[n] = findTrib(n-3) + findTrib(n-2) + findTrib(n-1)
        #     return memo[n]
        # return findTrib(n)

        #using recursion; 31/38 passed; timelimit exceeded; T = O(3 ^ N), S = O(1)
        #if n == 0: return 0
        #elif n == 1: return 1
        #elif n == 2: return 1
        #else: return self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)
