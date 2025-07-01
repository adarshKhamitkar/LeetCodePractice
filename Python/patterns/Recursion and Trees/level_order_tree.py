"""
Given the root of a binary tree, return the level order traversal of its nodes' values. 
(i.e., from left to right, level by level).

Example1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
"""

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root:List[TreeNode]) -> List[List[int]]:
        if root == None: return []
        levels = []

        def counter(root, level):
            if len(levels) == level:
                levels.appen([])

            levels[level].append(root.val)

            if root.left: counter(root.left, level+1)
            if root.right: counter(root.right, level+1)

        counter(root,0)
        return levels
    
if __name__ == "__main__":
    # Example usage
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    solution = Solution()
    print(solution.levelOrder(root))  # Output: [[3], [9, 20], [15, 7]]
    root2 = TreeNode(1)
    print(solution.levelOrder(root2))  # Output: [[1]]
    root3 = None
    print(solution.levelOrder(root3))  # Output: []

    #Time Complexity: O(n) where n is the number of nodes in the tree.
    #Space Complexity: O(n) for the levels list that stores the values of nodes at each level.
    #The recursion stack can also take O(h) space where h is the height of the tree, but in the worst case (skewed tree), h can be O(n).
    #Thus, the overall space complexity is O(n).
    #The time complexity is O(n) because we visit each node exactly once.
    #The space complexity is O(n) because we store the values of all nodes in the levels list.

"""
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
"""

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None: return []
        levels = []

        def bottom_up_levels(levels):

            if len(levels) == 0: return []
            L, R = 0, len(levels)-1
            while(L<=R):
                levels[L], levels[R] = levels[R], levels[L]
                L, R = L+1, R-1

            return levels

        def counter(root, level):
            if len(levels) == level:
                levels.append([])

            if root.left:
                counter(root.left, level+1)
            if root.right:
                counter(root.right, level+1)

            levels[level].append(root.val)

        counter (root, 0)

        levels = bottom_up_levels(levels) 
        return levels

        