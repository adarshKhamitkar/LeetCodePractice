"""
A shop is selling candies at a discount. For every two candies sold, the shop gives a third candy for free.

The customer can choose any candy to take away for free as long as the cost of the chosen candy is less than or equal to the minimum cost of the two candies bought.

For example, if there are 4 candies with costs 1, 2, 3, and 4, and the customer buys candies with costs 2 and 3, they can take the candy with cost 1 for free, but not the candy with cost 4.
Given a 0-indexed integer array cost, where cost[i] denotes the cost of the ith candy, return the minimum cost of buying all the candies.

 

Example 1:

Input: cost = [1,2,3]
Output: 5
Explanation: We buy the candies with costs 2 and 3, and take the candy with cost 1 for free.
The total cost of buying all candies is 2 + 3 = 5. This is the only way we can buy the candies.
Note that we cannot buy candies with costs 1 and 3, and then take the candy with cost 2 for free.
The cost of the free candy has to be less than or equal to the minimum cost of the purchased candies.
Example 2:

Input: cost = [6,5,7,9,2,2]
Output: 23
Explanation: The way in which we can get the minimum cost is described below:
- Buy candies with costs 9 and 7
- Take the candy with cost 6 for free
- We buy candies with costs 5 and 2
- Take the last remaining candy with cost 2 for free
Hence, the minimum cost to buy all candies is 9 + 7 + 5 + 2 = 23.
Example 3:

Input: cost = [5,5]
Output: 10
Explanation: Since there are only 2 candies, we buy both of them. There is not a third candy we can take for free.
Hence, the minimum cost to buy all candies is 5 + 5 = 10.
"""
from typing import List

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        if len(cost) == 0: return -1  # Edge case: no candies to buy
        cost.sort()
        minimum_cost = 0

        while(cost):
            if(len(cost) < 2):
                minimum_cost += cost.pop()
                break
            candy_i = cost.pop()
            candy_ii = cost.pop()
            if cost:
                free = cost.pop()
            minimum_cost += candy_i + candy_ii

        return minimum_cost
if __name__ == "__main__":
    obj = Solution()
    
    result = obj.minimumCost([1,2,3])
    print(result)  # Output: 5
    
    result = obj.minimumCost([6,5,7,9,2,2])
    print(result)  # Output: 23
    
    result = obj.minimumCost([5,5])
    print(result)  # Output: 10
    result = obj.minimumCost([1,2,3,4,5])
    print(result)  # Output: 12
    result = obj.minimumCost([1,2,3,4,5,6])
    print(result)  # Output: 16
    result = obj.minimumCost([1,2,3,4,5,6,7])
    print(result)  # Output: 24

    # Time Complexity: O(n log n) where n is the length of the cost array due to sorting.
    # Space Complexity: O(1) since we are using a constant amount of space for the minimum cost calculation.