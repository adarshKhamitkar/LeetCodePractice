"""
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

class Solution:
    def lengthOfLongestSubstring(self,s:str)->int:
        _longest = 0 #to continuously update the maximum length of the longest non-repeating substr

        _hashset = set() #to store and check for repeating characters

        _l = 0 #to store the starting point of the substr.

        _n = len(s)
        _res = [] #optional, to store the non-repeating substrings

        for _r in range(_n):
            #if previously added to the set
            while s[_r] in _hashset:
                #untill all the duplicate charaters are in the substr s[_l:_r+1]
                _hashset.remove(s[_l])
                _l += 1

            #if not previously added to the set
            _hashset.add(s[_r]) #add the char to set if not previously found
            _window = (_r - _l) + 1 #calculate the current window length
            _res.append(s[_l:(_r+1)]) #optional, can be skipped
            _longest = max(_window, _longest) 
        
        return _longest
        