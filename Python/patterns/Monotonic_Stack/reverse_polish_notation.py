"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""

class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        operations = {
            "+" : lambda x,y: x+y,
            "*" : lambda x,y: x*y,
            "-" : lambda x,y: x-y,
            "/" : lambda x,y: int(x/y)
        }
        
        for token in tokens:
            if token in operations:
                operation = operations[token]
                x = stack.pop()
                y = stack.pop()
                res = operation(y,x)
                stack.append(res)
            else:
                stack.append(int(token))
                
        return stack[-1]
    
if __name__ == "__main__":
    obj = Solution()
    print(obj.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])) # Output: 22
    print(obj.evalRPN(["4","13","5","/","+"])) # Output: 6
    print(obj.evalRPN(["2","1","+","3","*"])) # Output: 9
    print(obj.evalRPN(["2","3","+","4","*"])) # Output: 20

    #Time Complexity: O(n), where n is the number of tokens.
    #Space Complexity: O(n), where n is the number of tokens in the stack.