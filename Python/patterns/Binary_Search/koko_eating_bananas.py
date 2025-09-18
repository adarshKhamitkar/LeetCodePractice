"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. 
Each hour, she chooses some pile of bananas and eats k bananas from that pile. 
If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
"""

from typing import List
import math

class Solution:
    def minEatingSpeed(self,piles:List[int],h:int) -> int:
        l, r = 1, max(piles)

        res = r

        while l<=r:
            k = l + (r - l) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            if hours <= h:
                res = min(k, res)
                r = k - 1
            else:
                l = k + 1
        return res
    
if __name__ == "__main__":
    piles = [3,6,7,11]
    h = 8
    print(Solution().minEatingSpeed(piles,h))  # Output: 4

    piles = [30,11,23,4,20]
    h = 5
    print(Solution().minEatingSpeed(piles,h))  # Output: 30

    piles = [30,11,23,4,20]
    h = 6
    print(Solution().minEatingSpeed(piles,h))  # Output: 23


    #Time Complexity: O(n log m) where n is the number of piles and m is the maximum number of bananas in a pile.
    #Space Complexity: O(1) as we are using only a constant amount of extra space.