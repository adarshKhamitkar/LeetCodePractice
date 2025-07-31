"""
Add Digits:
Given an array of integers, the task is to repeatedly sum the digits of each integer until a single-digit result is obtained.
Then, return the maximum of these single-digit results.
Example:
Input: [38, 40, 44, 50, 60]
Output: 8

The single-digit results are:
38 -> 3 + 8 = 11 -> 1 + 1 = 2
40 -> 4 + 0 = 4
44 -> 4 + 4 = 8
50 -> 5 + 0 = 5
60 -> 6 + 0 = 6
The maximum single-digit result is 8.
"""

from typing import List

class Solution:
    def sumDigits(self, arr:List[int])-> int:
        def addDigits(num: int) -> int:
            total = 0
            while num != 0:
                num, r = divmod(num, 10)
                total += r
            return total
        res = []
        for i in arr:
            while len(str(i)) != 1:
                i = addDigits(i)
            res.append(i)
        _hashmap = {}
        ans = []
        for i in res:
            _hashmap[i] = _hashmap.get(i, 0) + 1

        max_val = _hashmap[max(_hashmap, key=_hashmap.get)]
        for i in _hashmap:
            if _hashmap[i] == max_val:
                ans.append(i)

        return max(ans)


if __name__ == "__main__":
    arr = [38, 40, 44, 50, 60]
    sol = Solution()
    print(sol.sumDigits(arr))  # Output: 8

    arr = [123, 456, 780, 1011, 2022, 3033]
    print(sol.sumDigits(arr))  # Output: 6

# Time Complexity: O(N * K) where N is the number of integers in the array and K is the maximum number of digits in any integer.
# Space Complexity: O(N) for storing the results in a list.