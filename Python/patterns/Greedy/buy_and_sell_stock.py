"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        i=0
        for j in range(1, len(prices)):
            if prices[j] > prices[i]:
                curr_profit = prices[j] - prices[i]
                max_profit = max(max_profit, curr_profit)
            else: i = j
        return max_profit
    
    #Time Complexity: O(n) where n is the length of the prices array.
    #Space Complexity: O(1) as we are using a constant amount of space for variables.
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([7,1,5,3,6,4]))  # Output: 5
    print(solution.maxProfit([7,6,4,3,1]))    # Output: 0
    print(solution.maxProfit([1,2,3,4,5]))    # Output: 4
    print(solution.maxProfit([5,4,3,2,1]))    # Output: 0
    print(solution.maxProfit([3,2,6,5,0,3]))  # Output: 4
    print(solution.maxProfit([1,2,3,0,2]))    # Output: 2
