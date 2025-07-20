"""
Return the maximum element in a Binary Tree (BST).
"""
from typing import Optional

class TreeNode:
    def __init__(self,val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def returnMaxElement(self,root:Optional[TreeNode])-> int:
        def dfs(node, max_val):
            if node:
                if node.val > max_val:
                    max_val = node.val
                dfs(node.left,max_val)
                dfs(node.right,max_val)
            return max_val
        return max(dfs(root.left,root.val),dfs(root.right,root.val)) if root else -1
        

        
if __name__ == "__main__":
    # Example usage
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    solution = Solution()
    print(solution.returnMaxElement(root))  # Output: 20

    root2 = TreeNode(1)
    print(solution.returnMaxElement(root2))  # Output: 1

    root3 = None
    print(solution.returnMaxElement(root3))  # Output: -inf (or some defined value for empty tree)

    #time complexity: O(n) where n is the number of nodes in the tree, as we traverse all nodes.
    #space complexity: O(h) where h is the height of the tree, due to the recursion stack.
    #In the worst case (skewed tree), h can be O(n), but for balanced trees, h is O(log n).
    #Thus, the overall space complexity is O(h).
    #The time complexity is O(n) because we visit each node exactly once.
    #The space complexity is O(h) due to the recursion stack, which can go as deep as the height of the tree.
    #In a balanced tree, this is O(log n), but in a skewed tree, it can be O(n).