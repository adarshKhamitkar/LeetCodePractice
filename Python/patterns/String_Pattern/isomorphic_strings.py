"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:

Mapping 'e' to 'a'.
Mapping 'g' to 'd'.
Example 2:

Input: s = "foo", t = "bar"

Output: false

Explanation:

The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:

Input: s = "paper", t = "title"

Output: true

 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.

"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        map_s_t = {}
        map_t_s = {}

        for i,j in zip(s,t):
            if i not in map_s_t and j not in map_t_s:
                map_s_t[i] = j
                map_t_s[j] = i

            elif map_s_t.get(i) != j or map_t_s.get(j) != i:
                return False
        return True 