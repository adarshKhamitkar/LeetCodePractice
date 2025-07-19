"""
You are given the root node of a binary search tree (BST) and a value to insert into the tree. 
Return the root node of the BST after the insertion. 
It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, 
as long as the tree remains a BST after insertion. You can return any of them.

Example 1:
Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]

Example 2:
Input: root = [40,20,60,10,30,50,70],
val = 25
Output: [40,20,60,10,30,50,70,null,null,25]
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        t_node = TreeNode(val)
        if not root: return t_node

        def dfs(root, node):
            if not root.left and node.val < root.val:
                root.left = node
                return
            elif not root.right and node.val > root.val:
                root.right = node
                return
            else:
                if node.val < root.val:
                    dfs(root.left, node)
                else:
                    dfs(root.right, node)

        dfs(root, t_node)
        return root
    
# Example usage:
if __name__ == "__main__":
    # Create a sample BST
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    # Insert a value into the BST
    val = 5
    solution = Solution()
    new_root = solution.insertIntoBST(root, val)

    # Function to print the tree in-order for verification
    def print_in_order(node):
        if node:
            print_in_order(node.left)
            print(node.val, end=' ')
            print_in_order(node.right)

    print_in_order(new_root)  # Output should show the tree with the new value inserted
    # Expected output: 1 2 3 4 5 7
    # The output will show the in-order traversal of the BST after insertion.
    # The inserted value 5 should appear in the correct position in the output.
    # This confirms that the insertion was successful and the BST properties are maintained.
    # The output will be: 1 2 3 4 5 7

    #Time Complexity: O(h), where h is the height of the tree. In the worst case, this could be O(n) for a skewed tree.
    #Space Complexity: O(1) for the iterative approach, as we are not using any additional data structures that grow with the size of the input tree.