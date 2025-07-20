"""
Given the root of a binary search tree and a target value, 
return the value in the BST that is closest to the target. 
If there are multiple answers, print the smallest.

Example 1:
Input: root = [4,2,5,1,3], target = 3.714286
Output: 4

Example 2:
Input: root = [1], target = 4.428571
Output: 1
"""

from typing import Optional

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target:float) -> int:
        def inOrder(node):
            return inOrder(node.left) + [node.val] + inOrder(node.right) if node else []
        
        return min(inOrder(root), key = lambda x: abs(x - target))
    

if __name__ == "__main__":
    # Example usage
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    target = 3.714286
    solution = Solution()
    print(solution.closestValue(root, target))  # Output: 4

    target2 = 4.428571
    root2 = TreeNode(1)
    print(solution.closestValue(root2, target2))  # Output: 1

#Time Complexity: O(n) where n is the number of nodes in the tree, as we traverse all nodes to create the in-order list.
#Space Complexity: O(n) for storing the in-order traversal of the tree in a list
