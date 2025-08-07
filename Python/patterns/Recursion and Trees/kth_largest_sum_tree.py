"""
You are given the root of a binary tree and a positive integer k.

The level sum in the tree is the sum of the values of the nodes that are on the same level.

Return the kth largest level sum in the tree (not necessarily distinct). If there are fewer than k levels in the tree, return -1.

Note that two nodes are on the same level if they have the same distance from the root.

 

Example 1:


Input: root = [5,8,9,2,1,3,7,4,6], k = 2
Output: 13
Explanation: The level sums are the following:
- Level 1: 5.
- Level 2: 8 + 9 = 17.
- Level 3: 2 + 1 + 3 + 7 = 13.
- Level 4: 4 + 6 = 10.
The 2nd largest level sum is 13.
Example 2:


Input: root = [1,2,null,3], k = 1
Output: 3
Explanation: The largest level sum is 3.
 

Constraints:

The number of nodes in the tree is n.
2 <= n <= 105
1 <= Node.val <= 106
1 <= k <= n
"""

import heapq
from typing import Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthlargestlevelsum(self, root:Optional[TreeNode], k:int) -> int:
        if not root: return -1

        _levels, _heap = [], []
        def dfs(node, level):
            if len(_levels) == level:
                _levels.append([])

            _levels[level].append(node.val)

            if node.left: dfs(node.left, level + 1)
            if node.right: dfs(node.right, level + 1)

        dfs(root, 0)

        if len(_levels) >= k:
            for level in _levels:
                heapq.heappush(_heap, sum(level))
                if len(_heap) > k:
                    heapq.heappop(_heap)

            return _heap[0]
        return -1
    
if __name__ == "__main__":
    # Example usage:
    root = TreeNode(5)
    root.left = TreeNode(8)
    root.right = TreeNode(9)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(1)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(4)
    root.left.left.right = TreeNode(6)

    solution = Solution()
    print(solution.kthlargestlevelsum(root, 2))  # Output: 13

    # Another example
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(None)
    root2.left.left = TreeNode(3)

    print(solution.kthlargestlevelsum(root2, 1))  # Output: 3