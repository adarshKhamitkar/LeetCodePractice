"""
Given a binary tree with the following rules:

root.val == 0
For any treeNode:
If treeNode.val has a value x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
If treeNode.val has a value x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.

Implement the FindElements class:

FindElements(TreeNode* root) Initializes the object with a contaminated binary tree and recovers it.
bool find(int target) Returns true if the target value exists in the recovered binary tree.
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:
    def dfs(self, current_node, current_val):
        if current_node is None:
            return
        self.seen.add(current_val)
        self.dfs(current_node.left, (current_val * 2) + 1)
        self.dfs(current_node.right, (current_val * 2) + 2)

    def __init__(self, root:Optional[TreeNode]):
        self.seen = set()
        self.dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self.seen
    
if __name__ == "__main__":
    # Example usage
    root = TreeNode(-1)
    root.left = TreeNode(-1)
    root.right = TreeNode(-1)
    root.left.left = TreeNode(-1)
    root.left.right = TreeNode(-1)

    find_elements = FindElements(root)
    print(find_elements.find(0))  # Output: True
    print(find_elements.find(1))  # Output: True
    print(find_elements.find(2))  # Output: True
    print(find_elements.find(3))  # Output: True
    print(find_elements.find(4))  # Output: False