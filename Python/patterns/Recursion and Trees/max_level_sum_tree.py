"""
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

Example 1:
Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.

"""

import math
from typing import Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def maxLevelSum(self, root:Optional[TreeNode])-> int:
        if not root: return 0
        _levels = []
        _maxlevelsum = (-1,(-1) * math.inf)
        def dfs(node, level):
            if len(_levels) == level:
                _levels.append([])

            _levels[level].append(node.val)

            if node.left: dfs(node.left, level+1)
            if node.right: dfs(node.right, level+1)

        dfs(root, 0)

        for i, level in enumerate(_levels):
            _levelsum = sum(level)
            if _levelsum > _maxlevelsum[1]:
                _maxlevelsum = ((i+1), _levelsum)

        return _maxlevelsum[0]
    
if __name__ == "__main__":
    # Example usage:
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(0)
    root.left.left = TreeNode(7)
    root.left.right = TreeNode(-8)

    solution = Solution()
    print(solution.maxLevelSum(root))  # Output: 2

    # Another example
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(5)

    print(solution.maxLevelSum(root2))  # Output: 3
