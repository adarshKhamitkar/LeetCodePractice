"""
Write an Algorithm to return the leaf nodes of a binary tree.
"""

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def returnLeafNodes(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        leaf_nodes = []
        def dfs(node):
            if node.left == None and node.right == None:
                leaf_nodes.append(node.val)
            else:
                if node.left: dfs(node.left)
                if node.right: dfs(node.right)

        dfs(root)
        return leaf_nodes
    
if __name__ == "__main__":
    # Example usage:
    # Constructing a binary tree:
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    solution = Solution()
    print(solution.returnLeafNodes(root))  # Output: [4, 5, 3]
