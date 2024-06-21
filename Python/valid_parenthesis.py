"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        # bracket_list = list(s)
        # stack = []
        # if(len(bracket_list) % 2 != 0): return False
        # for i in bracket_list:
        #     if len(stack) == 0:
        #         stack.append(i)
        #         continue
        #     if i == ")":
        #         if (stack.pop() != "("): return False
        #     elif i == "}":
        #         if (stack.pop() != "{"): return False
        #     elif i == "]":
        #         if (stack.pop() != "["): return False
        #     else:
        #         stack.append(i)
        # return True

        stack = []
        mapping = {"}":"{",")":"(","]":"["}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else "#"
                if mapping[char] != top_element: return False
            else:
                stack.append(char)
        return not stack
