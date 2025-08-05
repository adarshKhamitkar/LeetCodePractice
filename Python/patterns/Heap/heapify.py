"""
Implement the heapify function to convert a list into a heap in-place. The heap should satisfy the heap property, where each parent node is less than or equal to its child nodes.
This function should not return anything, but modify the list in-place to represent a valid heap.

Example 1:

Input: nums = [3, 1, 4, 1, 5, 9]
Output: [1, 1, 4, 3, 5, 9]
Explanation: The input list is transformed into a valid min-heap.

Example 2:

Input: nums = [10, 20, 15]
Output: [10, 20, 15]
Explanation: The input list is already a valid min-heap.

Constraints:

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
"""
class Solution:
    def heapify(self, nums):
        n = len(nums)
        
        # Build a min-heap
        for i in range(n // 2 - 1, -1, -1):
            self._sift_down(nums, n, i)
    
    def _sift_down(self, nums, n, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and nums[left] < nums[smallest]:
            smallest = left
        if right < n and nums[right] < nums[smallest]:
            smallest = right
        
        if smallest != i:
            nums[i], nums[smallest] = nums[smallest], nums[i]
            self._sift_down(nums, n, smallest)
        # No return needed, nums is modified in-place

    def heap_sort(self, nums):
        self.heapify(nums)
        n = len(nums)
        
        # Extract elements from the heap one by one
        for i in range(n - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self._sift_down(nums, i, 0)
        return nums