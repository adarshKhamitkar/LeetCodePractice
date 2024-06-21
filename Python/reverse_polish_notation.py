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
 

Constraints:

1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+":lambda x,y: x+y,
            "-":lambda x,y: x-y,
            "*":lambda x,y: x*y,
            "/":lambda x,y: int(x/y)
        }

        # current_position = 0
        # while(len(tokens) > 1 ):
        #     while(tokens[current_position] not in ["+","-","*","/"]):
        #         current_position+=1

        #     operator = tokens[current_position]
        #     operation = operations[operator]
        #     ele1 = int(tokens[current_position-2])
        #     ele2 = int(tokens[current_position-1])
        #     tokens[current_position] = operation(ele1,ele2)

        #     tokens.pop(current_position-2)
        #     tokens.pop(current_position-2)
        #     current_position-=1
        # return int(tokens[0])

        stack = []
        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                ele1 = int(stack.pop())
                ele2 = int(stack.pop())
                operation = operations[token]
                stack.append(operation(ele2,ele1))
        return stack.pop()
