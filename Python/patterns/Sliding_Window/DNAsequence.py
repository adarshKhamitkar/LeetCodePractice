"""
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

 

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
 

Constraints:

1 <= s.length <= 105
s[i] is either 'A', 'C', 'G', or 'T'.
"""

from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        _n = len(s)
        _i = 0
        _ss = 0
        _hash = {}
        _res = []

        while (_ss <= _n):
            _ss = (_i + 10)
            _substr = s[_i:_ss]
            _hash[_substr] = _hash.get(_substr,0) + 1
            _i += 1

        for i in _hash:
            if _hash[i] > 1:
                _res.append(i)

        return _res
    
if __name__ == "__main__":
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    solution = Solution()
    print(solution.findRepeatedDnaSequences(s))  # Output: ["AAAAACCCCC","CCCCCAAAAA"]
    
    s2 = "AAAAAAAAAAAAA"
    print(solution.findRepeatedDnaSequences(s2))  # Output: ["AAAAAAAAAA"]

