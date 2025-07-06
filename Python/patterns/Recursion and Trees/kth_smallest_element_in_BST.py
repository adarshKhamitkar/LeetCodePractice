"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1   

Example 2:
Input: root = [5,3,6,2,4,null,null,1],
k = 3
Output: 3
"""

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root == None: return 0

        def inorder_traversal(node: Optional[TreeNode])->List[int]:
            return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right) if node else []
        
        return inorder_traversal(root)[k-1]
    
if __name__ == "__main__":
    # Example usage
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)

    solution = Solution()
    print(solution.kthSmallest(root, 1))  # Output: 1

    root2 = TreeNode(5)
    root2.left = TreeNode(3)
    root2.right = TreeNode(6)
    root2.left.left = TreeNode(2)
    root2.left.right = TreeNode(4)
    root2.left.left.left = TreeNode(1)

    print(solution.kthSmallest(root2, 3))  # Output: 3

    # Time Complexity: O(n) where n is the number of nodes in the tree, as we traverse all nodes.
    # Space Complexity: O(n) for the list that stores the inorder traversal of the tree
    # The recursion stack can also take O(h) space where h is the height of the
    # tree, but in the worst case (skewed tree), h can be O(n).
    # This solution is not optimal for large trees, as it constructs a list of all elements
    # and then accesses the k-th element. A more optimal solution would use a counter during
    # the inorder traversal to stop when the k-th element is found, which would reduce the
    # space complexity to O(h) where h is the height of the tree.
    # However, this solution is straightforward and works well for small to moderate-sized trees.
            